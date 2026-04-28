# climate-challenge-week0

# 🌍 African Climate Trend Analysis – Week 0

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/Status-Completed-green)
![EDA](https://img.shields.io/badge/Focus-Exploratory%20Data%20Analysis-orange)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-black)

---

## Project Overview

This project analyzes historical climate data (2015–2026) across five African countries:

**Ethiopia, Kenya, Sudan, Tanzania, and Nigeria**

It is part of a data-driven initiative to explore climate variability, detect trends, and identify regional vulnerabilities to support climate discussions ahead of **COP32 in Ethiopia (2027)**.

The analysis focuses on:
- Temperature trends
- Precipitation patterns
- Climate variability and anomalies
- Cross-country comparison

---

## Context

This work is conducted in the context of **EthioClimate Analytics**, supporting the **Ethiopian Ministry of Planning and Development**.

Role: **Junior Data Analyst**

The goal is to transform raw climate data into actionable insights that can support climate policy and negotiation strategies.

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/wossenF/climate-challenge-week0.git
cd climate-challenge-week0

### Create virtual environment
python -m venv venv

### Activate environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Run project
python --version

Run Analysis

Launch Jupyter Notebook: jupyter notebook

Open: notebooks/<country>_eda.ipynb 

📂 Project Structure

src/            → source code and utilities  
notebooks/      → EDA notebooks (country-wise analysis)  
scripts/        → helper scripts  
data/           → raw datasets (excluded from GitHub)  
.github/        → CI/CD workflows  

## Data Processing Summary

The dataset (NASA POWER, 2015–2026) was cleaned and prepared using the following steps:

Replaced sentinel values (-999) with NaN
Removed duplicate records
Converted YEAR and DOY into datetime format
Extracted monthly features for seasonal analysis
Handled missing values using forward-fill and filtering
Detected outliers using Z-score method

## CI/CD Pipeline

A GitHub Actions workflow is implemented to ensure reproducibility.

It automatically:

Installs dependencies
Verifies Python environment
Runs on every push to main

## Key Insight Direction

This project aims to support climate negotiation readiness by answering:

What is changing in the climate?
What impact does it suggest?
What policy action does it require?

## Data Note
Dataset covers 2015–2026
Raw data is excluded from this repository
NASA POWER climate variables used (temperature, rainfall, humidity, wind)

