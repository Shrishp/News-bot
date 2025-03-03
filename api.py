import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")  # Securely fetching API key
BASE_URL = "https://newsapi.org/v2/top-headlines"

def get_latest_news(country="us", category="technology"):
    url = f"{BASE_URL}?country={country}&category={category}&apiKey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])
        for i, article in enumerate(articles[:5], start=1):
            print(f"{i}. {article['title']}\n   {article['url']}\n")
    else:
        print("Error fetching news:", response.status_code)

if __name__ == "__main__":
    get_latest_news()
