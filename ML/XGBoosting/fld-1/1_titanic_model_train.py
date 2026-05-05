# Step 1: Imports
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


# Step 2: Load dataset
df = pd.read_csv("titanic_disaster_dataset/train.csv")


print("Dataset loaded successfully!")
print(df.head())



# Step 3: Basic preprocessing


# Drop useless columns
df = df.drop(["Name", "Ticket", "Cabin"], axis=1)


# Convert categorical to numeric
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})


# Fill missing values
df = df.fillna(df.mean())



print("\nPreprocessing done!")



# Step 4: Features & target
X = df.drop("Survived", axis=1)
y = df["Survived"]


# Step5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



# Step 6: Train model
model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    use_label_encoder=False,
    eval_metric="logloss",
)



model.fit(X_train, y_train)


print("\nModel training completed!")



# Step 7: Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)


print("\nAccuracy:", accuracy)



# Step 8: Save model
joblib.dump(model, "titanic_xgboost_model.pkl")

print("\nModel saved successfully!")
