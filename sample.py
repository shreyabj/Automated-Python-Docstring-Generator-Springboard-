"""Utility module for data processing and simple prediction workflows."""

import random


def generate_random_numbers(n):
    """Generate a list of random integers.

    Args:
        n (int): Number of random values to generate.

    Returns:
        list[int]: List of randomly generated integers.
    """
    return [random.randint(1, 100) for _ in range(n)]


def calculate_average(numbers):
    """Calculate the average of a list of numbers.

    Args:
        numbers (list[int]): Input list of integers.

    Returns:
        float: Average value.
    """
    return sum(numbers) / len(numbers) if numbers else 0.0


def find_maximum(numbers):
    """Return the maximum value from a list.

    Args:
        numbers (list[int]): Input list of integers.

    Returns:
        int: Maximum value.
    """
    return max(numbers)


class DataProcessor:
    """Perform basic data processing on numeric data."""

    def __init__(self, data):
        """Initialize the DataProcessor.

        Args:
            data (list[int]): Input numeric data.
        """
        self.data = data

    def normalize(self):
        """Normalize values between 0 and 1.

        Returns:
            list[float]: Normalized values.
        """
        max_val = max(self.data)
        return [x / max_val for x in self.data]

    def square_values(self):
        """Square each value in the dataset.

        Returns:
            list[int]: Squared values.
        """
        return [x ** 2 for x in self.data]


class SimpleModel:
    """Threshold-based prediction model."""

    def __init__(self, threshold):
        """Initialize the model.

        Args:
            threshold (float): Threshold value.
        """
        self.threshold = threshold

    def predict(self, value):
        """Predict whether value exceeds the threshold.

        Args:
            value (float): Input value.

        Returns:
            bool: Prediction result.
        """
        return value > self.threshold

    def batch_predict(self, values):
        """Predict results for multiple values.

        Args:
            values (list[float]): Input values.

        Returns:
            list[bool]: Prediction results.
        """
        return [self.predict(v) for v in values]


def run_pipeline(size):
    """Run the complete processing and prediction pipeline.

    Args:
        size (int): Number of random values to generate.

    Returns:
        dict: Pipeline results.
    """
    numbers = generate_random_numbers(size)
    avg = calculate_average(numbers)

    processor = DataProcessor(numbers)
    normalized = processor.normalize()

    model = SimpleModel(avg)

    return {
        "average": avg,
        "max": find_maximum(numbers),
        "predictions": model.batch_predict(normalized),
    }
