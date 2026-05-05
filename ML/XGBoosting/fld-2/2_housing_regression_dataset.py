# ================================
# STEP 0: Import Libraries
# ================================
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib


# ================================
# STEP 1: Load Dataset
# ================================
df = pd.read_csv("housing_dataset/boston.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:", df.shape)


# ================================
# STEP 2: Check Missing Values
# ================================
print("\nMissing values:")
print(df.isnull().sum())


# ================================
# STEP 3: Define Features & Target
# ================================
X = df.drop("MEDV", axis=1)
y = df["MEDV"]

print("\nFeature columns:")
print(X.columns)


# ================================
# STEP 4: Train-Test Split
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTrain shape:", X_train.shape)
print("Test shape:", X_test.shape)


# ================================
# STEP 5: Initialize Model
# ================================
xgb_model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)


# ================================
# STEP 6: Train Model
# ================================
print("\nTraining XGBoost model...")
xgb_model.fit(X_train, y_train)
print("Training completed!")


# ================================
# STEP 7: Predictions
# ================================
y_pred = xgb_model.predict(X_test)


# ================================
# STEP 8: Standard Evaluation
# ================================
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("MAE:", mae)
print("R2 Score:", r2)


# ================================
# STEP 9: Custom "Accuracy" Metric
# ================================
# Define tolerance (you can change this)
tolerance = 2.0  # within ±2 units (i.e., $2000)

# Calculate absolute error
errors = np.abs(y_test - y_pred)

# Count how many predictions are within tolerance
correct_predictions = np.sum(errors <= tolerance)

# Accuracy %
accuracy = (correct_predictions / len(y_test)) * 100

print("\nCustom Accuracy (within ±2 units):")
print(f"Accuracy: {accuracy:.2f}%")


# ================================
# STEP 10: Save Model
# ================================
joblib.dump(xgb_model, "xgb_boston_model.pkl")
print("\nModel saved!")


# ================================
# STEP 11: Test Inference
# ================================
loaded_model = joblib.load("xgb_boston_model.pkl")

sample_input = X_test.iloc[0:1]
sample_prediction = loaded_model.predict(sample_input)

print("\nSample Prediction:", sample_prediction[0])
print("Actual Value:", y_test.iloc[0])