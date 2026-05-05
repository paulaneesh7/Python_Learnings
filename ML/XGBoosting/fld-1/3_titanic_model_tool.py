# Step 1: Imports
import pandas as pd
import joblib


# Step 2: Load trained model
model = joblib.load("titanic_xgboost_model.pkl")


# Step 3: Preprocessing function (same as training)
def preprocess(df):
    df = df.copy()

    # Drop unused columns if present
    for col in ["Name", "Ticket", "Cabin"]:
        if col in df.columns:
            df = df.drop(col, axis=1)

    # Map categorical values
    if "Sex" in df.columns:
        df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

    if "Embarked" in df.columns:
        df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

    # Fill missing values
    if "Age" in df.columns:
        df["Age"] = df["Age"].fillna(df["Age"].mean())

    if "Fare" in df.columns:
        df["Fare"] = df["Fare"].fillna(df["Fare"].mean())

    if "Embarked" in df.columns:
        df["Embarked"] = df["Embarked"].fillna(0)

    return df


# Step 4: Prediction function (THIS is your tool core)
def predict_survival(input_data: dict):
    """
    input_data example:
    {
        "Pclass": 3,
        "Sex": "male",
        "Age": 22,
        "SibSp": 1,
        "Parch": 0,
        "Fare": 7.25,
        "Embarked": "S"
    }
    """

    # Convert input to DataFrame
    df = pd.DataFrame([input_data])

    # Preprocess
    df = preprocess(df)

    # Ensure correct column order
    expected_columns = [
        "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"
    ]
    df = df[expected_columns]

    # Predict
    prediction = model.predict(df)[0]

    # Convert to readable output
    result = "Survived" if prediction == 1 else "Did not survive"

    return {
        "prediction": int(prediction),
        "result": result
    }


# Step 5: Simple test (run file directly)
if __name__ == "__main__":
    sample_input = {
        "Pclass": 3,
        "Sex": "male",
        "Age": 22,
        "SibSp": 1,
        "Parch": 0,
        "Fare": 7.25,
        "Embarked": "S"
    }

    output = predict_survival(sample_input)
    print("Prediction Output:", output)