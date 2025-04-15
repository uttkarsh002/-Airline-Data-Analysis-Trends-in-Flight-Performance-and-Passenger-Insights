import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# --------------------- EXTRACT ---------------------
# Load the dataset
file_path = "Airline Dataset Updated - v2.csv"  # Update with actual file path
df = pd.read_csv(file_path)

# --------------------- TRANSFORM ---------------------
# Rename columns (convert to lowercase & replace spaces with underscores)
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Convert departure_date to datetime
df['departure_date'] = pd.to_datetime(df['departure_date'], errors='coerce')

# Drop rows with missing departure dates
df = df.dropna(subset=['departure_date'])

# Handle missing values (Fill NA with appropriate values or drop rows)
df['age'].fillna(df['age'].median(), inplace=True)  # Fill missing ages with median
df.dropna(subset=['gender', 'nationality', 'flight_status', 'airport_name'], inplace=True)

# Create age group column
def categorize_age(age):
    if age < 13:
        return "Child"
    elif 13 <= age < 18:
        return "Teen"
    elif 18 <= age < 45:
        return "Adult"
    else:
        return "Elder"

df['age_group'] = df['age'].apply(categorize_age)

# Extract departure day & month
df['departure_day'] = df['departure_date'].dt.day_name()
df['departure_month'] = df['departure_date'].dt.month_name()

# Standardize flight status values
df['flight_status'] = df['flight_status'].str.strip().str.capitalize()

# --------------------- LOAD ---------------------
# Database connection setup (PostgreSQ) - Update credentials
DB_TYPE = 'postgresql'  
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_HOST = 'localhost'  
DB_PORT = '5432'  
DB_NAME = 'airline_db'

# Create database engine
engine = create_engine(f"{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Load the cleaned data into the database
table_name = 'airline_data'
df.to_sql(table_name, engine, if_exists='replace', index=False)

print("ETL process completed successfully!")
