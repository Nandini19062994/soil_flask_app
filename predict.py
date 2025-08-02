def model_fn(model_dir):
    import joblib
    import os
    model = joblib.load(os.path.join(model_dir, "model.pkl"))
    return model

def input_fn(request_body, request_content_type):
    import json
    if request_content_type == "application/json":
        return list(json.loads(request_body).values())

def predict_fn(input_data, model):
    prediction = model.predict([input_data])
    return prediction[0]

def output_fn(prediction, content_type):
    return str(prediction)
