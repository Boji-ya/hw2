import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import os

FILENAME = "data.txt" 


if not os.path.exists(FILENAME):
    print(f"Error: {FILENAME} not found.")
    print("Please make sure the file exists before running visualization.")
    exit()


categories = defaultdict(float)

with open(FILENAME, newline="", encoding="utf-8") as f:
    fieldnames = ['date', 'amount', 'category', 'note']
    reader = csv.DictReader(f, fieldnames=fieldnames)
    
    for row in reader:

        if not row["category"] or not row["amount"] or not row["date"]:
            continue
        try:

            short_date = row['date'][5:]
            
            new_key = f"{short_date} {row['category'].strip()}"
            

            categories[new_key] += float(row["amount"])
            
        except ValueError:
            continue

if not categories:
    print("No data found to plot!")
    exit()


labels = list(categories.keys())
sizes = list(categories.values())

colors = [
    '#F8BBD0', '#FFCCBC', '#FFE082', '#C8E6C9', '#B2DFDB', 
    '#B3E5FC', '#C5CAE9', '#E1BEE7', '#D7CCC8', '#CFD8DC'
]


explode = [0.03] * len(labels) 


plt.figure(figsize=(9, 7)) 


patches, texts, autotexts = plt.pie(
    sizes, 
    labels=labels, 
    colors=colors,    
    explode=explode,    
    autopct='%1.1f%%',  
    shadow=True,         
    startangle=140,
    textprops={'fontsize': 11} 
)

plt.title("Expense Distribution (Date & Category)", fontsize=16, fontweight='bold')
plt.axis("equal") # 確保是圓形


for text in autotexts:
    text.set_color('#333333')
    text.set_weight('bold')

print("圖表繪製成功")
plt.show()