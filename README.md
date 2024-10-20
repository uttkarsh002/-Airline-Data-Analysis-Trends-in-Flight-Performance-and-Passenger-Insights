# -Airline-Data-Analysis-Trends-in-Flight-Performance-and-Passenger-Insights

Overview
This project analyzes airline passenger data to explore various patterns, trends, and insights related to passengers' demographics, flight statuses, and other factors. The analysis involves data manipulation, cleaning, visualization, and statistical summaries using Python libraries such as pandas, numpy, matplotlib, and seaborn.

The goal is to understand passenger profiles (age, gender, nationality), flight statuses (on-time, delayed, or canceled), and seasonal patterns (departure dates, busy days/months). The project uses various visualization techniques to present the data meaningfully.

Data
The dataset used is named Airline Dataset Updated - v2.csv, containing passenger and flight information such as:

Passenger's age, gender, and nationality
Flight departure date
Flight status (on-time, delayed, canceled)
Other details about the airports and flight departure day.
Project Structure
The main steps in the project can be broken down into the following sections:

1. Data Loading and Initial Exploration
Loading data: The dataset is loaded using pandas.read_csv().
Initial exploration: data.head(), data.info(), and data.describe() are used to inspect the structure and summary of the dataset.
Checking for missing values: data.isna().sum() to identify any columns with missing data.
2. Data Preprocessing
Renaming columns: Column names are converted to lowercase and spaces replaced with underscores using airline.columns.
Handling dates: The departure_date column is cleaned and transformed into a datetime format. Dashes are replaced with slashes and the column is converted using pd.to_datetime().
3. Feature Engineering
Creating Age Groups: The dataset is enriched with a new column age_group, which categorizes passengers into 'Child', 'Teen', 'Adult', and 'Elder' based on their age. A custom function cat_age is applied using airline['age'].apply(cat_age).
Extracting Departure Day/Month: Day names (departure_day) and months (departure_month) are extracted from the departure_date column.
4. Data Visualization
Several visualizations are used to explore different dimensions of the dataset.

Pie Charts
Gender distribution: A pie chart is created to visualize the gender distribution of passengers using plt.pie().
Bar Charts
Flight status distribution: A bar chart shows the count of different flight statuses.
Age group vs. Flight status: Stacked bar charts compare flight status (on-time, delayed, canceled) by age group.
Nationality and Gender: Bar charts show the top 20 and top 10 nationalities by gender and the count of passengers from various countries.
Airport and Gender: Passenger gender distributions at different airports.
Line Plots
Flight Status Over Time: Line plots track how flight statuses (canceled, delayed, on-time) evolve over time, grouped by month using resample() and sns.lineplot().
5. Helper Functions
Custom helper functions are created to streamline plotting:

plot_groupbar: This function creates grouped bar charts based on any two columns (e.g., age group vs flight status, nationality vs gender).
plot_bar: This function generates a simple bar chart to show the count of categories in a specific column.
6. Insights and Trends
Busiest days and months: The dataset is analyzed to identify the busiest flight days and months by counting occurrences of departure_day and departure_month.
Top Nationalities and Airports: Top countries of passengers and top airports with the highest passenger count are identified.
Flight status trends: Using time-based resampling, flight statuses (on-time, delayed, canceled) are analyzed over time to detect any seasonal patterns or trends.
Key Findings
Gender Distribution: A larger percentage of passengers are male, as indicated by the gender distribution pie chart.
Age Groups: Adults (aged 19-45) form the largest group of passengers.
Nationality Insights: The top 10 nationalities include a mix of passengers from various continents.
Flight Status: The majority of flights are either on time or delayed, with fewer cancellations.
Time-based Trends: Certain months and days of the week are busier in terms of flights, and delays or cancellations may spike during these times.
Prerequisites
To run the project, you will need the following Python libraries:

pandas: For data manipulation and analysis.
numpy: For numerical computations.
matplotlib: For creating visualizations.
seaborn: For enhanced statistical visualizations.
Install the libraries via pip:

bash
Copy code
pip install pandas numpy matplotlib seaborn
How to Run
Clone the repository and navigate to the project directory.
Ensure you have the dataset Airline Dataset Updated - v2.csv in the correct path.
Run the script using a Python environment. All visualizations will be generated and displayed.
Directory Structure
bash
Copy code
- Airline-Passenger-Data-Analysis/
    - data/
        - Airline Dataset Updated - v2.csv  # Dataset file
    - analysis_script.py                    # Main script for analysis
    - README.md                             # Project documentation
Future Improvements
Machine Learning: Build predictive models to forecast flight delays or cancellations.
Interactive Dashboards: Integrate with Plotly or Dash to create an interactive dashboard.
Geospatial Analysis: Use maps to plot flight routes and delays across different regions.
License
This project is open-source and available under the MIT License.
