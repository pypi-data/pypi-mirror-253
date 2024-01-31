from .utils import fetch_page, scrape_products

class ProductScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.page_number = 1
        self.total_products = 0

    def fetch_page(self):
        url = f'{self.base_url}{self.page_number}/'
        return fetch_page(url)

    def scrape_products(self, html_content):
        products = scrape_products(html_content)

        if not products:
            return None

        num_products = len(products)
        self.total_products += num_products

        print(f'Page {self.page_number}: Number of products: {num_products}')

        # Increment to the next page
        self.page_number += 1

    def run(self):
        while True:
            html_content = self.fetch_page()

            if not html_content:
                break  # Stop the loop if there's an issue fetching the page

            self.scrape_products(html_content)

        print(f'Total number of products: {self.total_products}')
