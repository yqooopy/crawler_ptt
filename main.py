from crawler import PTTCrawler
from database import SQLiteDataSaver



crawler = PTTCrawler('Lifeismoney')
data = crawler.crawl()

# save data to database
saver = SQLiteDataSaver('database.db')
for d in data:
    print(d)
    saver.save_dict(d)
    print('Data saved to SQLite database')

 
