# Calculator Project

A simple calculator implementation in Python with both command-line and graphical interfaces, plus three different testing approaches.

## Project Structure

```
.
├── calculator.py                  # Main calculator implementation
├── test_calculator.py            # Basic assertion-based tests
├── test_calculator_unittest.py    # Unittest-based tests
├── test_calculator_pytest.py      # Pytest-based tests
├── requirements.txt              # Project dependencies
└── .github
    └── workflows
        └── test-ci.yml          # GitHub Actions workflow
```

## Setup

### Virtual Environment Setup

1. **Create a Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Pytest (if not using requirements.txt)**
   ```bash
   pip install pytest pytest-cov
   ```

### Deactivating Virtual Environment
When you're done working on the project:
```bash
deactivate
```

## Usage

### Command Line Interface
```python
from calculator import Calculator

calc = Calculator()

# Basic operations
result1 = calc.add(5, 3)        # Returns 8
result2 = calc.subtract(5, 3)   # Returns 2
result3 = calc.multiply(5, 3)   # Returns 15
result4 = calc.divide(6, 2)     # Returns 3

# Advanced operations
result5 = calc.modulo(7, 3)     # Returns 1
result6 = calc.power(2, 3)      # Returns 8
result7 = calc.square_root(9)   # Returns 3.0
```

### Graphical User Interface
Run the calculator GUI:
```bash
python calculator_gui.py
```

The GUI calculator features:
- Graphical User Interface
- Numeric keypad (0-9)
- Basic operations (+, -, *, /)
- Advanced operations (√, ^)
- Control buttons (C, ←, =)


## Testing Approaches

### 1. Basic Assertion Tests (`test_calculator.py`)
- Uses Python's built-in assert statements
- Simple and straightforward
- Good for learning basics

Run with:
```bash
# From project root directory
python test_calculator.py
```

### 2. Unittest Framework (`test_calculator_unittest.py`)
- Uses Python's built-in unittest framework
- Class-based approach
- Detailed test organization

Run with:
```bash
# Regular mode
python -m unittest test_calculator_unittest.py

# Verbose mode
python -m unittest test_calculator_unittest.py -v
```

### 3. Pytest Framework (`test_calculator_pytest.py`)
- Modern testing approach
- More features and cleaner syntax
- Supports fixtures and parameterized testing

Run with:
```bash
# Run all pytest tests
pytest

# Verbose mode
pytest -v

# With print statements
pytest -v -s

# With coverage reportven  
pytest --cov=calculator
```

Note: The `conftest.py` in the tests directory automatically handles Python path configuration for pytest. You don't need to set PYTHONPATH when using pytest.

## Features

The Calculator class provides:
- Addition (`add`)
- Subtraction (`subtract`)
- Multiplication (`multiply`)
- Division (`divide`)
- Modulo (`modulo`)
- Power (`power`)
- Square Root (`square_root`)

## Test Coverage

All three test suites cover:
- Basic arithmetic operations
- Edge cases:
  - Division by zero
  - Negative numbers
  - Zero values
- Complex operations:
  - Power calculations
  - Square root with precision
  - Modulo operations

## Comparison of Testing Approaches

1. **Basic Assertions** (`test_calculator.py`)
   - Pros: Simple, easy to understand
   - Cons: Limited features, basic error reporting

2. **Unittest** (`test_calculator_unittest.py`)
   - Pros: Built-in, good organization
   - Cons: More verbose, less modern features

3. **Pytest** (`test_calculator_pytest.py`)
   - Pros: Modern features, clean syntax, powerful fixtures
   - Cons: Additional dependency, learning curve
