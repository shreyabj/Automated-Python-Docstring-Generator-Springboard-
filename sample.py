import random

# test change for milestone 3


def generate_scores(count):
    if count <= 0:
        raise ValueError("Count must be positive")

    scores = []
    for _ in range(count):
        scores.append(random.randint(0, 100))
    return scores


def calculate_mean(values):
    if not values:
        return 0
    return sum(values) / len(values)


def check_pass(score, threshold):
    return score >= threshold


def score_stream(limit):
    for i in range(limit):
        yield i * 10


class ScoreAnalyzer:

    def __init__(self, scores):
        self.scores = scores
        self.total = sum(scores)

    def normalize_scores(self):
        max_score = max(self.scores)
        return [s / max_score for s in self.scores]

    def highest_score(self):
        return max(self.scores)


def run_analysis(size, pass_mark):
    scores = generate_scores(size)
    mean = calculate_mean(scores)

    analyzer = ScoreAnalyzer(scores)
    normalized = analyzer.normalize_scores()

    results = []
    for s in normalized:
        results.append(check_pass(s * 100, pass_mark))

    return {
        "mean": mean,
        "passed": results,
        "highest": analyzer.highest_score()
    }
