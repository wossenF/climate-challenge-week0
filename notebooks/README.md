# Climate Challenge – Week 0  
## Exploratory Data Analysis – Ethiopia

---

## Overview
This notebook presents the exploratory data analysis (EDA) for **Tanzania** using historical climate data (2015–2026).

The objective is to identify key climate patterns, trends, and anomalies to support data-driven insights for climate analysis.

---

## Dataset
The dataset includes daily climate observations with variables such as:

- Temperature (T2M, T2M_MAX, T2M_MIN)
- Precipitation (PRECTOTCORR)
- Humidity (RH2M)
- Wind Speed (WS2M)

⚠️ Note: The dataset is not included in this repository.  
Place the CSV file inside the `data/` folder before running the notebook.

---

## Data Cleaning
The following preprocessing steps were applied:

- Replaced sentinel values (`-999`) with `NaN`
- Removed duplicate rows
- Converted `YEAR` and `DOY` into datetime format
- Extracted `Month` for seasonal analysis
- Handled missing values using forward-fill
- Identified outliers using Z-score method

---

## Key Analysis

### 🌡 Temperature Trends
Analyzed monthly average temperature to observe seasonal patterns and long-term trends.

### 🌧 Precipitation Patterns
Explored rainfall distribution and identified wet and dry periods.

### 🔗 Correlation Analysis
Examined relationships between climate variables using correlation heatmaps.

### 📊 Distribution Analysis
Studied the distribution of precipitation and other variables to understand variability.

---

## Key Insights
- Temperature shows noticeable seasonal variation with signs of gradual change over time  
- Rainfall patterns indicate variability between wet and dry periods  
- Some extreme values suggest possible climate anomalies  

---

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook