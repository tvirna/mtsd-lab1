"""
Module for handling user input and data validation
"""
from typing import Tuple


class InputHandler:
    """Class for handling user input"""
    
    @staticmethod
    def get_float_input(prompt: str) -> float:
        """
        Ask user for a number with validation
        
        Args:
            prompt: prompt text
            
        Returns:
            float: entered number
        """
        while True:
            try:
                user_input = input(f"{prompt} = ").strip()
                return float(user_input)
            except ValueError:
                print(f"Error. Expected a valid real number, got {user_input} instead")
    
    @staticmethod
    def get_coefficients_interactive() -> Tuple[float, float, float]:
        """
        Get coefficients a, b, c in interactive mode
        
        Returns:
            Tuple[float, float, float]: coefficients a, b, c
        """
        while True:
            a = InputHandler.get_float_input("a")
            if a == 0:
                print("Error. a cannot be 0")
                continue
            break
        
        b = InputHandler.get_float_input("b")
        c = InputHandler.get_float_input("c")
        
        return a, b, c