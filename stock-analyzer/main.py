import argparse
from datetime import datetime
from pathlib import Path

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# ─────────── 設定（Shoさん仕様）───────────
SMA_WINDOWS = [21, 75, 200]
BB_WINDOW = 20
BB_STD = 2.0
# ─────────────────────────────────────────

def calc_indicators(df: pd.DataFrame) -> pd.DataFrame:
    close = df["Close"]

    # 移動平均線
    for w in SMA_WINDOWS:
        df[f"SMA{w}"] = close.rolling(w).mean()

    # ボリンジャーバンド
    ma = close.rolling(BB_WINDOW).mean()
    std = close.rolling(BB_WINDOW).std(ddof=0)
    df["BB_Mid"] = ma
    df["BB_Upper"] = ma + BB_STD * std
    df["BB_Lower"] = ma - BB_STD * std

    return df

def plot_chart(df: pd.DataFrame, ticker: str, out_png: Path):
    plt.figure(figsize=(12, 7))
    plt.plot(df.index, df["Close"], label="Close")

    # 移動平均線
    for w in SMA_WINDOWS:
        plt.plot(df.index, df[f"SMA{w}"], label=f"SMA{w}")

    # ボリンジャーバンド
    plt.plot(df.index, df["BB_Mid"], label="BB Mid")
    plt.plot(df.index, df["BB_Upper"], label="BB Upper")
    plt.plot(df.index, df["BB_Lower"], label="BB Lower")

    plt.title(f"{ticker} with SMA & Bollinger Bands")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig(out_png, dpi=150)
    plt.close()

def main():
    parser = argparse.ArgumentParser(description="Stock Analyzer")
    parser.add_argument("--ticker", required=True, help="例: AAPL, MSFT, 7203.T")
    parser.add_argument("--period", default="1y", help="期間: 6mo, 1y, 5y, max")
    parser.add_argument("--interval", default="1d", help="足: 1d, 1h, 1wk")
    args = parser.parse_args()

    # データ取得
    df = yf.download(args.ticker, period=args.period, interval=args.interval, progress=False)
    if df.empty:
        raise SystemExit("データ取得に失敗しました。ティッカーや期間を見直してください。")

    # 指標計算
    df = calc_indicators(df)

    # 出力フォルダ
    out_dir = Path("reports")
    out_dir.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_png = out_dir / f"{args.ticker}_{args.period}_{args.interval}_{ts}.png"
    out_xlsx = out_dir / f"{args.ticker}_{args.period}_{args.interval}_{ts}.xlsx"

    # チャート保存
    plot_chart(df, args.ticker, out_png)

    # Excel保存
    with pd.ExcelWriter(out_xlsx, engine="openpyxl") as writer:
        df.to_excel(writer, index=True, sheet_name="data")

    print("=== Summary ===")
    print(f"Ticker : {args.ticker}")
    print(f"Period : {args.period}, Interval: {args.interval}")
    last_close = float(df["Close"].iloc[-1])
    print(f"Last Close : {last_close:.2f}")
    print(f"Saved : {out_png}, {out_xlsx}")

if __name__ == "__main__":
    main()

    import glob, os, time
from pathlib import Path

def cleanup_reports(directory: Path, keep: int = 5):
    files = []
    for pat in ("*.png", "*.xlsx"):
        files += list((directory).glob(pat))
    files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    for p in files[keep:]:
        try: p.unlink()
        except: pass

