from transformers import pipeline
classifier = pipeline(
    task="sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)
def get_sentiment(text):
    result = classifier(text)[0]
    label = result["label"]
    score = result["score"]
    print(f"Sentiment: {label}, Confidence{score:.2f}")

if __name__ == "__main__":
    text= input("Enter text: ")
    get_sentiment(text)
