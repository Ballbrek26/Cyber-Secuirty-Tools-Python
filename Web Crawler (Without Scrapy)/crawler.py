import csv
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

base_url = "https://www.spacejam.com/1996/"
urls = [base_url]  # İşlenecek URL'ler
crawled_urls = set()  # Ziyaret edilen URL'ler (tekrarsız)
crawled_urls.add(base_url)  # Başlangıç URL'sini direkt ekliyoruz

while urls:
    current_url = urls.pop(0)  # FIFO (kuyruk mantığı)

    try:
        response = requests.get(current_url, timeout=10)
        response.raise_for_status()
    except:
        continue

    soup = BeautifulSoup(response.content, "html.parser")

    # Tüm linkleri bul ve işle
    for link in soup.select("a[href]"):
        raw_url = link['href']
        absolute_url = urljoin(current_url, raw_url)

        # URL filtreleme koşulları:
        if absolute_url.startswith(base_url) and absolute_url not in crawled_urls:
            urls.append(absolute_url)
            crawled_urls.add(absolute_url)
            print(f"Bulundu: {absolute_url}")

# CSV'ye yazma
with open('crawled.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Crawled URLs"])
    for url in crawled_urls:
        writer.writerow([url])

print(f"Toplam {len(crawled_urls)} URL kaydedildi.")