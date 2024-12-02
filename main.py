from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from app.services.vision_service import GetTextFromImage

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы с любых доменов
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)


@app.post('/upload_image')
async def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ['image/jpeg', 'image/png']:
        return JSONResponse(content={'Ошибка': 'Неправильный формат файла.'}, status_code=400)

    image_data = await file.read()

    text_composition = GetTextFromImage(1, image_data)

    return {'Состав': text_composition}


@app.post("/submit-text/")
async def submit_text(text: str = Form(...)):
    text_composition = text
    return JSONResponse(content={"Состав": text_composition})
