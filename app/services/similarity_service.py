from fuzzywuzzy import fuzz
from app.db.crud import get_latin_ingredients_from_db


def find_similar_ingredients(ingredients, threshold=85):
    database = get_latin_ingredients_from_db()
    id_ingredient = []
    for ingredient in ingredients:

        for word in database:
            if fuzz.ratio(ingredient.lower(), word[1].lower()) > threshold:
                id_ingredient.append(word[0])
    return id_ingredient
