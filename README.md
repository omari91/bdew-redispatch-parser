# BDEW Redispatch Parser

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A Python tool for validating and parsing BDEW Redispatch 3.0 XML data for German grid congestion management. Features strict XSD schema validation and Pandas integration for efficient data analysis.

## Overview

This parser is designed to work with XML data formats used in German energy market Redispatch processes (versions 2.0/3.0). It ensures data compliance with BDEW (Bundesverband der Energie- und Wasserwirtschaft) XSD schemas and transforms hierarchical XML structures into flat, analysis-ready Pandas DataFrames.

**Key Use Cases:**
- Grid congestion management data processing
- Redispatch capacity validation and analysis
- Time-series energy market data extraction
- BDEW compliance verification

## Features

### ✅ Strict Schema Validation
- XSD schema validation using `lxml`
- Ensures BDEW Redispatch 3.0 compliance
- Detailed error reporting for non-compliant data

### 📊 Data Parsing & Extraction
- Extracts key metrics:
  - Available Capacity (MW)
  - Time Intervals
  - Resource IDs
  - Market participant information
- Handles hierarchical XML structures
- Preserves data integrity during transformation

### 🔄 Analysis-Ready Output
- Direct export to Pandas DataFrames
- Optimized for time-series analysis
- Clean, flat data structure
- Easy integration with data science workflows

## Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Install Dependencies

```bash
# Clone the repository
git clone https://github.com/omari91/bdew-redispatch-parser.git
cd bdew-redispatch-parser

# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from src.parser import RedispatchParser

# Initialize parser with XSD schema
parser = RedispatchParser('data/schema.xsd')

# Validate and parse XML file
result = parser.parse('data/sample_redispatch.xml')

# Access parsed data as Pandas DataFrame
df = result.to_dataframe()
print(df.head())
```

### Validation Only

```python
from src.validator import SchemaValidator

# Validate XML against XSD schema
validator = SchemaValidator('data/schema.xsd')
is_valid, errors = validator.validate('data/sample_redispatch.xml')

if is_valid:
    print("XML is valid!")
else:
    print(f"Validation errors: {errors}")
```

### Advanced Usage

```python
import pandas as pd
from src.parser import RedispatchParser

# Parse multiple files
parser = RedispatchParser('data/schema.xsd')
files = ['file1.xml', 'file2.xml', 'file3.xml']

dataframes = []
for file in files:
    result = parser.parse(file)
    dataframes.append(result.to_dataframe())

# Combine all data
combined_df = pd.concat(dataframes, ignore_index=True)

# Analyze time-series data
combined_df['timestamp'] = pd.to_datetime(combined_df['timestamp'])
combined_df.set_index('timestamp', inplace=True)

# Calculate statistics
print(combined_df.groupby('resource_id')['capacity_mw'].describe())
```

## Project Structure

```
bdew-redispatch-parser/
├── src/
│   ├── __init__.py
│   ├── parser.py          # Main parser logic
│   ├── validator.py       # XSD validation
│   └── utils.py          # Helper functions
├── data/
│   ├── schema.xsd        # BDEW XSD schema
│   └── sample_*.xml      # Sample XML files
├── tests/
│   ├── test_parser.py
│   ├── test_validator.py
│   └── fixtures/         # Test data
├── requirements.txt
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

## Tech Stack

- **Python 3.10+**: Core language
- **lxml**: XML parsing and XSD validation
- **Pandas**: Data manipulation and analysis
- **pytest**: Unit testing framework

## Testing

Run the test suite to ensure everything works correctly:

```bash
# Run all tests
python -m pytest tests/

# Run with coverage report
python -m pytest tests/ --cov=src --cov-report=html

# Run specific test file
python -m pytest tests/test_parser.py -v
```

## Examples

Check the `examples/` directory for more detailed usage examples:

- `basic_parsing.py`: Simple XML parsing example
- `batch_processing.py`: Process multiple files
- `time_series_analysis.py`: Analyze capacity trends
- `validation_workflow.py`: Complete validation pipeline

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Reporting bugs
- Suggesting enhancements
- Submitting pull requests
- Code style and testing requirements

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- BDEW for the Redispatch data format specifications
- German energy market operators for use case requirements

## Contact

For questions or support, please open an issue on GitHub.

## Roadmap

- [ ] Support for Redispatch 4.0 specification
- [ ] REST API wrapper
- [ ] Command-line interface (CLI)
- [ ] Real-time data streaming support
- [ ] Enhanced visualization tools

---

**Note**: This tool is designed for data analysis and validation purposes. Always ensure compliance with relevant data protection and market regulations when handling real energy market data.
