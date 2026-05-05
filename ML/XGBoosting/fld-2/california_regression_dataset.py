import joblib
import pandas as pd
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_absolute_error, r2_score



# Step 1: Load Dataset
data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target  # this is price

print(df.head())


# Step 2: Prepare Data
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)




# Step 3: Train Models (Regression Versions)
model_xgb = XGBRegressor()
model_xgb.fit(X_train, y_train)




# Random Forest Regressor
model_rf = RandomForestRegressor()
model_rf.fit(X_train, y_train)


"""
Step 4: Evaluate (IMPORTANT DIFFERENCE)

In classification → accuracy
In regression → we use:

MAE (error)
RMSE (error)
R² score (goodness of fit)

"""
preds = model_xgb.predict(X_test)

print("MAE:", mean_absolute_error(y_test, preds))
print("R2 Score:", r2_score(y_test, preds))






# Step 5: Save Models
joblib.dump(model_xgb, "xgb_regressor.pkl")
joblib.dump(model_rf, "rf_regressor.pkl")

