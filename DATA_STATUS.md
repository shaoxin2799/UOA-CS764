# Dataset staging status — 2026-09-30

## Frozen and published

| Dataset | Snapshot | Release asset |
|---|---|---|
| ATUS | BLS 2003–2024 six-file multi-year release | `atus-2003-2024.zip` |
| BRFSS | CDC 2024 combined landline/cellphone XPT + codebook | `brfss-2024.zip` |
| THUML seed suite | Electricity, Traffic, Weather, Exchange Rate, ETTh1/2, ETTm1/2 | `timeseries-thuml-seed.zip` |
| GIFT-Eval | Full Salesforce/GiftEval snapshot | `gifteval.zip` |

Release tag: `research-data-2026-09-30`

Each frozen asset is accompanied by SHA-256 verification in `SHA256SUMS.txt`.

## NSHAP

Target studies are pinned:
- ICPSR 20541 — Round 1, version 10
- ICPSR 34921 — Round 2, version 5
- ICPSR 36873 — Round 3 + COVID-19, version 9

The public-use studies are available through ICPSR/NACDA, but ICPSR requires account/institutional authentication for download and rejects anonymous cloud-runner access. The automated probe records this access boundary. Restricted-use files are deliberately not requested or bypassed.

Therefore NSHAP raw public-use files are the only unfrozen input; all other previously discussed public datasets are frozen and published.
