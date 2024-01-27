# MT-Thresholds

Local version of the [online tool](https://kocmitom.github.io/MT-Thresholds). Use either from the command-line:
```bash
# accuracy is 63.989%
mt-thresholds bleu 1.00

# ChrF needs 0.710 difference for the same accuracy as BLEU
mt-thresholds chrf 0.63989 --delta
```

Or it can be used from Python:
```python3
import mt_thresholds

mt_thresholds.accuracy(1.0, "bleu") # 0.63989
mt_thresholds.delta(0.63989, "chrf") # 0.665
```