#!/usr/bin/env python3
"""Import PPC-related conversations from a ChatGPT data export into this repo.

Usage:
    python3 -I scripts/import_chatgpt_export.py <export.zip | export-folder | conversations.json>
        [--out imports/chatgpt/conversations] [--min-hits 3] [--all] [--extra-keywords "foo,bar"]

How to get the export: ChatGPT -> Settings -> Data controls -> Export data.
You get an emailed link to a ZIP that contains conversations.json.

The ZIP is read in memory and nothing is extracted. Output:
  - one Markdown file per matching conversation
  - INDEX.md: a checklist of imported chats, which you use when deleting them in ChatGPT
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import zipfile
from pathlib import Path

DEFAULT_KEYWORDS = [
    # platforms
    "google ads", "adwords", "performance max", "pmax", "meta ads", "facebook ads",
    "instagram ads", "ads manager", "linkedin ads", "campaign manager", "microsoft ads",
    "bing ads", "microsoft advertising", "reddit ads", "x ads", "twitter ads",
    "chatgpt ads", "ads.openai.com",
    # PPC vocabulary
    "ppc", "cpc", "cpl", "cpa", "cpm", "ctr", "roas", "quality score", "ad copy",
    "ad group", "ad set", "adset", "negative keyword", "keyword", "bid strategy",
    "target cpa", "max conversions", "retargeting", "remarketing", "lookalike",
    "custom audience", "customer match", "lead form", "conversion", "pixel",
    "conversions api", "capi", "utm", "landing page", "campaign", "headline",
    "impression share", "budget",
]


def load_conversations(src: Path) -> list[dict]:
    """Return the list of conversations from a ZIP, folder or JSON file."""
    convs: list[dict] = []

    def add(raw: bytes, name: str) -> None:
        data = json.loads(raw.decode("utf-8"))
        if isinstance(data, dict):  # some exports wrap the list
            data = data.get("conversations", [data])
        if not isinstance(data, list):
            raise ValueError(f"{name}: unexpected JSON shape")
        convs.extend(c for c in data if isinstance(c, dict))

    if src.is_file() and zipfile.is_zipfile(src):
        with zipfile.ZipFile(src) as zf:
            names = [n for n in zf.namelist()
                     if re.search(r"(^|/)conversations[^/]*\.json$", n)]
            if not names:
                sys.exit("No conversations*.json found inside the ZIP.")
            for n in sorted(names):
                add(zf.read(n), n)
    elif src.is_dir():
        files = sorted(src.glob("conversations*.json"))
        if not files:
            sys.exit(f"No conversations*.json in {src}")
        for f in files:
            add(f.read_bytes(), f.name)
    elif src.is_file():
        add(src.read_bytes(), src.name)
    else:
        sys.exit(f"Not found: {src}")
    return convs


def part_to_text(part) -> str:
    if isinstance(part, str):
        return part
    if isinstance(part, dict):
        ctype = part.get("content_type", "")
        if "image" in ctype or "asset_pointer" in part:
            return "_[image omitted]_"
        if "text" in part and isinstance(part["text"], str):
            return part["text"]
    return ""


def message_text(msg: dict) -> str:
    content = msg.get("content") or {}
    ctype = content.get("content_type")
    if ctype in ("text", "multimodal_text"):
        return "\n".join(t for t in (part_to_text(p) for p in content.get("parts") or []) if t)
    if ctype == "code":
        return f"```\n{content.get('text', '')}\n```"
    return ""  # skip tool output, browsing results, thoughts, etc.


def linear_thread(conv: dict) -> list[tuple[str, str, float | None]]:
    """Follow current_node back to the root to get the branch the user last saw."""
    mapping = conv.get("mapping") or {}
    node_id = conv.get("current_node")
    if node_id not in mapping:  # fallback: pick any leaf node
        leaves = [k for k, v in mapping.items() if not v.get("children")]
        node_id = leaves[-1] if leaves else None
    chain = []
    seen = set()
    while node_id and node_id in mapping and node_id not in seen:
        seen.add(node_id)
        node = mapping[node_id]
        msg = node.get("message")
        if msg:
            role = (msg.get("author") or {}).get("role", "")
            hidden = (msg.get("metadata") or {}).get("is_visually_hidden_from_conversation")
            text = message_text(msg).strip()
            if role in ("user", "assistant") and text and not hidden:
                chain.append((role, text, msg.get("create_time")))
        node_id = node.get("parent")
    chain.reverse()
    return chain


def score(title: str, body: str, keywords: list[str]) -> tuple[int, list[str], bool]:
    hay = body.lower()
    t = title.lower()
    hits, matched, in_title = 0, [], False
    for kw in keywords:
        pat = re.compile(r"(?<![a-z0-9])" + re.escape(kw) + r"(?![a-z0-9])")
        n = len(pat.findall(hay))
        if pat.search(t):
            in_title = True
            n += 1
        if n:
            hits += n
            matched.append(kw)
    return hits, matched, in_title


def slugify(s: str, n: int = 60) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return (s[:n].rstrip("-")) or "untitled"


def ts(x) -> str:
    try:
        return dt.datetime.fromtimestamp(float(x), dt.timezone.utc).strftime("%Y-%m-%d")
    except (TypeError, ValueError, OSError):
        return "unknown-date"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", type=Path)
    ap.add_argument("--out", type=Path, default=Path("imports/chatgpt/conversations"))
    ap.add_argument("--min-hits", type=int, default=3,
                    help="minimum keyword hits in the body if no keyword appears in the title (default 3)")
    ap.add_argument("--all", action="store_true", help="import every conversation, with no filtering")
    ap.add_argument("--extra-keywords", default="", help="comma-separated extra keywords")
    args = ap.parse_args()

    keywords = DEFAULT_KEYWORDS + [k.strip().lower() for k in args.extra_keywords.split(",") if k.strip()]
    convs = load_conversations(args.source)
    args.out.mkdir(parents=True, exist_ok=True)

    imported, skipped = [], 0
    for conv in convs:
        title = conv.get("title") or "Untitled"
        thread = linear_thread(conv)
        body = "\n".join(t for _, t, _ in thread)
        hits, matched, in_title = score(title, body, keywords)
        if not args.all and not (in_title or hits >= args.min_hits):
            skipped += 1
            continue
        date = ts(conv.get("create_time"))
        cid = conv.get("conversation_id") or conv.get("id") or ""
        fname = f"{date}-{slugify(title)}.md"
        path = args.out / fname
        i = 2
        while path.exists():
            path = args.out / f"{date}-{slugify(title)}-{i}.md"
            i += 1
        lines = [
            f"# {title}", "",
            f"- Source: ChatGPT export",
            f"- Created: {date} · Last updated: {ts(conv.get('update_time'))}",
            f"- Conversation ID: `{cid}`",
            f"- Matched keywords: {', '.join(matched[:15]) or '—'}",
            "- Status: ☐ reviewed  ☐ key points moved into platform folders / learnings.md  ☐ deleted in ChatGPT",
            "", "---", "",
        ]
        for role, text, _ in thread:
            lines += [f"### {'You' if role == 'user' else 'ChatGPT'}", "", text, ""]
        path.write_text("\n".join(lines), encoding="utf-8")
        imported.append((date, title, cid, path.name, hits))

    imported.sort()
    index = args.out.parent / "INDEX.md"
    rows = [
        "# ChatGPT import — index", "",
        f"Imported {len(imported)} of {len(convs)} conversations "
        f"(skipped {skipped} that didn't look PPC-related). Generated {dt.date.today()}.", "",
        "Delete a chat in ChatGPT only after its file has been reviewed and its key points have been moved into the repo.", "",
        "| ✓ Deleted in ChatGPT | Date | Title | File | Keyword hits |",
        "|---|---|---|---|---|",
    ]
    rows += [f"| ☐ | {d} | {t.replace('|', '/')} | [{f}](conversations/{f}) | {h} |"
             for d, t, _, f, h in imported]
    index.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"Imported {len(imported)} / {len(convs)} conversations -> {args.out}")
    print(f"Index: {index}")


if __name__ == "__main__":
    main()
