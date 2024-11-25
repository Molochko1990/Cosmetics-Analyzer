from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from io import BytesIO
from app.services.vision_service import GetTextFromImage
from app.services.text_processing_service import clean_and_extract
from app.services.similarity_service import find_similar_words
import asyncio
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        print(f"Получено изображение: {file.filename}, размер: {len(image_bytes)} байт")
        recognized_text = await asyncio.to_thread(GetTextFromImage, BytesIO(image_bytes))
        processed_text = clean_and_extract(recognized_text)
        similar_words = find_similar_words(processed_text)
        print(similar_words)
        return JSONResponse(content={"message": similar_words}, status_code=200)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)
