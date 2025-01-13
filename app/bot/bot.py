from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from io import BytesIO
from app.services.vision_service import GetTextFromImage
from app.services.text_processing_service import clean_and_extract
from app.services.similarity_service import find_similar_ingredients_for_image, find_similar_ingredients_for_text
from app.services.ingredient_score import calculate_ingredient_score
from app.services.cosmetic_risk_determining_service import get_most_dangerous_ingredient
from app.db.crud import get_latin_name
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Отправь изображение или текст, чтобы я мог рассказать больше о безопасности этого косметического средства.")

async def process_image(update: Update, context: CallbackContext):
    try:
        file = await update.message.photo[-1].get_file()
        image_bytes = await file.download_as_bytearray()
        recognized_text = await asyncio.to_thread(GetTextFromImage, BytesIO(image_bytes))
        processed_text = clean_and_extract(recognized_text)
        id_similar_ingredients = find_similar_ingredients_for_image(processed_text)
        ingredient_score = calculate_ingredient_score(id_similar_ingredients)
        id_most_danger_ingredients = get_most_dangerous_ingredient(id_similar_ingredients)
        cosmetic_risk = get_latin_name([id_most_danger_ingredients])
        similar_ingredients = get_latin_name(id_similar_ingredients)
        danger_ingredient_str = " - ".join(cosmetic_risk[0])
        all_ingredients_str = "\n".join([ingredient[0] + " - " + ingredient[1] for ingredient in similar_ingredients])
        response = f"*Средняя оценка опасности всех ингредиентов:* {ingredient_score} из 5\n\n*Самый опасный ингредиент в этом составе:*\n\n{danger_ingredient_str}\n\n*Все ингредиенты которые были найдены в базе:*\n\n{all_ingredients_str}"
        await update.message.reply_text(response, parse_mode="Markdown")
    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")
        await update.message.reply_text(f"Произошла ошибка. Сервис поддерживает только rus/en языки. Попробуйте ввести состав вручную")

async def process_text(update: Update, context: CallbackContext):
    try:
        user_text = update.message.text
        print(f"Получен текст от пользователя: {user_text}")
        processed_text = clean_and_extract(user_text)
        id_similar_ingredients = find_similar_ingredients_for_text(processed_text)
        ingredient_score = calculate_ingredient_score(id_similar_ingredients)
        id_most_danger_ingredients = get_most_dangerous_ingredient(id_similar_ingredients)
        cosmetic_risk = get_latin_name([id_most_danger_ingredients])
        similar_ingredients = get_latin_name(id_similar_ingredients)
        danger_ingredient_str = " - ".join(cosmetic_risk[0])
        all_ingredients_str = "\n".join([ingredient[0] + " - " + ingredient[1] for ingredient in similar_ingredients])
        response = f"*Средняя оценка опасности всех ингредиентов:* {ingredient_score} из 5\n\n*Самый опасный ингредиент в этом составе:*\n\n{danger_ingredient_str}\n\n*Все ингредиенты которые были найдены в базе:*\n\n{all_ingredients_str}"
        await update.message.reply_text(response, parse_mode="Markdown")

    except Exception as e:
        print(f"Ошибка при обработке текста: {e}")
        await update.message.reply_text(f"Произошла ошибка. Сервис поддерживает только rus/en языки. Попробуйте ввести состав заново")

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_text))
    application.add_handler(MessageHandler(filters.PHOTO, process_image))

    application.run_polling()

if __name__ == '__main__':
    main()
