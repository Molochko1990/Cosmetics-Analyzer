from fuzzywuzzy import fuzz
from app.db.crud import get_ingredients_from_db


def find_similar_words(ingredients, threshold=85):
    database = get_ingredients_from_db()
    matches = {}
    name = ''
    for ingredient in ingredients:
        ingredient_matches = []
        for word in database:
            if fuzz.ratio(ingredient.lower(), word[0].lower()) > threshold:
                print(word)
                ingredient_matches.append(f' Фактор опасности: {word[1]}')
                name = word[0]
                break
        matches[name] = ingredient_matches

    # Удаление ключей с пустыми значениями
    matches = {k: v for k, v in matches.items() if v}

    return matches
