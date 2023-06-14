from fastapi import FastAPI, Response, UploadFile
from image_preprocessing import load_image
from predict_image import make_predict

import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def predict(file: UploadFile = UploadFile(...)):
    image = await file.read()
    image_pre = load_image(image)
    result = make_predict(image_pre)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)