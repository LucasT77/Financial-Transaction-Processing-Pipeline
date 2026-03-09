<a id="readme-top"></a>
# Financial Transaction Processing Pipeline

<!-- TABLE OF CONTENTS -->
<summary>Table of Contents</summary>
  <ol>
	<li><a href="#about-the-project">About The Project</a>
	<li><a href="#features">Features</a></li></li>
	<li><a href="#architecture">Architecture</a></li>
	<li><a href="#example-transaction-data">Example Transaction Data</a></li>
	<li><a href="#installation">Installation</a></li>
	<li><a href="#usage">Usage</a></li>
	<li><a href="#report-example">Generated Report Example</a></li>
	<li><a href="#technologies">Technologies</a></li>
	<li><a href="#future-improvements">Future Improvements</a></li>
	<li><a href="#license">License</a></li>
  </ol>

## About The Project
A modular Python backend application that ingests, validates, stores, analyzes and reports financial transaction data from CSV files.
The project demonstrates backend software engineering practices such as layered architecture, data validation, database persistence and analytical reporting.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features
- CSV transaction ingestion
- Data validation for timestamps, currencies, and monetary values
- Financial-grade numeric handling using Python Decimal
- SQLite database storage with uniqueness constraints
- Duplicate transaction conflict detection
- SQL-based analytics for financial metrics
- Automated report generation
- Command-line interface for pipeline orchestration
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Architecture
The project follows a layered architecture separating responsibilities across modules.

```
CSV Input
   │
   ▼
ingest.py        → CSV parsing
   │
   ▼
validate.py      → data validation
   │
   ▼
database.py      → persistence (SQLite)
   │
   ▼
analysis.py      → SQL analytics
   │
   ▼
report.py        → report generation
   │
   ▼
main.py          → CLI orchestration
```

This separation improves maintainability, testability, and extensibility.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Example Transaction Data
```transaction_id,timestamp,amount,currency
tx1001,2024-01-01T10:00:00,120.50,USD
tx1002,2024-01-01T12:30:00,75.00,EUR
tx1003,2024-01-02T09:15:00,200.00,USD
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation
git clone ?? 
cd ??

No external dependencies are required.
Python 3.9+ recommended.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage
Run the pipeline from the command line:
python main.py <data_path> [database_path] [report_path]

Example:
python3 main.py transactions.csv transactions.db report.txt

Parameters:
- data_path (required): CSV file containing transaction data
- database_path (optional): SQLite database file
- report_path (optional): Output reort file
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Generated Report Example

```
Transaction Report
=================
Total Transaction Volume by Currency
USD: 12000.50
EUR: 9800.20

Average Transaction Amount by Currency
USD: 340.50
EUR: 221.00

Transaction Count by Currency
USD: 35
EUR: 44

Largest Transaction by Currency
USD: 9800.00
EUR: 4300.00

Daily Transaction Volume
2024-01-01: 3200.50
2024-01-02: 4100.20
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Technologies
- Python
- SQL
- SQLite
- Command-Line Interface (CLI)
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Future Improvements~
Possible Future Improvements
- Structured logging
- Automated unit tests (pytest)
- Docker containerization
- CSV export for analytics results
- REST API interface
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License
MIT License
<p align="right">(<a href="#readme-top">back to top</a>)</p>

