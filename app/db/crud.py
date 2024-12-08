import sqlite3
import os


def get_ingredients_from_db():
    # Получаем абсолютный путь к базе данных от корня проекта
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))  # Путь до корня проекта
    db_path = os.path.join(project_dir, "app", "db", "ingredients.db")

    print(f"Attempting to open database at: {db_path}")

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT latin_name, danger_factor, naturalness FROM ingredients WHERE latin_name IS NOT NULL")
        ingredients = [(row[0], row[1]) for row in cursor.fetchall()]  # Сохраняем оба столбца в кортежах
        connection.close()
        return ingredients
    except sqlite3.OperationalError as e:
        print(f"Error opening database: {e}")
