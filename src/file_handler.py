"""
Module for file operations in non-interactive mode
"""
import os
from typing import Tuple


class FileHandler:
    """Class for file operations"""
    
    @staticmethod
    def read_coefficients_from_file(filename: str) -> Tuple[float, float, float]:
        """
        Read coefficients from file
        
        Args:
            filename: path to file
            
        Returns:
            Tuple[float, float, float]: coefficients a, b, c
            
        Raises:
            FileNotFoundError: if file doesn't exist
            ValueError: if file format is incorrect or a = 0
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"file {filename} does not exist")
        
        try:
            with open(filename, 'r') as file:
                content = file.read().strip()
                
            # Check that file contains exactly three numbers separated by spaces
            parts = content.split()
            if len(parts) != 3:
                raise ValueError("invalid file format")
            
            a, b, c = map(float, parts)
            
            if a == 0:
                raise ValueError("Error. a cannot be 0")
                
            return a, b, c
            
        except (ValueError, IOError) as e:
            if "could not convert" in str(e) or "invalid literal" in str(e):
                raise ValueError("invalid file format")
            raise