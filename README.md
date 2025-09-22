# Python Automation Portfolio 🚀

このリポジトリには、Pythonを使った小さな自動化プロジェクトをまとめています。  
スクレイピングやExcelレポート生成などを通じて、データ処理のスキルを実践的に学べます。

This repository contains small automation projects written in Python.  
They demonstrate practical skills in data scraping, processing, and reporting.

---

## 📌 1. Quotes Scraper (スクレイピング / Web Scraping)
- サイト: [quotes.toscrape.com](https://quotes.toscrape.com)  
- 名言を取得してCSVに保存するPythonスクリプトです。  

This script scrapes famous quotes from [quotes.toscrape.com](https://quotes.toscrape.com)  
and saves them into a CSV file.

### ▶ 使い方 / Usage
```bash
# デフォルト3ページ分のスクレイピング / Default: scrape 3 pages
python scraper.py

# 5ページ分スクレイピング / Scrape 5 pages
python scraper.py 5

---

## 2. Excel Auto Report (pandas + openpyxl)

このスクリプトは、サンプルの売上データを作成し、地域ごとのサマリーを出力して、  
さらに棒グラフ付きの Excel レポートを自動生成します。📊

This script generates a sales dataset, creates a summary by region,  
and outputs an Excel file with both *Raw Data* and a bar chart in *Summary*.

### ▶ 使い方 / Usage
```bash
python report.py
```
