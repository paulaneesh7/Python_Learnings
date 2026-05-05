from langchain.tools import tool
from titanic_model_tool import predict_survival


@tool
def titanic_survival_predictor(input_data: dict) -> dict:
    """
    Predict whether a Titanic passenger would survive.

    Input should be a JSON with:
    Pclass, Sex, Age, SibSp, Parch, Fare, Embarked
    """
    return predict_survival(input_data)