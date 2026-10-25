# liljanabottigliero.com

Yana Bottigliero's portfolio site. Static HTML on GitHub Pages, custom domain via `CNAME`.

- `template.html` is the page layout. `build.py` holds the portfolio pieces and awards and writes `index.html`.
- To add a clip or award: edit the `WORKS` or `AWARDS` list in `build.py`, then run `python3 build.py index.html template.html`.
- Images live in `files/img/`, PDFs in `files/pdf/`.
- Push to `main` to deploy.
