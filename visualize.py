import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import os

FILENAME = "expenses.csv"

if not os.path.exists(FILENAME):
    print("Error: expenses.csv not found.")
    print("Please make sure the file exists before running visualization.")
    exit()

# Read expense data
categories = defaultdict(float)

with open(FILENAME, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        categories[row["category"]] += float(row["amount"])

# Prepare data for pie chart
labels = categories.keys()
sizes = categories.values()

# Plot pie chart
plt.figure()
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Expense Distribution by Category")
plt.axis("equal")

plt.show()
