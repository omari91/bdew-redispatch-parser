# Contributing to BDEW Redispatch Parser

Thank you for considering contributing to BDEW Redispatch Parser! This document provides guidelines for contributing to the project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and collaborative environment for all contributors.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- A clear and descriptive title
- Detailed steps to reproduce the issue
- Expected behavior vs. actual behavior
- Your environment (Python version, OS, etc.)
- Sample XML data if relevant (please anonymize sensitive data)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- A clear and descriptive title
- A detailed description of the proposed enhancement
- Examples of how the enhancement would be used
- Any relevant examples from other projects

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the code style guidelines
3. **Add tests** for any new functionality
4. **Update documentation** if you're changing functionality
5. **Ensure tests pass** by running the test suite
6. **Write a clear commit message** describing your changes
7. **Submit a pull request** with a comprehensive description

## Development Setup

1. Clone your fork of the repository:
```bash
git clone https://github.com/YOUR_USERNAME/bdew-redispatch-parser.git
cd bdew-redispatch-parser
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Run tests to verify your setup:
```bash
python -m pytest tests/
```

## Code Style Guidelines

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Write clear comments for complex logic

## Testing Guidelines

- Write unit tests for new functionality
- Ensure all tests pass before submitting PR
- Aim for good test coverage
- Use descriptive test names
- Include both positive and negative test cases

## Commit Message Guidelines

Write clear and meaningful commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests when relevant

Example:
```
Add validation for Redispatch 3.0 schema

- Implement strict XSD validation
- Add error messages for common validation failures
- Update tests to cover new validation logic

Fixes #123
```

## Questions?

If you have questions about contributing, feel free to open an issue for discussion.

Thank you for your contributions!
