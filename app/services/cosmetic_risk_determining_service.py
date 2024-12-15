import requests
from app.db.crud import get_latin_name

URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

def determining_cosmetic_risk(ids):
    ingredients = get_latin_name(ids)
    iam_token = "https://yandex.cloud/ru/docs/iam/operations/iam-token/create "
    folder_id = "b1gf3amjf6uujcqkj28e"
    data = {}
    data["modelUri"] = f"gpt://{folder_id}/yandexgpt-lite/latest"
    data["completionOptions"] = {"temperature": 0.3, "maxTokens": 1000}
    data["messages"] = [
        {"role": "system", "text": "Твоя задача проанализировать компоненты и составить топ самых опасных. Твой ответ должен начинаться со слов 'Косметическое средство' опасно или не опасно, 'Самые опасные компоненты это' . Твой ответ должен быть максимум 20 слов"},
        {"role": "user", "text": f"{ingredients}"},
    ]

    response = requests.post(
        URL,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {iam_token}"
        },
        json=data,
    ).json()

    return response['result']['alternatives'][0]['message']['text']





