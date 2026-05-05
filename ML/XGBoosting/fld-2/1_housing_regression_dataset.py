# ================================
# STEP 0: Import Libraries
# ================================
import pandas as pd
import numpy as np

# Train-test split
from sklearn.model_selection import train_test_split

# Model
from xgboost import XGBRegressor

# Evaluation metrics
from sklearn.metrics import mean_absolute_error, r2_score

# Model saving
import joblib


# ================================
# STEP 1: Load Dataset
# ================================
# Make sure your CSV file name is correct
df = pd.read_csv("housing_dataset/boston.csv")

# Quick look at data
print("First 5 rows:")
print(df.head())

print("\nDataset shape:", df.shape)


# ================================
# STEP 2: Basic Data Check
# ================================
# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# If there were missing values, we would handle them
# But this dataset is usually clean


# ================================
# STEP 3: Define Features (X) and Target (y)
# ================================
# X = all columns except MEDV
# y = target (what we want to predict)

X = df.drop("MEDV", axis=1)
y = df["MEDV"]

print("\nFeature columns:")
print(X.columns)


# ================================
# STEP 4: Train-Test Split
# ================================
# Split data into training and testing
# 80% training, 20% testing

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nTrain shape:", X_train.shape)
print("Test shape:", X_test.shape)


# ================================
# STEP 5: Initialize XGBoost Model
# ================================
# Using basic parameters (can tune later)

xgb_model = XGBRegressor(
    n_estimators=100,   # number of trees
    learning_rate=0.1,  # step size
    max_depth=5,        # depth of each tree
    random_state=42
)


# ================================
# STEP 6: Train the Model
# ================================
print("\nTraining XGBoost model...")

xgb_model.fit(X_train, y_train)

print("Training completed!")


# ================================
# STEP 7: Make Predictions
# ================================
# Predict on test data

y_pred = xgb_model.predict(X_test)


# ================================
# STEP 8: Evaluate Model Performance
# ================================
# MAE → average error
# R2 → how well model explains variance

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("MAE (Mean Absolute Error):", mae)
print("R2 Score:", r2)


# ================================
# STEP 9: Save the Trained Model
# ================================
joblib.dump(xgb_model, "xgb_boston_model.pkl")

print("\nModel saved as xgb_boston_model.pkl")


# ================================
# STEP 10: Load Model + Test Inference
# ================================
# (This simulates how your MCP tool will use it)

loaded_model = joblib.load("xgb_boston_model.pkl")

# Take one sample from test data
sample_input = X_test.iloc[0:1]

# Predict using loaded model
sample_prediction = loaded_model.predict(sample_input)

print("\nSample Prediction:", sample_prediction[0])
print("Actual Value:", y_test.iloc[0])