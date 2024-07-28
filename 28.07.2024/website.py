import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    return response.text

def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a_tag in soup.find_all('a', href=True):
        links.append(a_tag['href'])
    return links

def main():
    url = 'https://www.example.com'
    html = fetch_page(url)
    links = extract_links(html)
    for link in links:
        print(link)

if __name__ == "__main__":
    main()
