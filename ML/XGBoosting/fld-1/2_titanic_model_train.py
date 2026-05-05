# Step 1: Imports
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


# Step 2: Preprocessing function
def preprocess(df):
    # Drop unnecessary columns
    df = df.drop(["Name", "Ticket", "Cabin"], axis=1)

    # Convert categorical to numeric
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

    # Fill missing values properly
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Fare"] = df["Fare"].fillna(df["Fare"].mean())
    df["Embarked"] = df["Embarked"].fillna(0)

    return df


# Step 3: Load training data
df = pd.read_csv("titanic_disaster_dataset/train.csv")
print("Dataset loaded!")


# Step 4: Preprocess training data
df = preprocess(df)
print("Preprocessing done!")


# Step 5: Features & target
X = df.drop(["Survived", "PassengerId"], axis=1)
y = df["Survived"]


# Step 6: Train-validation split
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Train-validation split done!")


# Step 7: Train model
model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    eval_metric="logloss"
)

model.fit(X_train, y_train)
print("Model training completed!")


# Step 8: Validate model
y_val_pred = model.predict(X_val)
accuracy = accuracy_score(y_val, y_val_pred)
print("Validation Accuracy:", accuracy)


# Step 9: Load test data
test_df = pd.read_csv("titanic_disaster_dataset/test.csv")
passenger_ids = test_df["PassengerId"]

test_df = preprocess(test_df)

# Ensure same column order as training
test_df = test_df[X.columns]

print("Test data loaded and processed!")


# Step 10: Predict on test data
test_predictions = model.predict(test_df)


# Step 11: Save predictions
output = pd.DataFrame({
    "PassengerId": passenger_ids,
    "Survived": test_predictions
})

output.to_csv("predictions.csv", index=False)
print("Predictions saved!")


# Step 12: Save model
joblib.dump(model, "titanic_xgboost_model.pkl")
print("Model saved successfully!")