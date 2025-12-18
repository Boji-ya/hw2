import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import os

FILENAME = "data.txt" 

# 檢查檔案是否存在
if not os.path.exists(FILENAME):
    print(f"Error: {FILENAME} not found.")
    print("Please make sure the file exists before running visualization.")
    exit()

# Read expense data
categories = defaultdict(float)

with open(FILENAME, newline="", encoding="utf-8") as f:
    fieldnames = ['date', 'amount', 'category', 'note']
    reader = csv.DictReader(f, fieldnames=fieldnames)
    
    for row in reader:
        # 防呆機制
        if not row["category"] or not row["amount"] or not row["date"]:
            continue
        try:
            # === 關鍵修改：組合「短日期」跟「類別」===
            # row['date'][5:] 會把 "2025-12-19" 變成 "12-19" (比較不佔空間)
            short_date = row['date'][5:]
            
            # 組合新的 Key，例如："12-19 Food"
            new_key = f"{short_date} {row['category'].strip()}"
            
            # 加總到新的 Key 下
            categories[new_key] += float(row["amount"])
            
        except ValueError:
            continue

# Check if there is data
if not categories:
    print("No data found to plot!")
    exit()

# Prepare data for pie chart
labels = list(categories.keys())
sizes = list(categories.values())

# === 🎨 美化設定區 ===

# 1. 絕美淡粉彩配色 (莫蘭迪色系)
colors = [
    '#F8BBD0', '#FFCCBC', '#FFE082', '#C8E6C9', '#B2DFDB', 
    '#B3E5FC', '#C5CAE9', '#E1BEE7', '#D7CCC8', '#CFD8DC'
]

# 2. 炸開效果 (讓每一塊之間有一點點縫隙，看起來更有質感)
explode = [0.03] * len(labels) 

# 設定圖表大小
plt.figure(figsize=(9, 7)) 

# 3. 畫圖 (套用 colors 和 explode)
patches, texts, autotexts = plt.pie(
    sizes, 
    labels=labels, 
    colors=colors,       # ★ 套用新顏色
    explode=explode,     # ★ 套用炸開效果
    autopct='%1.1f%%',   # 顯示百分比
    shadow=True,         # 加入陰影立體感
    startangle=140,
    textprops={'fontsize': 11} # 調整文字大小
)

# 設定標題
plt.title("Expense Distribution (Date & Category)", fontsize=16, fontweight='bold')
plt.axis("equal") # 確保是圓形

# 調整百分比文字的顏色 (白色在深色區塊比較明顯，黑色在淺色比較明顯，這裡統一用深灰色)
for text in autotexts:
    text.set_color('#333333')
    text.set_weight('bold')

print("📊 圖表繪製成功！")
plt.show()