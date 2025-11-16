import yagmail
import pandas
from main import NewsFeed
import datetime
while True:
    if datetime.datetimenow.hour==17 and datetime.datetimenow.minute==43:
        df = pandas.read_excel("C:\\Users\\nupur\\Documents\\people.xlsx")
        for index , row in df.iterrows():
                today=datetime.date.now().strftime('%Y-%m-%d')
                yesterday=datetime.datetime.now()-datetime.timedelta(days=1).strftime('%Y-%m-%d')
                news_feed=NewsFeed(interest=row["interest"],from_date=yesterday,to_date=today)
                email = yagmail.SMTP(user="gs123@gmailcom", password="126543@fk")
                email.send(to=['email'], subject=f"your{row['interst']} news for today!",
                contents=f"hi{row['name']}\n see what's on about {row['interst']} today.\n")

    time.sleep(60)