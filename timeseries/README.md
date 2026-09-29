# Redundancy-aware Time-Series Retrieval

Data staging for the retrieval-augmented forecasting project.

Core seed datasets:
- electricity
- traffic
- weather
- exchange_rate
- ETT (ETTh1/ETTh2/ETTm1/ETTm2)

Primary diagnostics include duplicate sensitivity, retrieval diversity, effective-neighbour ratio M_eff/K, variance shrinkage, misleading/OOD-neighbour robustness, rare-pattern recovery, MSE and MAE.

The GitHub Action downloads the canonical THUML Time-Series-Library copies and freezes a manifest. GIFT-Eval is kept as an optional broader benchmark rather than silently mixed into the original seed suite.
