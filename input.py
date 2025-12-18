import os
from datetime import datetime

def add_expense():
    print("=== 記帳系統 ===")
    
    # 1. 輸入日期
    default_date = datetime.now().strftime("%Y-%m-%d")
    date = input(f"日期 (Enter 自動設定為今天 {default_date}): ") or default_date
    
    # 2. 輸入金額 
    amount = input("金額 (請輸入純數字，例如 100): ")
    
    # 3. 輸入類別
    category = input("類別 (例如 Food, Transport): ")
    
    # 4. 備註
    note = input("備註 (可選): ")

    # 存檔格式：確保用逗號隔開，且順序固定
    # 格式：日期,金額,類別,備註
    with open('data.txt', mode='a', encoding='utf-8') as file: # mode a->append新資料 不會修改前面的資料
        line = f"{date},{amount},{category},{note}\n"
        file.write(line)
        
    print(f"已儲存：{line.strip()}")
    print("----------------------------")

if __name__ == "__main__":
    while True:
        add_expense()
        # 讓使用者決定要不要繼續，按 n 就離開
        if input("繼續輸入下一筆嗎? (y/n): ").lower() == 'n':
            print("程式結束，資料已存於 data.txt")
            break