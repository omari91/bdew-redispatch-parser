\# BDEW Redispatch Data Parser



\## Overview

A Python-based tool designed to validate and parse XML data formats used in the German energy market (specifically Redispatch 2.0/3.0 processes). It ensures data compliance with XSD schemas and transforms hierarchical XML into flat Pandas DataFrames for analysis.



\## Features

\* \*\*Schema Validation:\*\* Strict XSD validation using `lxml` to ensure BDEW compliance.

\* \*\*Data Parsing:\*\* Extracts key metrics (Available Capacity MW, Time Intervals, Resource IDs).

\* \*\*Analysis Ready:\*\* Exports data to Pandas for time-series analysis.



\## Project Structure

\* `src/`: Core parser logic.

\* `data/`: Sample BDEW XML and XSD files.

\* `tests/`: Unit tests to ensure reliability.



\## Tech Stack

\* Python 3.10+

\* Pandas

\* LXML

