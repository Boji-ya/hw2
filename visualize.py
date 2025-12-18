import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import os

FILENAME = "data.txt" 

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
        # 防呆：避免讀到空行導致報錯
        if not row["category"] or not row["amount"]:
            continue
            
        # 統計金額
        try:
            categories[row["category"]] += float(row["amount"])
        except ValueError:
            continue # 如果金額不是數字就跳過

# Check if there is data
if not categories:
    print("No data found to plot!")
    exit()

# Prepare data for pie chart
labels = categories.keys()
sizes = categories.values()

# Plot pie chart
plt.figure(figsize=(8, 6)) # 加大一點圖表比較好看
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Expense Distribution by Category")
plt.axis("equal")

plt.show()