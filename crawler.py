import requests
from bs4 import BeautifulSoup

class PTTCrawler:
    def __init__(self, board):
        self.base_url = f'https://www.ptt.cc/bbs/{board}/index.html'
        self.headers = {
            'cookie': 'over18=1;'
        }

    def fetch_page(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            print(f'Failed to retrieve page: {response.status_code}')
            return None

    def parse_titles(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('div', class_='title')
        return [(title.a.text.strip(), title.a['href']) for title in titles if title.a]

    def crawl(self):
        html = self.fetch_page(self.base_url)
        data = []

        if html:
            titles = self.parse_titles(html)
            for title in titles:
                # print(title[0], title[1])
                datadict = {'title': title[0], 'url': title[1]}
                data.append(datadict)
            return data
if __name__ == '__main__':
    crawler = PTTCrawler('Gossiping')
    crawler.crawl()


