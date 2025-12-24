# KPI Snapshot (PaySim Sample)

## Key Metrics

- **Total transactions**: 10,000
- **Total value**: 1,830,226,100.59
- **Average value**: 183,022.61
- **Fraud Rate**: 0.1300%
- **Flagged Fraud Rate**: 0.0000%

## Key Insights
- Portfolio mix is concentrated by transaction type (see notebook chart).
- Fraud exists at a low rate(0.13%) but spikes across time steps.
- Flagged fraud is far below observed fraud, indicating a detection gap.

## Recommendations
- Improve detection using a two-stage approach: simple rules + lightweight model.
- Add monitoring/alerts for fraud rate by time and transaction type.
