import pandas as pd
from datetime import datetime

# ダミーデータ作成
data = {
    "Date": pd.date_range(start="2025-01-01", periods=7, freq="D"),
    "Sales": [1200, 1500, 900, 1800, 2000, 1700, 2200],
    "Region": ["Tokyo", "Osaka", "Nagoya", "Tokyo", "Osaka", "Nagoya", "Tokyo"]
}

df = pd.DataFrame(data)

# 集計（地域ごとの合計）
summary = df.groupby("Region")["Sales"].sum().reset_index()

# Excel出力
filename = f"sales_report_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
with pd.ExcelWriter(filename, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Raw Data", index=False)
    summary.to_excel(writer, sheet_name="Summary", index=False)

print(f"[OK] Excel report saved: {filename}")

