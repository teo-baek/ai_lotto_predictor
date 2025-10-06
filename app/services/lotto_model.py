import numpy as np
from random import sample


def generate_predictions(n_sets=5):
    """
    단순 무작위 기반 예측 (향후 ML 모델로 교체 예정)
    """
    predictions = []
    for _ in range(n_sets):
        numbers = sorted(sample(range(1, 46), 6))
        confidence = round(np.random.uniform(0.9, 0.99), 3)
        predictions.append({"numbers": numbers, "confidence": confidence})
    return predictions
