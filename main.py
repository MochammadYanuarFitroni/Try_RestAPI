from fastapi import FastAPI, Response, UploadFile
import uvicorn
import traceback

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "dunia"}

@app.post("/uploadfile")
async def create_upload_file(upload_file:UploadFile, response: Response):
    try:
        if upload_file.content_type not in ["image/jpeg", "image/png"]:
            response.status_code = 400
            return {"message": "Only image/jpeg & image/png supported"}
        
        # tes = upload_file.file.read()
        # img = image.load_img(BytesIO(tes), target_size=(64, 64))
        # # print(img)
        # img2 = image.img_to_array(img)
        # # print(img2)
        # img3 = img2/225.0
        # # print(img3.shape)
        # img4 = img3.reshape(1, 64, 64, 3)
        # # print(img4)

        # pred = model.predict(img4)
        # pred *= 100
        # print(pred)
        # indeks = np.argmax(pred)
        # print(indeks)
        # hasil = labels[indeks]
        # print(hasil)
        # # result = model.predict(img4)
        # # print(type(result))

        return {"filename": upload_file.filename}
    
    except Exception as e:
        traceback.print_exc()
        response.status_code = 500
        return {"message": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)