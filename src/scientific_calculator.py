import math
from .base_calculator import Calculator
class ScientificCalculator(Calculator):
    def power(self, a, b):
        result = math.pow(a, b)
        self.history.append(f"{a} raised to the power of {b} is {result}")
        return result

    def sine(self, angle):
        result = math.sin(math.radians(angle))
        self.history.append(f"Sine of {angle} degrees is {result}")
        return result

    def cosine(self, angle):
        result = math.cos(math.radians(angle))
        self.history.append(f"Cosine of {angle} degrees is {result}")
        return result
