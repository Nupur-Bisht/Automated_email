import requests
from pprint import pprint
import os
from dotenv import load_dotenv

dotenv.load_dotenv()
class NewsFeed:
    base_url = "https://newsfeed.org/v2/everything?"

    def __init__(self,interest,from_date,to_date,lang):
        self.api_key = os.getenv("API_KEY")
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.lang = lang

    def get(self):

         url=("https://newsapi.org/v2/everything?"
             f"qInTitle={self.interest}&"
             f"from={self.from_date}&"
             f"to={self.to_date}&"
             f"language={self.lang}&"
             f"apiKey= {self.api_key} ")
         responce =requests.get(url)
         content=responce.json()
         x= content['articles']
         email_body=''
         for article in x:
                email_body=email_body+article['title']+"\n"+article['url']+"\n\n"
         return email_body
if __name__=="__main__":
    news_feed =NewsFeed(interest='nasa',from_date='2025-08-28',to_date='2025-08-31',lang='en')
    print(news_feed.get())
