import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("netflix_revenue_updated.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(r"\s+", " ", regex=True)

print(df.columns)

# Features
X = df[
    [
        "UCAN Members",
        "EMEA Members",
        "LATM Members",
        "APAC Members",
        "UCAN ARPU",
        "EMEA ARPU",
        "LATM ARPU",
        "APAC ARPU",
    ]
]

# Target
y = df["Global Revenue"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("✅ Model trained successfully!")