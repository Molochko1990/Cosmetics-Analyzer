from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from io import BytesIO
from app.services.vision_service import GetTextFromImage
from app.services.text_processing_service import clean_and_extract
from app.services.similarity_service import find_similar_ingredients
from app.services.ingredient_score import calculate_ingredient_score
from app.services.cosmetic_risk_determining_service import determining_cosmetic_risk
from app.db.crud import get_latin_name
import asyncio


# Создание экземпляра бота
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Отправь изображение или текст, чтобы я мог помочь.")


async def process_image(update: Update, context: CallbackContext):
    try:
        file = await update.message.photo[-1].get_file()
        image_bytes = await file.download_as_bytearray()

        print(f"Получено изображение: {file.file_id}, размер: {len(image_bytes)} байт")
        recognized_text = await asyncio.to_thread(GetTextFromImage, BytesIO(image_bytes))
        processed_text = clean_and_extract(recognized_text)
        id_similar_ingredients = find_similar_ingredients(processed_text)
        ingredient_score = calculate_ingredient_score(id_similar_ingredients)
        cosmetic_risk = determining_cosmetic_risk(id_similar_ingredients)
        similar_ingredients = get_latin_name(id_similar_ingredients)

        response = f"Оценка ингредиентов: {ingredient_score}\nРиск косметического продукта: {cosmetic_risk}\nПодобные ингредиенты: {similar_ingredients}"
        await update.message.reply_text(response)
    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")
        await update.message.reply_text(f"Произошла ошибка: {e}")


async def process_text(update: Update, context: CallbackContext):
    try:
        user_text = update.message.text
        print(f"Получен текст от пользователя: {user_text}")

        # Обрабатываем текст
        processed_text = clean_and_extract(user_text)
        id_similar_ingredients = find_similar_ingredients(processed_text)
        ingredient_score = calculate_ingredient_score(id_similar_ingredients)
        cosmetic_risk = determining_cosmetic_risk(id_similar_ingredients)
        similar_ingredients = get_latin_name(id_similar_ingredients)

        response = f"Оценка ингредиентов: {ingredient_score}\nРиск косметического продукта: {cosmetic_risk}\nПодобные ингредиенты: {similar_ingredients}"
        await update.message.reply_text(response)
    except Exception as e:
        print(f"Ошибка при обработке текста: {e}")
        await update.message.reply_text(f"Произошла ошибка: {e}")


def main():
    application = Application.builder().token("").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_text))
    application.add_handler(MessageHandler(filters.PHOTO, process_image))

    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()
