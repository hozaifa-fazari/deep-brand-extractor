#!/usr/bin/env python3
"""Assemble a brand report body into a standalone HTML file, then print it to PDF.

Fonts are fetched once from Google Fonts and cached, then base64-inlined, so the
produced HTML is a single portable file that renders Arabic (RTL) correctly with
no network access. The PDF is printed with headless Chromium via Playwright.

    python3 tools/render-pdf.py brand/<name>-body.html \
        --css brand/assets/report.css \
        --title "..." --footer "..." --out brand/<name>.pdf
"""

import argparse
import base64
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

FONT_QUERY = (
    "https://fonts.googleapis.com/css2"
    "?family=IBM+Plex+Sans+Arabic:wght@400;600;700"
    "&family=IBM+Plex+Sans:wght@400;600;700"
    "&family=IBM+Plex+Mono:wght@400"
    "&display=swap"
)
# Google serves woff2 only to browser-like clients.
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
SUBSETS = {"arabic", "latin"}
CACHE = Path(os.environ.get("BRAND_FONT_CACHE", Path.home() / ".cache" / "deep-brand-fonts"))


def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def inline_fonts() -> str:
    """Return @font-face rules with the woff2 payloads base64-inlined."""
    CACHE.mkdir(parents=True, exist_ok=True)
    cached = CACHE / "inline-fonts.css"
    if cached.exists():
        return cached.read_text(encoding="utf-8")

    css = _get(FONT_QUERY).decode("utf-8")
    rules, seen = [], set()
    for subset, body in re.findall(r"/\*\s*([a-z0-9-]+)\s*\*/\s*@font-face\s*\{(.*?)\}", css, re.S):
        if subset not in SUBSETS:
            continue
        family = re.search(r"font-family:\s*'([^']+)'", body).group(1)
        weight = re.search(r"font-weight:\s*(\d+)", body).group(1)
        url = re.search(r"url\((https://[^)]+)\)", body).group(1)
        urange = re.search(r"unicode-range:\s*([^;]+);", body)
        key = (family, weight, subset)
        if key in seen:
            continue
        seen.add(key)

        blob = CACHE / url.rsplit("/", 1)[-1]
        if not blob.exists():
            blob.write_bytes(_get(url))
        payload = base64.b64encode(blob.read_bytes()).decode()
        rules.append(
            f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};"
            f"src:url(data:font/woff2;base64,{payload}) format('woff2');"
            + (f"unicode-range:{urange.group(1).strip()};" if urange else "")
            + "}"
        )

    out = "\n".join(rules)
    cached.write_text(out, encoding="utf-8")
    return out


def build_html(body: str, css: str, title: str, lang: str, direction: str) -> str:
    return (
        f'<!doctype html>\n<html lang="{lang}" dir="{direction}">\n<head>\n'
        f'<meta charset="utf-8">\n'
        f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{title}</title>\n<style>\n{inline_fonts()}\n{css}\n</style>\n"
        f"</head>\n<body>\n{body}\n</body>\n</html>\n"
    )


FOOTER = """
<div style="width:100%;font-size:7pt;color:#9C9A91;padding:0 16mm;
            font-family:'IBM Plex Sans',sans-serif;display:flex;
            justify-content:space-between;align-items:center;">
  <span>__LABEL__</span>
  <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
</div>"""


def chromium_path() -> str | None:
    """Prefer an already-installed Chromium over whichever build Playwright pins."""
    explicit = os.environ.get("CHROMIUM_PATH")
    if explicit:
        return explicit
    root = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))
    for candidate in sorted(root.glob("chromium-*/chrome-linux/chrome"), reverse=True):
        return str(candidate)
    return None


def to_pdf(html_path: Path, pdf_path: Path, footer_label: str, outline: bool = False) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"], executable_path=chromium_path())
        page = browser.new_page()
        page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=FOOTER.replace("__LABEL__", footer_label),
            margin={"top": "17mm", "bottom": "20mm", "left": "16mm", "right": "16mm"},
            # headings become PDF bookmarks; needs a tagged PDF
            outline=outline,
            tagged=outline,
        )
        browser.close()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("body", type=Path, help="HTML fragment holding the report content")
    ap.add_argument("--css", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True, help="destination .pdf")
    ap.add_argument("--title", required=True)
    ap.add_argument("--footer", default="", help="text shown at the foot of every page")
    ap.add_argument("--lang", default="ar")
    ap.add_argument("--dir", dest="direction", default="rtl", choices=["rtl", "ltr"])
    ap.add_argument("--outline", action="store_true",
                    help="add a bookmark tree built from the document headings")
    args = ap.parse_args()

    html = build_html(
        args.body.read_text(encoding="utf-8"),
        args.css.read_text(encoding="utf-8"),
        args.title,
        args.lang,
        args.direction,
    )
    html_path = args.out.with_suffix(".html")
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html, encoding="utf-8")

    to_pdf(html_path, args.out, args.footer or args.title, args.outline)
    print(json.dumps({
        "html": str(html_path), "html_bytes": html_path.stat().st_size,
        "pdf": str(args.out), "pdf_bytes": args.out.stat().st_size,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
