# Python Automation Portfolio 🚀

このリポジトリには、Pythonを使った自動化プロジェクトをまとめています。  
スクレイピングやExcelレポート生成などを通じて、データ処理のスキルを実践的に学べます。

This repository contains small automation projects written in Python.  
They demonstrate practical skills in data scraping, processing, and reporting.

---

## 1. Quotes Scraper (スクレイピング / Web Scraping)

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
```
---

## 2. Excel Auto Report (pandas + openpyxl)

このスクリプトは、サンプルの売上データを作成し、地域ごとのサマリーを出力して、
さらに棒グラフ付きの Excel レポートを自動生成します。📊

This script generates a sales dataset, creates a summary by region,
and outputs an Excel file with both *Raw Data* and a bar chart in *Summary*.

### 使い方 / Usage
```bash
python3 report.py
```

## 2. Stock Analyzer (株価分析)

- API: [yfinance](https://github.com/ranaroussi/yfinance) を利用して株価を取得
- 分析: 移動平均線 (SMA) とボリンジャーバンドを可視化
- 出力: Excel + PNG グラフ

### サンプル出力

#### Apple 株価 (AAPL)
![AAPL sample](docs/images/aapl_sampl.png)

#### トヨタ自動車 (7203.T)
![Toyota sample](docs/images/aapl_sampl2.png)





