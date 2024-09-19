from datetime import datetime
import requests

# Fonction pour demander à Better GPT
def ask_bettergpt(question, gpt_key, gpt_url, model, preparation_prompt):
    headers = {
        "Authorization": f"Bearer {gpt_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": preparation_prompt  # Votre prompt personnalisé ici
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }

    response = requests.post(gpt_url, json=data, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        answer = response_data["choices"][0]["message"]["content"]
        return answer
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None