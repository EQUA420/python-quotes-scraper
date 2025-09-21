import time
import csv
import sys
from typing import List, Dict
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X) Python-Portfolio Scraper"
}

def fetch_page(url: str) -> BeautifulSoup:
    r = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()
    return BeautifulSoup(r.text, "lxml")

def parse_quotes(soup: BeautifulSoup) -> List[Dict[str, str]]:
    data = []
    for q in soup.select(".quote"):
        text = q.select_one(".text").get_text(strip=True)
        author = q.select_one(".author").get_text(strip=True)
        tags = ",".join(t.get_text(strip=True) for t in q.select(".tags a.tag"))
        data.append({"text": text, "author": author, "tags": tags})
    return data

def find_next_page(soup: BeautifulSoup) -> str | None:
    nxt = soup.select_one("li.next a")
    return (BASE_URL + nxt["href"]) if nxt else None

def scrape(max_pages: int = 3) -> List[Dict[str, str]]:
    url = BASE_URL
    all_rows: List[Dict[str, str]] = []
    page = 1
    while url and page <= max_pages:
        print(f"[INFO] Fetching: {url}")
        soup = fetch_page(url)
        all_rows.extend(parse_quotes(soup))
        url = find_next_page(soup)
        page += 1
        time.sleep(1)
    return all_rows

def save_csv(rows: List[Dict[str, str]], path: str = "quotes.csv") -> None:
    if not rows:
        print("[WARN] No data collected.")
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"[OK] Saved {len(rows)} rows to {path}")

if __name__ == "__main__":
    max_pages = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    data = scrape(max_pages=max_pages)
    save_csv(data)


