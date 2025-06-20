import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys

def get_all_links(url):
    visited = set()
    links = set()

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f" Error fetching URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    for tag in soup.find_all('a', href=True):
        href = tag.get('href')
        full_url = urljoin(url, href)
        parsed = urlparse(full_url)

        if parsed.scheme in ['http', 'https']:
            norm_url = parsed.scheme + "://" + parsed.netloc + parsed.path
            if norm_url not in visited:
                visited.add(norm_url)
                links.add(norm_url)

    return sorted(links)

def save_links(links, filename="crawled_links.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for link in links:
            f.write(link + "\n")
    print(f" Links saved to {filename}")

def main():
    print(" Web Crawler – List All Links\n")
    url = input("Enter the URL to crawl: ").strip()

    if not url.startswith("http"):
        url = "http://" + url

    print("\n Crawling... Please wait...\n")
    links = get_all_links(url)

    if links:
        print(f" Found {len(links)} unique links:\n")
        for link in links:
            print(link)

        choice = input("\n Save links to a file? (yes/no): ").strip().lower()
        if choice == "yes":
            save_links(links)
    else:
        print(" No links found or unable to fetch page.")

if __name__ == "__main__":
    main()
