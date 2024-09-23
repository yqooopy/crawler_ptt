from crawler import PTTCrawler
from database import SQLiteDataSaver
import time



crawler = PTTCrawler('Lifeismoney')
saver = SQLiteDataSaver('database.db')

# auto crawl and save data to database every 5 sec
while True:
    data = crawler.crawl()
    for data in data:
        saver.save_dict(data)
    print("Waiting for 5 sec...")
    time.sleep(5)



