import sqlite3
import os


def get_latin_ingredients_from_db():
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))  # Путь до корня проекта
    db_path = os.path.join(project_dir, "app", "db", "ingredients.db")

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT id, latin_name FROM ingredients WHERE latin_name IS NOT NULL")
        ingredients = [(row[0], row[1]) for row in cursor.fetchall()]
        connection.close()
        return ingredients
    except sqlite3.OperationalError as e:
        print(f"Error opening database: {e}")

def get_danger_factor_and_naturalness(ids):
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))  # Путь до корня проекта
    db_path = os.path.join(project_dir, "app", "db", "ingredients.db")

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        query = f"""
        SELECT id, danger_factor, naturalness
        FROM ingredients
        WHERE id IN ({', '.join(map(str, ids))})
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        connection.close()

        return rows

    except sqlite3.Error as e:
        print(f"Ошибка подключения или выполнения запроса: {e}")
        return None

def get_latin_name(ids):
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))  # Путь до корня проекта
    db_path = os.path.join(project_dir, "app", "db", "ingredients.db")

    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        query = f"""
        SELECT latin_name, danger_factor
        FROM ingredients
        WHERE id IN ({', '.join(map(str, ids))})
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        connection.close()

        return [[row[0], row[1]] for row in rows]

    except sqlite3.Error as e:
        print(f"Ошибка подключения или выполнения запроса: {e}")
        return None

