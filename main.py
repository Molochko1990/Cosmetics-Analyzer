from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse


from app.services.vision_service import GetTextFromImage

app = FastAPI()


@app.post('/upload_image')
async def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ['image/jpeg', 'image/png']:
        return JSONResponse(content={'Ошибка': 'Неправильный формат файла.'}, status_code=400)

    image_data = await file.read()

    text_composition = GetTextFromImage(0, image_data)

    return {'Состав:': text_composition}
