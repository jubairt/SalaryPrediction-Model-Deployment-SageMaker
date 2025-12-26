import json
import pandas as pd
import joblib

def model_fn(model_dir):
    model = joblib.load(f"{model_dir}/model.pkl")
    return model

def input_fn(request_body, content_type):
    data = json.loads(request_body)
    return pd.DataFrame(data)


def predict_fn(input_data, model):
    prediction = model.predict(input_data)
    return prediction

def output_fn(prediction, accept):
    return json.dump(prediction.tolist())