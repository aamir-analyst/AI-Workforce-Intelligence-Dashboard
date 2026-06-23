import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/AI_Impact_on_Jobs_2030.csv")

# =====================================================
# 1. HIGHEST PAYING JOBS
# =====================================================

salary = (
    df.groupby("Job_Title")["Average_Salary_USD"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))
salary.plot(kind="barh")

plt.title("Top 10 Highest Paying Jobs")
plt.xlabel("Average Salary (USD)")
plt.ylabel("Job Title")

plt.tight_layout()
plt.savefig("screenshots/highest_paying_jobs.png")
plt.close()

# =====================================================
# 2. FUTURE-PROOF CAREERS
# =====================================================

future = (
    df.groupby("Job_Title")["Future_Demand_Score"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))
future.plot(kind="barh")

plt.title("Top 10 Future-Proof Careers")
plt.xlabel("Future Demand Score")
plt.ylabel("Job Title")

plt.tight_layout()
plt.savefig("screenshots/future_proof_jobs.png")
plt.close()

# =====================================================
# 3. INDUSTRY GROWTH POTENTIAL
# =====================================================

industry_growth = (
    df.groupby("Industry")["Job_Growth_2030"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12,6))
industry_growth.plot(kind="bar")

plt.title("Industry Growth Potential by 2030")
plt.xlabel("Industry")
plt.ylabel("Average Job Growth")

plt.tight_layout()
plt.savefig("screenshots/industry_growth.png")
plt.close()

# =====================================================
# 4. AI TOOL USAGE VS SALARY
# =====================================================

salary_ai = (
    df.groupby("AI_Tool_Usage")["Average_Salary_USD"]
    .mean()
)

plt.figure(figsize=(8,5))
salary_ai.plot(kind="bar")

plt.title("Average Salary by AI Tool Usage")
plt.xlabel("AI Tool Usage")
plt.ylabel("Average Salary (USD)")

plt.tight_layout()
plt.savefig("screenshots/salary_vs_ai_usage.png")
plt.close()

# =====================================================
# 5. AI RISK VS FUTURE DEMAND
# =====================================================

job_summary = df.groupby("Job_Title").agg({
    "AI_Replacement_Risk":"mean",
    "Future_Demand_Score":"mean"
})

plt.figure(figsize=(12,8))

plt.scatter(
    job_summary["AI_Replacement_Risk"],
    job_summary["Future_Demand_Score"]
)

for job in job_summary.index:
    plt.annotate(
        job,
        (
            job_summary.loc[job,"AI_Replacement_Risk"],
            job_summary.loc[job,"Future_Demand_Score"]
        ),
        fontsize=7
    )

plt.title("AI Risk vs Future Demand")
plt.xlabel("AI Replacement Risk")
plt.ylabel("Future Demand Score")

plt.tight_layout()
plt.savefig("screenshots/ai_risk_vs_future_demand.png")
plt.close()

# =====================================================
# 6. TOP COUNTRIES BY JOB COUNT
# =====================================================

countries = (
    df["Country"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(12,6))
countries.plot(kind="barh")

plt.title("Top Countries by Job Count")
plt.xlabel("Number of Jobs")
plt.ylabel("Country")

plt.tight_layout()
plt.savefig("screenshots/top_countries.png")
plt.close()

# =====================================================
# 7. HIRING TREND
# =====================================================

hiring = df["Hiring_Trend_2026"].value_counts()

plt.figure(figsize=(7,7))
hiring.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Hiring Trend 2026")

plt.tight_layout()
plt.savefig("screenshots/hiring_trend.png")
plt.close()

print("="*60)
print("ALL INSIGHT CHARTS GENERATED SUCCESSFULLY")
print("="*60)