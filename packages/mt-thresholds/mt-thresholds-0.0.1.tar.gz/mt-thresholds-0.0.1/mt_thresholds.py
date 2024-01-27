import json
import math
import argparse

_thresholds = {
    k.lower(): v
    for k, v in json.load(open("thresholds.json", "r")).items()
}
METRICS = set(_thresholds.keys())

def check_metric_ok(metric):
    if metric not in METRICS:
        raise Exception(
            f"Invalid metric {metric}, please use any of the following: " + str(METRICS))

def cmd_entry():
    args = argparse.ArgumentParser(
        description="Example usage: mt-thresholds accuracy bleu 0.6")
    args.add_argument("metric", type=str)
    args.add_argument("value", type=float,
                      help="Accuracy is on scale from 0 to 1.")
    args.add_argument("--delta", action="store_true",
                      help="Given accuracy show deltas of another metric.")
    args = args.parse_args()
    args.metric = args.metric.lower()

    check_metric_ok(args.metric)

    if args.delta:
        print(f"{delta(args.value, args.metric):.3f}")
    else:
        print(f"{accuracy(args.value, args.metric):.3f}")


def accuracy(delta: float, metric: str) -> float:
    check_metric_ok(metric)

    a, b = _thresholds[metric]
    return a * (1 / (1 + math.pow(math.e, -b * delta)))


def delta(accuracy: float, metric: str) -> float:
    check_metric_ok(metric)
    
    a, b = _thresholds[metric]
    try:
        return -math.log(a / (accuracy * 100) - 1) / b
    except:
        return math.nan
