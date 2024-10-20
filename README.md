# -Airline-Data-Analysis-Trends-in-Flight-Performance-and-Passenger-Insights

## Overview

This project analyzes an airline dataset to explore passenger demographics, flight statuses, and seasonal trends. The goal is to identify patterns such as gender and nationality distribution, busy flight days/months, and the prevalence of flight delays or cancellations. The analysis is performed using Python libraries like `pandas`, `numpy`, `matplotlib`, and `seaborn`, and visualized through various charts.

## Dataset

The dataset is **`Airline Dataset Updated - v2.csv`**, which contains the following key columns:
- `Age`: Passenger's age.
- `Gender`: Passenger's gender.
- `Nationality`: Passenger's country of origin.
- `Departure Date`: Date of flight departure.
- `Flight Status`: Status of the flight (On-time, Delayed, or Canceled).
- `Airport Name`: Name of the departure airport.

## Key Features of the Project

### 1. Data Loading and Initial Exploration
- The dataset is loaded into a pandas DataFrame using `pd.read_csv()`.
- Functions like `data.head()`, `data.info()`, and `data.describe()` are used to understand the structure and summary of the data.
- Missing values are checked using `data.isna().sum()`.

### 2. Data Preprocessing
- **Column Renaming**: All column names are converted to lowercase and spaces are replaced with underscores.
- **Date Formatting**: The `departure_date` column is cleaned and converted into a `datetime` format.
- **Age Grouping**: A new column `age_group` is created to categorize passengers as Child, Teen, Adult, or Elder based on their age.

### 3. Feature Engineering
- **Extracting Day and Month**: Departure day (`departure_day`) and month (`departure_month`) are extracted from `departure_date` for analysis of seasonal trends.
  
### 4. Data Visualization
- **Pie Charts**: Gender distribution of passengers is shown via a pie chart.
- **Bar Charts**: 
  - Flight status distribution (On-time, Delayed, Canceled).
  - Age group and flight status comparisons.
  - Gender and nationality distributions.
  - Top 10 airports based on passenger counts.
- **Line Plots**: Flight status trends over time (on-time, delayed, canceled) using monthly resampling.

### 5. Custom Helper Functions
- **`plot_groupbar()`**: Generates grouped bar charts for two columns (e.g., nationality vs gender, age group vs flight status).
- **`plot_bar()`**: Generates a bar chart to show the count of categories in a column.

### 6. Insights and Trends
- **Busiest Days and Months**: Identify the busiest departure days and months using bar charts.
- **Nationality and Gender**: Explore the gender distribution across the top 10 nationalities.
- **Flight Status Trends**: Analyze flight status changes over time and explore if specific days or months experience more delays or cancellations.

## Key Findings

1. **Gender Distribution**: The majority of passengers are male.
2. **Age Group Analysis**: Adults (aged 19-45) are the largest group of passengers.
3. **Flight Status**: The majority of flights are either on-time or delayed, with fewer cancellations.
4. **Seasonal Trends**: Certain days of the week and months have a higher flight frequency, with delays peaking during specific periods.

## Requirements

You will need the following Python libraries to run the project:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

Install them via `pip`:
```bash
pip install pandas numpy matplotlib seaborn

