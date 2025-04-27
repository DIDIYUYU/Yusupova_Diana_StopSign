from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
from main import process_image

app = FastAPI()


@app.post("/detect")
async def detect_stop_sign(file: UploadFile = File(...)):
    try:
        # Читаем загруженное изображение
        image_data = await file.read()
        image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

        # Обрабатываем изображение
        processed_image = process_image(image)

        # Конвертируем обратно в формат для отправки
        _, img_encoded = cv2.imencode('.jpg', processed_image)

        return {"success": True, "image": img_encoded.tobytes()}
    except Exception as e:
        return {"success": False, "error": str(e)}