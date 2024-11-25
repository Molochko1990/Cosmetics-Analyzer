import re

def clean_and_extract(ingredients):
    cleaned = re.sub(r'[^a-zA-Z,;: ]', '', ingredients)
    ingredient_list = [ingredient.strip() for ingredient in re.split('[,;:]', cleaned)]
    return ingredient_list

