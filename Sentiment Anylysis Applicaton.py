import requests
from config import HF_API_KEY


API_URL = "/https://router.huggingface.comodels/distilbert-base-uncased-finetuned-sst-2-english"
headers = {"Authorization": "Bearer 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"}

def g_s(text):
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": text})
        if response.status_code == 200:
            result = response.json()
            print("Response :", result)
            sentiment = result[0]['label']
            confidence = result[0]['score']

            print(f"Sentiment {sentiment} with confidence {confidence}")

        else:
            print(f"Error : {response.status_code} , Message : {response}")
    except requests.exceptions.RequestException as e:
        print(f"An error occured {e}")


text1 = input("Enter any text")
