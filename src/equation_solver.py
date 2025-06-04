"""
Module for solving quadratic equations of the form ax² + bx + c = 0
"""
import math
from typing import List, Tuple


class QuadraticEquation:
    """Class for representing and solving quadratic equations"""
    
    def __init__(self, a: float, b: float, c: float):
        """
        Initialize quadratic equation
        
        Args:
            a: coefficient for x²
            b: coefficient for x
            c: constant term
            
        Raises:
            ValueError: if a = 0
        """
        if a == 0:
            raise ValueError("a cannot be 0")
        
        self.a = a
        self.b = b
        self.c = c
    
    def get_discriminant(self) -> float:
        """Calculate equation discriminant"""
        return self.b ** 2 - 4 * self.a * self.c
    
    def solve(self) -> List[float]:
        """
        Solve quadratic equation
        
        Returns:
            List of equation roots (can be empty, contain 1 or 2 roots)
        """
        discriminant = self.get_discriminant()
        
        if discriminant < 0:
            return []
        elif discriminant == 0:
            root = -self.b / (2 * self.a)
            return [root]
        else:
            sqrt_discriminant = math.sqrt(discriminant)
            root1 = (-self.b + sqrt_discriminant) / (2 * self.a)
            root2 = (-self.b - sqrt_discriminant) / (2 * self.a)
            return sorted([root1, root2])
    
    def get_roots_count(self) -> int:
        """Return number of real roots"""
        discriminant = self.get_discriminant()
        if discriminant < 0:
            return 0
        elif discriminant == 0:
            return 1
        else:
            return 2
    
    def __str__(self) -> str:
        """Return string representation of equation"""
        return f"({self.a}) x^2 + ({self.b}) x + ({self.c}) = 0"