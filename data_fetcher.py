import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def fetch_latest_data():
    """
    Hàm này sẽ lấy dòng dữ liệu mới nhất từ tệp JSON lưu trữ bởi signal bot.
    """
    try:
        with open("latest_data.json", "r", encoding="utf-8") as f:
            latest_data = json.load(f)

            # Lấy khóa cuối cùng (tức là dòng dữ liệu mới nhất)
            latest_key = list(latest_data.keys())[-1]
            latest_entry = latest_data[latest_key]

            print("Đã lấy dòng dữ liệu mới nhất từ bot signal:")
            #email = latest_entry.get('email', 'N/A')
            #payment_date = latest_entry.get('paymentDate', 'N/A')
            #expiry_date = latest_entry.get('expiryDate', 'N/A')
            #account_id = latest_entry.get('accountId', 'N/A')
            print(f"Email: {latest_entry.get('email', 'N/A')}, Payment Date: {latest_entry.get('paymentDate', 'N/A')}, Expiry Date: {latest_entry.get('expiryDate', 'N/A')}, Account ID: {latest_entry.get('accountId', 'N/A')}")
            return latest_entry
    except FileNotFoundError:
        print("Chưa có dữ liệu mới nào từ bot signal.")
    except json.JSONDecodeError:
        print("Lỗi khi đọc dữ liệu từ tệp JSON.")
