# Ready-1 Website

Static website for [Ready-1](https://www.getready1.com), built with Pelican and a custom Bootstrap theme.

## Local Development

Python 3.13 is the supported development version.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
make html
make serve PORT=8000
```

The local site is available at `http://localhost:8000`.

## Production Build

```sh
make publish
python scripts/validate_site.py output
```

Generated files under `output/` are intentionally ignored and must not be committed.

## Deployment

Pushes to `main` run `.github/workflows/pages.yml`. The workflow audits Python dependencies, builds and validates the site, then deploys the generated artifact through GitHub Pages.

The custom domain and `.nojekyll` marker are maintained in `content/extras/` and copied to the artifact root by Pelican.

GitHub Pages does not support repository-defined HTTP response headers. The templates provide a restrictive Content Security Policy and referrer policy in HTML; stronger response headers would require placing a configurable CDN in front of Pages.

## Published Documents

Everything under `content/pdfs/` is public. `scripts/validate_site.py` enforces an explicit allowlist so private business documents cannot be published accidentally.
