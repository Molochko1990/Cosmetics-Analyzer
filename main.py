from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from io import BytesIO
from app.services.vision_service import GetTextFromImage
from app.services.text_processing_service import clean_and_extract
from app.services.similarity_service import find_similar_ingredients
from app.services.ingredient_score import calculate_ingredient_score
from app.services.cosmetic_risk_determining_service import determining_cosmetic_risk
from app.db.crud import get_latin_name
import asyncio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Настройки CORS для разрешения всех источников
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserInput(BaseModel):
    text: str


@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        print(f"Получено изображение: {file.filename}, размер: {len(image_bytes)} байт")
        recognized_text = await asyncio.to_thread(GetTextFromImage, BytesIO(image_bytes))
        processed_text = clean_and_extract(recognized_text)
        id_similar_ingredients = find_similar_ingredients(processed_text)
        ingredient_score = calculate_ingredient_score(id_similar_ingredients)
        cosmetic_risk = determining_cosmetic_risk(id_similar_ingredients)
        similar_ingredients = get_latin_name(id_similar_ingredients)

        return JSONResponse(
            content={
                "block1": ingredient_score,
                "block2": cosmetic_risk,
                "block3": similar_ingredients
            },
            status_code=200
        )
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/process-user-input/")
async def process_user_input(user_input: UserInput):
    try:
        print(f"Получен текст от пользователя: {user_input.text}")
        processed_text = clean_and_extract(user_input.text)
        id_similar_ingredients = find_similar_ingredients(processed_text)
        ingredient_score = calculate_ingredient_score(id_similar_ingredients)
        cosmetic_risk = determining_cosmetic_risk(id_similar_ingredients)
        similar_ingredients = get_latin_name(id_similar_ingredients)

        return JSONResponse(
            content={
                "block1": ingredient_score,
                "block2": cosmetic_risk,
                "block3": similar_ingredients
            },
            status_code=200
        )
    except Exception as e:
        print(f"Ошибка при обработке текста: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)
