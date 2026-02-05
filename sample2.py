import math
import random


# ---------------------------
# Utility Functions
# ---------------------------

def generate_random_numbers(n):
    numbers = []
    for _ in range(n):
        numbers.append(random.randint(1, 100))
    return numbers


def calculate_average(numbers):
  
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def find_maximum(numbers):
    return max(numbers)


# ---------------------------
# Data Processing Class
# ---------------------------

class DataProcessor:
  

    def __init__(self, data):
        self.data = data

    def normalize(self):
        max_val = max(self.data)
        return [x / max_val for x in self.data]

    def square_values(self):
      
        return [x ** 2 for x in self.data]


# ---------------------------
# Model Logic Class
# ---------------------------

class SimpleModel:

    def __init__(self, threshold):
        self.threshold = threshold

    def predict(self, value):
        
        return value > self.threshold

    def batch_predict(self, values):
        results = []
        for v in values:
            results.append(self.predict(v))
        return results


# ---------------------------
# Main Workflow Function
# ---------------------------

def run_pipeline(size):
    numbers = generate_random_numbers(size)
    avg = calculate_average(numbers)
    maximum = find_maximum(numbers)

    processor = DataProcessor(numbers)
    normalized = processor.normalize()

    model = SimpleModel(avg)
    predictions = model.batch_predict(normalized)

    return {
        "average": avg,
        "max": maximum,
        "predictions": predictions
    }
