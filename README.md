# Quadratic Equation Solver

Console application for solving quadratic equations of the form ax² + bx + c = 0.

## Description

This application allows solving quadratic equations in two modes:
- **Interactive mode**: user enters coefficients through console
- **File mode**: coefficients are read from a file

The application calculates the discriminant and finds from 0 to 2 real roots of the equation.

## Build and Run

### Requirements
- Python 3.6 or newer
- Unix-like system (Linux, macOS) or Windows with bash

### Installation
1. Clone the repository:
```bash
git clone https://github.com/tvirna/mtsd-lab1
cd mtsd-lab1
```

2. Make the script executable:
```bash
chmod +x equation
```

### Usage

#### Interactive Mode
```bash
./equation
```

Usage example:
```
$ ./equation
a = 2
b = 1
c = -3
Equation is: (2.0) x^2 + (1.0) x + (-3.0) = 0
There are 2 roots
x1 = -1.5
x2 = 1.0
```

#### File Mode
```bash
./equation <file_path>
```

Example:
```bash
./equation test_data.txt
```

## File Format for Non-Interactive Mode

The file should contain three real numbers (coefficients a, b, c) separated by a single space, ending with a newline character:

```
a b c\n
```

File example:
```
1.0 0.0 -4.0
```

**Important:**
- Use dot (.) as decimal separator
- Coefficient `a` cannot equal 0
- File must end with a newline character
- File must contain exactly three numbers

## Project Structure

```
mtsd-lab1/
├── src/
│   ├── equation_solver.py      # Equation solving logic
│   ├── input_handler.py        # User input handling
│   ├── file_handler.py         # File operations
│   └── main.py                 # Main module
├── requirements.pdf            # Project requirements
├── equation                    # Executable script
└── README.md                   # Documentation
```

## Revert Commit

The repository history contains a revert commit with hash: `[COMMIT_HASH]`

This commit reverts changes that were introduced in commit `[REVERTED_COMMIT_HASH]`, where input validation was incorrectly implemented.

## Usage Examples

### Equation with Two Roots
```bash
$ ./equation
a = 1
b = 0
c = -4
Equation is: (1.0) x^2 + (0.0) x + (-4.0) = 0
There are 2 roots
x1 = -2.0
x2 = 2.0
```

### Equation with One Root
```bash
$ ./equation
a = 1
b = -2
c = 1
Equation is: (1.0) x^2 + (-2.0) x + (1.0) = 0
There are 1 roots
x1 = 1.0
```

### Equation with No Real Roots
```bash
$ ./equation
a = 1
b = 0
c = 1
Equation is: (1.0) x^2 + (0.0) x + (1.0) = 0
There are 0 roots
```

## Error Handling

The application correctly handles the following situations:
- Invalid numeric input
- Coefficient `a` = 0
- Non-existent files
- Incorrect file format
- User program interruption (Ctrl+C)

## License

This project was created for educational purposes.