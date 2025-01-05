from app.db.crud import get_danger_factor_and_naturalness

def calculate_ingredient_score(id_ingredients):
    ingredients = get_danger_factor_and_naturalness(id_ingredients)
    score = 0

    for ingredient in ingredients:
        id, danger_factor, naturalness = ingredient

        if danger_factor.lower() == 'низкий':
            score += 1
        elif danger_factor.lower() == 'средний':
            score += 2

        if naturalness.lower() == 'натуральный':
            score += 1
        elif naturalness.lower() == 'синтетический':
            score += 2

    max_possible_score = len(ingredients) * 4
    normalized_score = (score / max_possible_score) * 5
    return round(normalized_score, 2)

