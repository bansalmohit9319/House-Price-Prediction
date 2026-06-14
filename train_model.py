import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import joblib

# Load Dataset
data = pd.read_csv("../housing.csv")

# Features
X = data[
    [
        "area_sqft",
        "bedrooms",
        "bathrooms",
        "living_area_sqft",
        "kitchen_area_sqft",
        "dining_area_sqft",
        "garage_area_sqft",
        "balcony_area_sqft",
        "floors",
        "age_years",
        "location",
        "property_type"
    ]
]

# Target
y = data["price_usd"]

# Categorical Columns
categorical_features = [
    "location",
    "property_type"
]

# Numeric Columns
numeric_features = [
    "area_sqft",
    "bedrooms",
    "bathrooms",
    "living_area_sqft",
    "kitchen_area_sqft",
    "dining_area_sqft",
    "garage_area_sqft",
    "balcony_area_sqft",
    "floors",
    "age_years"
]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

# Model Pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ))
])

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model.fit(X_train, y_train)

# Save Model
joblib.dump(model, "house_model.pkl")

# Accuracy
score = model.score(X_test, y_test)

print("✅ Model Trained Successfully!")
print(f"📊 R² Score: {score:.4f}")
print("💾 Saved as house_model.pkl")