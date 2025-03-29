# FOSSGIS Atlas – Meta-Landscape zu den Konferenzen

🇺🇳 🇺🇸 🇬🇧 (eng) -> readme.md  

Mit anderen Worten eine Art Konferenzkartografierung 2025++.

Also ein kuratiertes, datengetriebenes Meta-Archiv der FOSSGIS-Konferenzen – strukturiert, visualisiert, verlinkt.

Dieses Projekt sammelt, strukturiert und analysiert alle öffentlich verfügbaren Inhalte der FOSSGIS-Konferenz 2025 – darunter Videos, Abstracts, Slides und View-Zahlen. Ziel ist eine interaktive Meta-Landkarte, die Orientierung in der Themenvielfalt der Konferenzen ermöglicht.

Mögliche Datenquellen:

- [media.ccc.de – FOSSGIS 2025](https://media.ccc.de/c/fossgis2025)
- [YouTube-Playlist](https://www.youtube.com/playlist?list=PLTli5-lbeoia6iMs0ncbq6-N3ngH9Hs5C)
- [Pretalx-Konferenzplan](https://pretalx.com/fossgis2025)

## Projektziele

- Drei-stufige Taxonomie (Supergruppe → Gruppe → Untergruppe)
- Master-Tabellen mit über 200 Programmpunkten, inkl. Vorträgen, Workshops, Lightning Talks, Links, Dauer, Viewzahlen
- Interaktive Visualisierungen (Heatmap, Tree-View, Watchlists)
- JupyterLab-Umgebung via Binder
- DOI-fähige Releases über Zenodo (Working Paper & Dataset)

## Notebook starten (via Binder)

https://mybinder.org/v2/gh/fosseam/fossgis-atlas/main?labpath=notebooks/0_fossgis_atlas_main.ipynb


## Projektstruktur

```
notebooks/     → Jupyter Notebooks (Datenimport, Analyse, Visualisierung)
data/          → Rohdaten aus Pretalx, CCC, YouTube
exports/       → Snapshots & finale CSVs
docs/          → Projektbeschreibung, Phasenmodell, Tree-Views etc.
requirements.txt
README.md
liesmich.md
```


## Mögliche Abhängigkeiten

| Paket           | Zweck                                        |
|------------------|---------------------------------------------|
| `jupyterlab`     | Dein UI, läuft auch über Binder              |
| `requests`       | Für Pretalx- und media.ccc-Downloads         |
| `beautifulsoup4` | HTML-Scraping von media.ccc + YouTube        |
| `pandas`         | Tabellenstruktur für Masterdataset           |
| `plotly`         | Interaktive Visualisierung                   |
| `yt-dlp`         | YouTube-Metadaten extrahieren ohne API-Key   |


**Optional:** Geo/Mapping (später ggf. aktivieren)
- geopandas
- ipyleaflet



## Mitmachen & Beiträge

Dir gefällt diese Idee hier?
Dann freuen wir uns über Unterstützung, Ideen und kritische Rückmeldungen – ob in Form von Issues, Pull Requests oder Peer Reviews.

Das Projekt befindet sich im Aufbau und ist offen für:

- Ergänzungen zu Taxonomie und Kategorien
- neue Analyse- oder Visualisierungsansätze (z. B. mit QGIS, Streamlit, TimelineJS)
- Validierung und Kuratierung von Inhalten
- Exportformate, Watchlists, Filterideen, Mapping-Konzepte
- OpenScience Peer Reviews

Für größere Beiträge oder Kollaboration sprich uns gern direkt an – oder eröffne ein Issue im Repository.

## Zitierung;

**DOI:** Wird bei erstem Release über Zenodo vergeben

- Der aktuelle Entwicklungsstand ist als Working Paper geplant
- Zukünftige Snapshots und finale Datasets erhalten jeweils eigene DOIs
- Und auch diese Repo wird mit Zenodo pro Release synchronisiert

## Lizenzierung

\
**Code & Notebooks:**[GNU General Public License v3.0 or later (GPL-3.0+)](https://www.gnu.org/licenses/gpl-3.0.html)

**Dokumentation & Inhalte (README, Phasenmodell, Tree etc.):**\
[Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
