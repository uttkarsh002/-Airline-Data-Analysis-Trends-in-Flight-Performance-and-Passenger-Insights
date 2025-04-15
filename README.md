# ✈️ Airline Data Analysis – Trends in Flight Performance and Passenger Insights

## 📊 Overview

This project analyzes an airline dataset to uncover key trends in passenger demographics, flight statuses, and seasonal travel behavior. The aim is to derive actionable insights such as the busiest travel periods, most frequent nationalities, gender distribution, and the pattern of flight delays or cancellations.

The analysis is powered by Python for data processing and visualization, followed by an ETL pipeline and a final dashboard in Tableau for interactive exploration.

---

## 📁 Dataset

**Filename:** `Airline Dataset Updated - v2.csv`

### Key Columns:

- `Age`: Passenger's age  
- `Gender`: Passenger's gender  
- `Nationality`: Passenger's country of origin  
- `Departure Date`: Date of flight departure  
- `Flight Status`: On-time, Delayed, or Canceled  
- `Airport Name`: Departure airport

---

## 🔁 ETL Process

### 1. **Extract**
- Loaded dataset using `pandas.read_csv()` from CSV.

### 2. **Transform**
- Cleaned column names to lowercase and replaced spaces with underscores.
- Parsed and formatted `departure_date` into datetime.
- Created new features:
  - `age_group`: (Child, Teen, Adult, Elder)
  - `departure_day`: Day of the week
  - `departure_month`: Month name
- Standardized values in the `flight_status` column.

### 3. **Load**
- Exported the final cleaned dataset to:
  - A `.csv` file for Tableau consumption.
  - Or stored it in a database like PostgreSQL for scalability.

---

## 📈 Exploratory Data Analysis (EDA)

### 1. **Initial Exploration**
- Used `data.head()`, `data.info()`, `data.describe()`, and `data.isna().sum()` to explore structure and missing values.

### 2. **Visualization**
- **Pie Charts:** Gender distribution
- **Bar Charts:**
  - Flight status breakdown (on-time, delayed, canceled)
  - Age group vs. flight status
  - Nationality & gender counts
  - Top 10 busiest airports
- **Line Plots:** Monthly trends in flight statuses
- **Custom Functions:**
  - `plot_bar()`
  - `plot_groupbar()`

---

## 📌 Key Insights

- **Gender Distribution:** Majority of passengers are male.
- **Age Group:** Most passengers are adults (19–45).
- **Flight Status:** Most flights are on-time or delayed, with few cancellations.
- **Seasonal Trends:** Peak delays during certain months and weekdays.
- **Airport Traffic:** Clear patterns of traffic across top 10 departure airports.

---

## 📊 Tableau Dashboard

### Data Connection
- Processed `.csv` file is imported into Tableau for interactive visual analysis.

### Dashboard Visuals:
- **Gender & Nationality Breakdown:** Pie/Bar charts
- **Flight Status Trends:** Line chart by month
- **Top Airports:** Heatmap or bar chart
- **Seasonal Trends:** Monthly/Weekday distributions
- **Interactive Filters:** Nationality, gender, flight status, date

---

## 🛠 Tools & Technologies

- **Languages:** Python (pandas, numpy, matplotlib, seaborn)
- **ETL & Scripting:** pandas, SQL
- **Visualization:** Tableau Public
- **IDE:** VS Code

---

## ✅ Requirements

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn
