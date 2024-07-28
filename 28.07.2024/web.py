import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.html = self.fetch_page()

    def fetch_page(self):
        response = requests.get(self.url)
        return response.text

    def parse_html(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        return soup

    def extract_links(self):
        soup = self.parse_html()
        links = []
        for a_tag in soup.find_all('a', href=True):
            links.append(a_tag['href'])
        return links

    def save_links(self, filename):
        links = self.extract_links()
        with open(filename, 'w') as file:
            for link in links:
                file.write(link + '\n')

def main():
    url = 'https://www.example.com'
    scraper = WebScraper(url)
    scraper.save_links('links.txt')

if __name__ == "__main__":
    main()
