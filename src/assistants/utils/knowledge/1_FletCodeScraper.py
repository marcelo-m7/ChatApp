import os
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse

class FletCodeScraper:
    def __init__(self, base_url: str, sitemap_url: str, save_folder: str) -> None:
        self.base_url = base_url
        self.sitemap_url = sitemap_url
        self.save_folder = save_folder
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        os.makedirs(save_folder, exist_ok=True)

    def fetch_sitemap(self) -> list:
        try:
            response = requests.get(self.sitemap_url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'xml')
            return [loc.text for loc in soup.find_all('loc') if loc.text.startswith(self.base_url)]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching sitemap: {e}")
            return []

    def extract_python_code(self, url: str) -> list:
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            code_blocks = []
            for block in soup.find_all('pre'):
                if "language-python" in block.get("class", []):
                    code_blocks.append(block.text.strip())
            
            return code_blocks
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return []

    def save_to_file(self, data: dict, url: str) -> None:
        parsed_url = urlparse(url)
        file_name = f"{parsed_url.path.replace('/', '_')}.json".strip('_')
        file_path = os.path.join(self.save_folder, file_name)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {file_path}")

    def process_site(self) -> None:
        urls = self.fetch_sitemap()
        for url in urls:
            code_snippets = self.extract_python_code(url)
            if code_snippets:
                self.save_to_file({"url": url, "code_snippets": code_snippets}, url)


def start_scraper():
    scraper = FletCodeScraper(
        base_url='https://flet.dev/docs/', 
        sitemap_url='https://flet.dev/sitemap.xml', 
        save_folder='__extracted_code'
    )
    scraper.process_site()
    print("Web scraping completed successfully.")

if __name__ == "__main__":
    start_scraper()
