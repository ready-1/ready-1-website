#!/usr/bin/env python3
"""Validate generated site structure, metadata, assets, and local links."""

from __future__ import annotations

import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup


SITE_ORIGIN = "https://www.getready1.com"
ALLOWED_PDFS = {"ready-1-labor-and-travel-policy-20240101.pdf"}
REQUIRED_FILES = {
    ".nojekyll",
    "404.html",
    "CNAME",
    "about/index.html",
    "archives.html",
    "contact/index.html",
    "index.html",
    "sitemap.xml",
    "the-history-and-science-of-color-temperature.html",
}


def local_target(output_dir: Path, url: str) -> Path | None:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc:
        if f"{parsed.scheme}://{parsed.netloc}" != SITE_ORIGIN:
            return None
        path = parsed.path or "/"
    else:
        path = parsed.path

    if not path.startswith("/"):
        return None

    relative = Path(unquote(path).lstrip("/"))
    if not relative.parts:
        relative = Path("index.html")
    elif path.endswith("/"):
        relative /= "index.html"
    elif not relative.suffix:
        relative /= "index.html"
    return output_dir / relative


def validate(output_dir: Path) -> list[str]:
    errors: list[str] = []

    for relative_path in sorted(REQUIRED_FILES):
        if not (output_dir / relative_path).exists():
            errors.append(f"missing required output: {relative_path}")

    cname = output_dir / "CNAME"
    if cname.exists() and cname.read_text(encoding="utf-8").strip() != "www.getready1.com":
        errors.append("CNAME must contain www.getready1.com")

    source_pdfs = Path("content/pdfs")
    published_documents = {
        path.relative_to(source_pdfs).as_posix()
        for path in source_pdfs.rglob("*")
        if path.is_file()
    }
    unexpected_pdfs = published_documents - ALLOWED_PDFS
    if unexpected_pdfs:
        errors.append(f"unexpected publishable PDFs: {', '.join(sorted(unexpected_pdfs))}")

    html_files = sorted(output_dir.rglob("*.html"))
    if not html_files:
        errors.append("no generated HTML files found")
        return errors

    for html_file in html_files:
        relative_path = html_file.relative_to(output_dir)
        soup = BeautifulSoup(html_file.read_text(encoding="utf-8"), "html.parser")

        title = soup.title.string.strip() if soup.title and soup.title.string else ""
        if not title:
            errors.append(f"{relative_path}: missing title")

        if not soup.find("meta", attrs={"name": "description", "content": True}):
            errors.append(f"{relative_path}: missing meta description")

        canonicals = soup.find_all("link", rel="canonical")
        if len(canonicals) != 1:
            errors.append(f"{relative_path}: expected exactly one canonical URL")
        else:
            canonical = canonicals[0].get("href", "")
            if not canonical.startswith(SITE_ORIGIN):
                errors.append(f"{relative_path}: canonical uses the wrong origin")
            if canonical.endswith("/index.html"):
                errors.append(f"{relative_path}: canonical exposes index.html")

        if not soup.find("meta", property="og:image", content=True):
            errors.append(f"{relative_path}: missing Open Graph image")
        if not soup.find("meta", attrs={"name": "twitter:image", "content": True}):
            errors.append(f"{relative_path}: missing Twitter image")

        seen_ids: set[str] = set()
        for element in soup.find_all(id=True):
            element_id = element["id"]
            if element_id in seen_ids:
                errors.append(f"{relative_path}: duplicate id {element_id!r}")
            seen_ids.add(element_id)

        for image in soup.find_all("img"):
            if not image.has_attr("alt"):
                errors.append(f"{relative_path}: image is missing alt text")

        for element, attribute in [
            *((anchor, "href") for anchor in soup.find_all("a", href=True)),
            *((link, "href") for link in soup.find_all("link", href=True)),
            *((script, "src") for script in soup.find_all("script", src=True)),
            *((image, "src") for image in soup.find_all("img", src=True)),
        ]:
            url = element.get(attribute, "")
            if url.startswith(("#", "mailto:", "tel:")):
                continue
            target = local_target(output_dir, url)
            if target is not None and not target.exists():
                errors.append(f"{relative_path}: broken local reference {url}")

    homepage_heading = "Keep the picture clean."
    for relative_path in ["author/bob-king.html", "category/concepts.html"]:
        generated_file = output_dir / relative_path
        if generated_file.exists() and homepage_heading in generated_file.read_text(encoding="utf-8"):
            errors.append(f"{relative_path}: incorrectly renders the homepage")

    return errors


def main() -> int:
    output_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "output").resolve()
    if not output_dir.is_dir():
        print(f"error: output directory does not exist: {output_dir}", file=sys.stderr)
        return 2

    errors = validate(output_dir)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Validated {len(list(output_dir.rglob('*.html')))} HTML files in {output_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
