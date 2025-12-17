import requests
from config import HF_API_KEY  # Use this instead of hardcoding!


API_URL = "https://router.huggingface.co/hf-inference/models/distilbert-base-uncased-finetuned-sst-2-english"
# Use the imported key here
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def g_s(text):
    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": text})
        
        if response.status_code == 200:
            result = response.json()
            
            # Check if result is a list (success) or a dict (loading/error)
            if isinstance(result, list) and len(result) > 0:
                # The model returns a nested list: [[{'label': 'POSITIVE', 'score': 0.99}]]
                data = result[0][0] 
                sentiment = data['label']
                confidence = data['score']
                print(f"Sentiment: {sentiment} with confidence {confidence:.4f}")
            else:
                print("Model is still loading, please wait a few seconds...")
                print("Response:", result)

        elif response.status_code == 503:
            print("Model is currently loading on Hugging Face servers. Try again in 20 seconds.")
        else:
            print(f"Error: {response.status_code}, Message: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

text1 = input("Enter any text: ")
g_s(text1)
