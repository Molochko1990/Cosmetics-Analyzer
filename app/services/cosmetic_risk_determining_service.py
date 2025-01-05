from app.db.crud import get_danger_factor_and_naturalness

def get_most_dangerous_ingredient(id_ingredients):
    ingredients = get_danger_factor_and_naturalness(id_ingredients)
    most_dangerous = None
    highest_danger_score = -1

    for ingredient in ingredients:
        id, danger_factor, naturalness = ingredient
        if danger_factor.lower() == 'низкий':
            danger_value = 1
        elif danger_factor.lower() == 'средний':
            danger_value = 2
        elif danger_factor.lower() == 'высокий':
            danger_value = 3
        else:
            danger_value = 0
        if naturalness.lower() == 'натуральный':
            naturalness_value = 1
        elif naturalness.lower() == 'синтетический':
            naturalness_value = 2
        else:
            naturalness_value = 0
        total_score = danger_value + naturalness_value
        if total_score > highest_danger_score:
            most_dangerous = ingredient
            highest_danger_score = total_score

    return most_dangerous[0]
