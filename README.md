# Research Data Staging

This repository is used as a temporary reproducibility and data-transfer hub for active experiments.

## AAMAS social-simulation extension

Data roles and acquisition rules are under `aamas/`. ATUS 2003–2024 is automated; BRFSS is kept year-explicit; NSHAP remains authenticated/licensed-only.

## Redundancy-aware time-series retrieval

The `timeseries/` area stages the original forecasting seed suite (electricity, traffic, weather, exchange rate, ETT) plus optional GIFT-Eval expansion.

## Workflows

- `Fetch ATUS 2003-2024` → downloads the six official BLS ZIPs, validates archives, hashes them, builds a manifest, and publishes an artifact.
- `Fetch time-series seed data` → downloads canonical THUML copies, hashes them, builds a manifest, and publishes an artifact.

Formal experiment code should consume frozen artifacts/local snapshots rather than live-download external data during runs.
