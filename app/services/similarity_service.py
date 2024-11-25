from fuzzywuzzy import fuzz

database = [
    "Water", "Glyceryl Stearate", "Cetearyl Alcohol", "Stearic Acid",
    "Ethylhexylglycerin", "Fragrance", "Sodium Chloride", "Pentylene Glycol",
    "Tetrasodium EDTA", "Olea Europaea"
]
# ingredients = [
#     "Wter", "Glyceryl Stearate", "Ethylhexy Stearat", "Giycerin",
#     "Cetearyl Alcohol", "Stearic Acid", "Phenoxyethanol", "Sodium PCA"
# ]
def find_similar_words(ingredients, threshold=70):
    database = [
        "Water", "Glyceryl Stearate", "Cetearyl Alcohol", "Stearic Acid",
        "Ethylhexylglycerin", "Fragrance", "Sodium Chloride", "Pentylene Glycol",
        "Tetrasodium EDTA", "Olea Europaea"
    ]
    matches = {}
    for ingredient in ingredients:
        matches[ingredient] = [
            word for word in database if fuzz.ratio(ingredient.lower(), word.lower()) > threshold
        ]
    return matches
