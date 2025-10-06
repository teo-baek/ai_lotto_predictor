import numpy as np
import random


def generate_predictions(num_sets: int = 5):
    results = []
    for _ in range(num_sets):
        numbers = sorted(random.sample(range(1, 46), 6))
        confidence = round(random.uniform(90.0, 99.9), 1)
        results.append({"numbers": numbers, "confidence": confidence})
    return results
