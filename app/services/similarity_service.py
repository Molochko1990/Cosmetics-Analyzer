from fuzzywuzzy import fuzz
from app.db.crud import get_latin_ingredients_from_db, get_russian_ingredients_from_db


def find_similar_ingredients_for_image(ingredients, threshold=85):
    latin_database = get_latin_ingredients_from_db()
    russian_database = get_russian_ingredients_from_db()

    latin_ids = []
    russian_ids = []

    for ingredient in ingredients:
        for word in latin_database:
            if fuzz.ratio(ingredient.lower(), word[1].lower()) > threshold:
                latin_ids.append(word[0])
                break

    for ingredient in ingredients:
        for word in russian_database:
            if fuzz.ratio(ingredient.lower(), word[1].lower()) > threshold:
                russian_ids.append(word[0])
                break

    if len(russian_ids) > len(latin_ids):
        return russian_ids
    else:
        return latin_ids

def find_similar_ingredients_for_text(ingredients, threshold=90):
    latin_database = get_latin_ingredients_from_db()
    russian_database = get_russian_ingredients_from_db()

    latin_ids = []
    russian_ids = []

    for ingredient in ingredients:
        for word in latin_database:
            if fuzz.ratio(ingredient.lower(), word[1].lower()) > threshold:
                latin_ids.append(word[0])
                break

    for ingredient in ingredients:
        for word in russian_database:
            if fuzz.ratio(ingredient.lower(), word[1].lower()) > threshold:
                russian_ids.append(word[0])
                break

    if len(russian_ids) > len(latin_ids):
        return russian_ids
    else:
        return latin_ids
