import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return None

    return response.text

def scrape_products(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    products = soup.find_all('li', class_='product')  # Update the selector based on the structure
    return products if products else None
