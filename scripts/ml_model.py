import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
# Load dataset
df = pd.read_csv("data/AI_Impact_on_Jobs_2030.csv")

# Features
features = [
    "Years_Experience",
    "AI_Replacement_Risk",
    "Future_Demand_Score",
    "Average_Salary_USD",
    "Job_Growth_2030",
    "Performance_Score",
    "Job_Satisfaction"
]

X = df[features]

# Target
y = df["Hiring_Trend_2026"]

# Encode target
le = LabelEncoder()
y = le.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Results
print("=" * 60)
print("MODEL ACCURACY")
print("=" * 60)

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")

print("\nClassification Report")
print(classification_report(y_test, y_pred))

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

print("\nFeature Importance")
print(importance.sort_values(
    by="Importance",
    ascending=False
))