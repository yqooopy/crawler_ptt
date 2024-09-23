from crawler import PTTCrawler
from database import SQLiteDataSaver



crawler = PTTCrawler('Gossiping')
# save data to database
saver = SQLiteDataSaver('database.db')

# auto crawl and save data to database every 5 sec
import time
while True:
    data = crawler.crawl()
    for data in data:
        saver.save_dict(data)
        # print data
        # print(saver.query_data("SELECT * FROM data"))
    print("Waiting for 5 sec...")
    time.sleep(5)



