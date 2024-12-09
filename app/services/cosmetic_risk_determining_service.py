import requests
from app.db.crud import get_latin_name

URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

def determining_cosmetic_risk(ids):
    ingredients = get_latin_name(ids)
    iam_token = "t1.9euelZqXzcbLyZyWkJuPk4uOm8uQy-3rnpWakI_Pz5rJl5Sbyp2ek8iSyZrl8_dFLyRF-e9MZWx-_N3z9wVeIUX570xlbH78zef1656VmpmQkpuMy5ydx8mbl4nNj4qd7_zF656VmpmQkpuMy5ydx8mbl4nNj4qd.wmIsGOlyeaALRpKuwhEOd4lqWHRDo6JuUqD54eO5vU9xTcXQUVwuz6SZR7-vXun5m9jYjz8cQtwJVSyb34XlCA"
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





