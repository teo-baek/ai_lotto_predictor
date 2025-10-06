def calculate_frequency(predictions):
    freq = {i: 0 for i in range(1, 46)}
    for pred in predictions:
        for n in pred["numbers"]:
            freq[n] += 1
    return freq
