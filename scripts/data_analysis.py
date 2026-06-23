import pandas as pd

# Load Dataset
df = pd.read_csv("data/AI_Impact_on_Jobs_2030.csv")

# =========================
# BASIC DATA OVERVIEW
# =========================

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print("\nFirst 5 Rows:")
print(df.head())

print("\nRows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

# =========================
# TOP JOB ROLES
# =========================

print("\n" + "=" * 60)
print("TOP 10 JOB ROLES")
print("=" * 60)

top_jobs = df["Job_Title"].value_counts().head(10)

print(top_jobs)

# =========================
# HIGHEST PAYING JOBS
# =========================

print("\n" + "=" * 60)
print("HIGHEST PAYING JOBS")
print("=" * 60)

salary = df.groupby("Job_Title")["Average_Salary_USD"].mean()

highest_salary = salary.sort_values(ascending=False).head(10)

print(highest_salary)

# Save CSV
highest_salary.to_csv(
    "dashboard/highest_paying_jobs.csv"
)

# =========================
# TOP COUNTRIES
# =========================

print("\n" + "=" * 60)
print("TOP COUNTRIES")
print("=" * 60)

top_countries = df["Country"].value_counts().head(10)

print(top_countries)

# =========================
# EDUCATION LEVELS
# =========================

print("\n" + "=" * 60)
print("EDUCATION LEVELS")
print("=" * 60)

print(df["Education_Level"].value_counts())

# =========================
# HIRING TRENDS
# =========================

print("\n" + "=" * 60)
print("HIRING TRENDS 2026")
print("=" * 60)

print(df["Hiring_Trend_2026"].value_counts())

# =========================
# AI TOOL USAGE
# =========================

print("\n" + "=" * 60)
print("AI TOOL USAGE")
print("=" * 60)

print(df["AI_Tool_Usage"].value_counts())

# =========================
# AI REPLACEMENT RISK
# =========================

risk = df.groupby("Job_Title")["AI_Replacement_Risk"].mean()

high_risk = risk.sort_values(
    ascending=False
).head(10)

low_risk = risk.sort_values(
    ascending=True
).head(10)

print("\n" + "=" * 60)
print("TOP 10 HIGH RISK JOBS")
print("=" * 60)

print(high_risk)

print("\n" + "=" * 60)
print("TOP 10 LOW RISK JOBS")
print("=" * 60)

print(low_risk)

# Save CSV
high_risk.to_csv(
    "dashboard/high_risk_jobs.csv"
)

low_risk.to_csv(
    "dashboard/low_risk_jobs.csv"
)

# =========================
# FUTURE DEMAND ANALYSIS
# =========================

future = df.groupby(
    "Job_Title"
)["Future_Demand_Score"].mean()

future_demand = future.sort_values(
    ascending=False
).head(10)

print("\n" + "=" * 60)
print("TOP FUTURE DEMAND JOBS")
print("=" * 60)

print(future_demand)

future_demand.to_csv(
    "dashboard/future_demand_jobs.csv"
)

# =========================
# COUNTRY-WISE AI RISK
# =========================

country_ai = df.groupby(
    "Country"
)["AI_Replacement_Risk"].mean()

print("\n" + "=" * 60)
print("COUNTRIES WITH HIGHEST AI RISK")
print("=" * 60)

print(country_ai.sort_values(
    ascending=False
).head(10))

# =========================
# SKILLS ANALYSIS
# =========================

print("\n" + "=" * 60)
print("TOP 20 REQUIRED SKILLS")
print("=" * 60)

skills = df["Required_Skills"].value_counts().head(20)

print(skills)

skills.to_csv(
    "dashboard/top_skills.csv"
)

# =========================
# HIRING TREND VS INDUSTRY
# =========================

print("\n" + "=" * 60)
print("HIRING TREND VS INDUSTRY")
print("=" * 60)

hiring_industry = pd.crosstab(
    df["Hiring_Trend_2026"],
    df["Industry"]
)

print(hiring_industry)

hiring_industry.to_csv(
    "dashboard/hiring_trend_vs_industry.csv"
)

print("\n" + "=" * 60)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)