# Data sources

## ATUS 2003–2024
Official BLS landing page:
https://www.bls.gov/tus/data/datafiles-0324.htm

Files staged:
- atusresp-0324.zip
- atusrost-0324.zip
- atusact-0324.zip
- atussum-0324.zip
- atuswho-0324.zip
- atuscps-0324.zip

## Time-Series-Library
Hugging Face dataset:
https://huggingface.co/datasets/thuml/Time-Series-Library

The downloader stages electricity, traffic, weather, exchange rate and ETT-small.

## GIFT-Eval
Optional broader benchmark:
https://huggingface.co/datasets/Salesforce/GiftEval

## Freeze rule
Every automated acquisition emits SHA-256 hashes and a JSON manifest. Formal experiment jobs should consume the frozen snapshot, not redownload live data.
