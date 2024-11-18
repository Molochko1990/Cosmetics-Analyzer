import sqlite3

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Создание таблиц
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        traditional_name VARCHAR(255),
        latin_name VARCHAR(255),
        INCI_name VARCHAR(255),
        danger_factor VARCHAR(20),
        naturalness VARCHAR(20),
        usage TEXT,
        safety TEXT
        
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS effectiveness (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS synonyms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50)
    );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complementary_params (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100)
        );
        """)

    # Создание связующих таблиц
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredient_categories (
        ingredient_id INTEGER,
        category_id INTEGER,
        PRIMARY KEY (ingredient_id, category_id),
        FOREIGN KEY (ingredient_id) REFERENCES ingredients(id),
        FOREIGN KEY (category_id) REFERENCES categories(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredient_effectiveness (
        ingredient_id INTEGER,
        effectiveness_id INTEGER,
        PRIMARY KEY (ingredient_id, effectiveness_id),
        FOREIGN KEY (ingredient_id) REFERENCES ingredients(id),
        FOREIGN KEY (effectiveness_id) REFERENCES effectiveness(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredient_safety_parameters (
        ingredient_id INTEGER,
        safety_parameter_id INTEGER,
        PRIMARY KEY (ingredient_id, safety_parameter_id),
        FOREIGN KEY (ingredient_id) REFERENCES ingredients(id),
        FOREIGN KEY (safety_parameter_id) REFERENCES safety_parameters(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredient_synonyms (
        ingredient_id INTEGER,
        synonym_id INTEGER,
        PRIMARY KEY (ingredient_id, synonym_id),
        FOREIGN KEY (ingredient_id) REFERENCES ingredients(id),
        FOREIGN KEY (synonym_id) REFERENCES synonyms(id)
    );
    """)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

# Создание базы данных
create_database("ingredients.db")
