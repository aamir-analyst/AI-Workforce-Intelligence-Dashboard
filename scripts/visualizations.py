import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/AI_Impact_on_Jobs_2030.csv")

# 1. Top Job Roles
top_jobs = df["Job_Title"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_jobs.plot(kind="bar")
plt.title("Top 10 Job Roles")
plt.tight_layout()
plt.savefig("screenshots/top_jobs.png")
plt.close()

# 2. Top Countries
countries = df["Country"].value_counts().head(10)

plt.figure(figsize=(10,5))
countries.plot(kind="bar")
plt.title("Top Countries")
plt.tight_layout()
plt.savefig("screenshots/top_countries.png")
plt.close()

# 3. Hiring Trend
hiring = df["Hiring_Trend_2026"].value_counts()

plt.figure(figsize=(6,6))
hiring.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Hiring Trend 2026")
plt.savefig("screenshots/hiring_trend.png")
plt.close()

# 4. Education Level
education = df["Education_Level"].value_counts()

plt.figure(figsize=(6,6))
education.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Education Level Distribution")
plt.savefig("screenshots/education_level.png")
plt.close()

# 5. Salary vs AI Risk (Advanced Chart)
plt.figure(figsize=(10,6))
plt.scatter(
    df["AI_Replacement_Risk"],
    df["Average_Salary_USD"]
)

plt.title("Salary vs AI Replacement Risk")
plt.xlabel("AI Replacement Risk")
plt.ylabel("Average Salary (USD)")
plt.tight_layout()
plt.savefig("screenshots/salary_vs_ai_risk.png")
plt.close()

# 6. Future Demand Score Distribution
plt.figure(figsize=(10,6))
plt.hist(df["Future_Demand_Score"], bins=20)
plt.title("Future Demand Score Distribution")
plt.xlabel("Future Demand Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("screenshots/future_demand_distribution.png")
plt.close()

print("All charts saved successfully!")


import seaborn as sns

plt.figure(figsize=(10,6))

numeric_cols = [
    "Years_Experience",
    "AI_Replacement_Risk",
    "Future_Demand_Score",
    "Average_Salary_USD",
    "Job_Growth_2030",
    "Performance_Score",
    "Job_Satisfaction"
]

sns.heatmap(
    df[numeric_cols].corr(),
    annot=True
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("screenshots/correlation_heatmap.png")
plt.close()