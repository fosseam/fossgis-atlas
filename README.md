# FOSSGIS Atlas – Meta Landscape of the Conferences

🇩🇪 (deu) -> liesmich.md

Or in other words: a kind of conference cartography 2025++.

A curated, data-driven meta-archive of the FOSSGIS conferences – structured, visualized, interlinked.

This project collects, structures, and analyzes all publicly available content from the FOSSGIS 2025 conference – including videos, abstracts, slides, and view counts. The goal is to create an interactive meta-landscape that provides orientation within the thematic diversity of the conferences.

Possible data sources:

- [media.ccc.de – FOSSGIS 2025](https://media.ccc.de/c/fossgis2025)
- [YouTube Playlist](https://www.youtube.com/playlist?list=PLTli5-lbeoia6iMs0ncbq6-N3ngH9Hs5C)
- [Pretalx Conference Schedule](https://pretalx.com/fossgis2025)

## Project Goals

- Three-level taxonomy (Supergroup → Group → Subgroup)
- Master tables with over 200 program items, including talks, workshops, lightning talks, links, durations, and view counts
- Interactive visualizations (heatmaps, tree views, watchlists)
- JupyterLab environment via Binder
- DOI-based releases via Zenodo (Working Paper & Dataset)

## Launch Notebook (via Binder)

tbd.

## Project Structure

```
notebooks/     → Jupyter notebooks (data import, analysis, visualization)
data/          → Raw data from Pretalx, CCC, YouTube
exports/       → Snapshots & final CSVs
docs/          → Project description, phase model, tree views, etc.
requirements.txt
README.md
```

## Contribute & Collaborate

Like the idea?
We welcome support, suggestions, and critical feedback – whether through Issues, Pull Requests, or Peer Reviews.

This project is under active development and open to:

- Extensions to taxonomy and categorization
- New approaches to analysis or visualization (e.g., with QGIS, Streamlit, TimelineJS)
- Validation and curation of content
- Export formats, watchlists, filters, mapping concepts
- OpenScience peer reviews

For larger contributions or collaborations, feel free to reach out – or open an issue in the repository.

## Citation

**DOI:** Will be assigned via Zenodo upon first release

- The current state is planned as a Working Paper
- Future snapshots and final datasets will each receive their own DOI
- This repository will also be synced with Zenodo on every release

## Licensing

**Code & Notebooks:**
[GNU General Public License v3.0 or later (GPL-3.0+)](https://www.gnu.org/licenses/gpl-3.0.html)

**Documentation & Content (README, Phase Model, Tree, etc.):**
[Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

