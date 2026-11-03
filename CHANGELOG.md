# Changelog

## 0.1.0 (unreleased)

First release as a standalone package, extracted from the gov.ie Wagtail codebase
(`ogcio/govie-wagtail`). Based on [wagtailcharts](https://github.com/overcastsoftware/wagtailcharts) 0.6.3.

Changes from wagtailcharts 0.6.3 made while the code lived in gov.ie:

- Python package renamed from `wagtailcharts` to `wagtail_charts`.
- Chart.js upgraded from v3.7.1 to v4.5.1; Jspreadsheet CE v5 and jSuites v6.
- New chart types: pyramid and scatter (with chart markers).
- New settings: point style, aspect ratio, chart title, column as dataset,
  X tick label step, chart navigator and logarithmic Y axes.
- Custom admin icon, and dark theme support for the spreadsheet editor.
- Fixes to tooltip labels, label formatting and left/right Y axis indexing.

Changes made for packaging:

- `chart_block.html` no longer depends on a project-specific `core_tags` library;
  `generate_uuid4` is now provided by `wagtailcharts_tags`.
- The admin icon is registered from `wagtail_hooks.py`, so it no longer depends on
  `wagtail_charts.blocks` being imported first.
