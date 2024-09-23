import sqlite3

class SQLiteDataSaver:
    def __init__(self, db_name='data.db'):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        """Create the table if it doesn't exist."""
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS data (
                    timestamp  INTEGER,
                    title TEXT,
                    url TEXT
                )
            ''')
    def save_dict(self, data_dict):
        """Save the given dictionary to the SQLite database."""
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute("SELECT COUNT(*) FROM data WHERE timestamp = ?", (data_dict['timestamp'],))
            if c.fetchone()[0] > 0:
                print("Timestamp already exists. Skipping insert.")
                return   
            c.execute("INSERT INTO data (timestamp,title, url) VALUES (?,?,?)", 
                      (data_dict['timestamp'],data_dict['title'], data_dict['url']))
            conn.commit()
            print("Data saved successfully.",data_dict['timestamp'],data_dict['title'])
            
    def query_data(self, query):
        """Query the data from the database."""
        with sqlite3.connect(self.db_name) as conn:
            c = conn.cursor()
            c.execute(query)
            return c.fetchall()
if __name__ == '__main__':
    # test save dict
    data_saver = SQLiteDataSaver()
    data_saver.save_dict({'timestamp':123,'title': 'Test Title', 'url': 'https://www.example.com'})
    # print data
    print(data_saver.query_data("SELECT * FROM data"))

