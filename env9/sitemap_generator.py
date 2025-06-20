import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

visited = set()

def is_internal(base_url, link):
    base_domain = urlparse(base_url).netloc
    link_domain = urlparse(link).netloc
    return base_domain == link_domain or link_domain == ""

def crawl(url, base_url):
    if url in visited:
        return []

    try:
        response = requests.get(url, timeout=10)
        if "text/html" not in response.headers.get("Content-Type", ""):
            return []

        visited.add(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        for tag in soup.find_all("a", href=True):
            href = urljoin(url, tag['href'])
            href = href.split('#')[0]
            href = href.rstrip('/')  
            if is_internal(base_url, href) and href not in visited:
                links.append(href)
        
        return links

    except requests.RequestException:
        return []

def generate_sitemap(start_url, max_pages=100):
    to_crawl = [start_url.rstrip('/')]
    base_url = start_url
    sitemap_links = []

    print(" Crawling started...\n")
    while to_crawl and len(visited) < max_pages:
        current = to_crawl.pop(0)
        print(f" Visiting: {current}")
        sitemap_links.append(current)
        new_links = crawl(current, base_url)
        to_crawl.extend(new_links)

    return sorted(set(sitemap_links))

def save_as_xml(urls, filename="sitemap.xml"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in urls:
            f.write("  <url>\n")
            f.write(f"    <loc>{url}</loc>\n")
            f.write(f"    <lastmod>{time.strftime('%Y-%m-%d')}</lastmod>\n")
            f.write("    <changefreq>weekly</changefreq>\n")
            f.write("    <priority>0.5</priority>\n")
            f.write("  </url>\n")
        f.write('</urlset>\n')
    print(f"\n Sitemap saved to {filename}")

def main():
    print(" Sitemap Generator\n")
    start_url = input("Enter the website URL (e.g., https://example.com): ").strip()

    if not start_url.startswith("http"):
        start_url = "http://" + start_url

    max_pages = input("Max pages to crawl (default 100): ").strip()
    max_pages = int(max_pages) if max_pages.isdigit() else 100

    sitemap_links = generate_sitemap(start_url, max_pages)
    print(f"\n Total pages found: {len(sitemap_links)}")
    save_as_xml(sitemap_links)

if __name__ == "__main__":
    main()
