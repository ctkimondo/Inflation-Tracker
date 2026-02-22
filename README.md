# Global Inflation Refinery & Analytics
An automated, containerized ETL pipeline and analytical engine for global economic data.

# Project Overview
This project transforms raw, nested economic data from the OECD API into a production-ready data refinery. It moves beyond simple analysis by implementing a robust ETL (Extract, Transform, Load) architecture, ensuring that global inflation insights are automated, standardized, and scalable.

# Data Engineering Architecture
This system is built using a Modular Design to separate concerns and ensure reliability:
- Extraction (src/extract.py): Programmatically fetches 1.6M+ records from the OECD SDMX-JSON API with custom timeout handling.
- Transformation (src/transform.py): Decodes complex composite keys and flattens nested JSON structures into a clean, analytical format.
- Loading (src/load.py): Persists data into Apache Parquet format, utilizing columnar storage to optimize for speed and disk space (80% more efficient than CSV).
- Automation: Integrated with GitHub Actions (CI/CD) to trigger a full refinery run every Monday at 8:00 AM UTC via Cron scheduling.
- Containerization: Fully packaged with Docker to ensure 100% reproducibility across any cloud environment.
- ecouples storage from compute by streaming transformed Parquet files to an S3 bucket.
# Analytical Insights
While the refinery moves the data, the analysis identifies economic risk:
- High-Risk Zones: Identifies countries like Argentina and Turkey as outliers with both high inflation and high volatility.
- Stability Zones: Highlights the Euro Area and Canada as ideal environments for long-term investment.
- Volatility Tracking: Uses Standard Deviation metrics to rank countries by economic predictability.

# Getting Started
## Prerequisites
- Docker
- Python 3.11+
- Running with Docker 

## Running With Docker
docker build -t inflation-refinery .

docker run inflation-refinery

## Manual Installation
pip install -r requirements.txt

python src/main.py

# Tech Stack
Language: Python 3.11

Libraries: Pandas, PyArrow (Parquet Engine), Requests, Seaborn, Matplotlib

DevOps: Docker, GitHub Actions, YAML

Format: Apache Parquet (Columnar Storage)

