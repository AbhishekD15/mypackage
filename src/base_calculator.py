class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"Added {a} to {b} got {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"Subtracted {b} from {a} got {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"Multiplied {a} with {b} got {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.history.append(f"Divided {a} by {b} got {result}")
        return result

    def show_history(self):
        for entry in self.history:
            print(entry)
