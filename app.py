from fastapi import FastAPI

app = FastAPI(title="Pipeline Test")

@app.get("/")
async def home():
    return "<h2>This is a sample Pipelining Project</h2>"

from inference_onnx import ColaONNXPredictor

# load the model
predictor = ColaONNXPredictor("./models/model.onnx")

@app.get("/predict")
async def get_prediction(text: str):
    result =  predictor.predict(text)
    return result