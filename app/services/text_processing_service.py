import re

def clean_and_extract(ingredients):
    cleaned = re.sub(r'[^a-zA-Zа-яА-ЯёЁ,;: ]', '', ingredients)
    ingredient_list = [ingredient.strip() for ingredient in re.split('[,;:]', cleaned)]
    return ingredient_list
