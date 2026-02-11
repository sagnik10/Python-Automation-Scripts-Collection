# Python-Automation-and-Core-Concepts-Practice

Comprehensive Python practice repository covering Selenium automation testing, OOP principles, generators, iterators, exception handling, file processing, and functional programming concepts.

---

## Overview

This repository contains structured Python practice scripts combining:

- Selenium-based web automation testing
- Pytest test configuration
- Object-Oriented Programming (OOP)
- Generators and iterators
- Exception handling
- File handling
- Functional programming concepts

The project demonstrates both practical automation skills and strong Python fundamentals.

---

## Project Structure

```
Python-Automation-and-Core-Concepts-Practice/

├── CartAutomation.py
├── conftest.py
├── Private#&ProtectedValidation.py
├── LargeFileReading.py
├── ReduceForProductOfList.py
├── FinallyWithFileHandling.py
├── MultipleExceptionUsingOneTryBlock.py
├── ConvertedGenerator.py
├── FibonacciGenerator.py
├── CustomIteratorClass.py
└── README.md
```

---

## 1. Selenium Automation Testing

### CartAutomation.py
Implements end-to-end automation testing for:

- User registration
- Login
- Product selection
- Cart validation
- Checkout process

Uses:
- Selenium WebDriver
- Explicit waits
- Pytest framework
- Dynamic test data generation

### conftest.py
Provides:

- Pytest fixture for WebDriver setup
- Browser selection via command line
- Session-level driver management

Run tests:

```bash
pytest --browser=chrome
```

---

## 2. Object-Oriented Programming

### Private#&ProtectedValidation.py

Demonstrates:

- Protected variables
- Private variables
- Encapsulation
- Property decorators
- Getter and setter validation
- AttributeError handling

---

## 3. File Handling & Resource Management

### FinallyWithFileHandling.py

Demonstrates:

- Using try/finally to safely close files
- Proper file resource management

### LargeFileReading.py

Demonstrates:

- Generator-based file reading
- Memory-efficient large file processing

---

## 4. Exception Handling

### MultipleExceptionUsingOneTryBlock.py

Demonstrates:

- Handling multiple exceptions in one block
- ValueError
- ZeroDivisionError

---

## 5. Functional Programming

### ReduceForProductOfList.py

Demonstrates:

- functools.reduce
- Lambda functions
- Product calculation

---

## 6. Generators

### ConvertedGenerator.py

Demonstrates:

- Yield-based generator
- On-demand computation

### FibonacciGenerator.py

Implements:

- Fibonacci sequence using generator

---

## 7. Custom Iterator

### CustomIteratorClass.py

Implements:

- Custom iterator class
- __iter__ method
- __next__ method
- StopIteration handling

---

## Technologies Used

- Python
- Selenium
- Pytest
- Functional Programming Concepts
- OOP Principles

---

## How to Run

Install dependencies:

```bash
pip install selenium pytest
```

Run automation tests:

```bash
pytest --browser=chrome
```

Run individual concept scripts:

```bash
python LargeFileReading.py
python FibonacciGenerator.py
```

---

## Learning Areas Covered

- Automation Testing
- Web Interaction using Selenium
- Python OOP
- Encapsulation
- Generators & Iterators
- Exception Handling
- File Processing
- Functional Programming

---

## Purpose

This repository serves as:

- Python fundamentals practice
- Automation testing portfolio demonstration
- Interview preparation resource
- Structured coding concept reference

---

## License

This repository is intended for educational and practice purposes.
