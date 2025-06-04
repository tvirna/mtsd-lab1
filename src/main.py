#!/usr/bin/env python3
"""
Console application for solving quadratic equations
"""
import sys
from equation_solver import QuadraticEquation
from input_handler import InputHandler
from file_handler import FileHandler


def format_output_interactive(equation: QuadraticEquation) -> None:
    """
    Format and output results in interactive mode
    
    Args:
        equation: quadratic equation object
    """
    print(f"Equation is: {equation}")
    
    roots = equation.solve()
    roots_count = len(roots)
    
    if roots_count == 0:
        print("There are 0 roots")
    elif roots_count == 1:
        print("There are 1 roots")
        print(f"x1 = {roots[0]}")
    else:
        print("There are 2 roots")
        print(f"x1 = {roots[0]}")
        print(f"x2 = {roots[1]}")


def format_output_file(equation: QuadraticEquation) -> None:
    """
    Format and output results in file mode
    
    Args:
        equation: quadratic equation object
    """
    print(f"Equation is: {equation}")
    
    roots = equation.solve()
    roots_count = len(roots)
    
    if roots_count == 0:
        print("There are 0 roots")
    elif roots_count == 1:
        print(f"There are 1 roots x1 = {roots[0]}")
    else:
        print(f"There are 2 roots")
        print(f"x1 = {roots[0]}")
        print(f"x2 = {roots[1]}")


def main():
    """Main program function"""
    if len(sys.argv) == 1:
        # Interactive mode
        try:
            a, b, c = InputHandler.get_coefficients_interactive()
            equation = QuadraticEquation(a, b, c)
            format_output_interactive(equation)
        except KeyboardInterrupt:
            print("\nProgram interrupted by user")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    elif len(sys.argv) == 2:
        # File mode
        filename = sys.argv[1]
        try:
            a, b, c = FileHandler.read_coefficients_from_file(filename)
            equation = QuadraticEquation(a, b, c)
            format_output_file(equation)
        except FileNotFoundError as e:
            print(str(e))
            sys.exit(1)
        except ValueError as e:
            print(str(e))
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)
    
    else:
        print("Usage: ./equation [file]")
        print("  No arguments: interactive mode")
        print("  One argument: file mode")
        sys.exit(1)


if __name__ == "__main__":
    main()