# World News in One Image — 19 November 2026

[![news-image-20261119](https://make.fun/c/news-image-20261119/badge)](https://make.fun/c/news-image-20261119)

A triptych by region — **AMERICAS / EUROPE / ASIA-PACIFIC** — summing up
Thursday 19 November 2026 in one image. Six verified stories, two per
region, under one big date header.

## Stories

| Region | Story |
|---|---|
| Americas | Anthropic debuts on Nasdaq — shares soar ~34% on day one, valued near $2 trillion |
| Americas | US Senate rejects Iran war-powers bid, 51–48 |
| Europe | World Court: Myanmar committed genocide against the Rohingya (9–6), reparations ordered |
| Europe | EU proposes €45bn loan for Ukraine |
| Asia-Pacific | Trump, Xi & Putin hold first three-way summit in Shenzhen — "Declaration toward Peace" |
| Asia-Pacific | APEC adopts the Shenzhen Outlook on trade, data and AI risks |

## How it runs

`main.py` (Python stdlib only, no network) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`) and checks
the PNG magic bytes. The image is 1024×1024 PNG, under 1 MiB.
