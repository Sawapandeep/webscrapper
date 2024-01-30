# web_scraper.py
import requests
from bs4 import BeautifulSoup
import json

def scrape_tables(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    tables_data = []

    for table in soup.find_all('table'):
        rows = []
        for row in table.find_all('tr'):
            cells = [cell.text.strip() for cell in row.find_all(['th', 'td'])]
            rows.append(cells)
        tables_data.append(rows)

    return tables_data

if __name__ == "__main__":
    # Replace 'https://example.com' with the URL of the webpage you want to scrape
    webpage_url = 'https://www.warframe.com/droptables'
    
    scraped_tables = scrape_tables(webpage_url)

    # Print the scraped data
    print(json.dumps(scraped_tables, indent=2))
