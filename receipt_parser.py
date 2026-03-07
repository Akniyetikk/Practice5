import re
import json

file_path = "/Users/u_kozhakova/Downloads/raw.txt"

def parse_receipt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    product_pattern = re.compile(r'\d+\.\n(.*?)\n\d+,\d{3} x', re.DOTALL)
    price_pattern = re.compile(r'Стоимость\n([\d\s]+,\d{2})')
    date_time_pattern = re.compile(r'Время: (\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})')
    total_pattern = re.compile(r'ИТОГО:\n([\d\s]+,\d{2})')
    payment_pattern = re.compile(r'([А-Яа-я\s]+):\n[\d\s]+,\d{2}\nИТОГО:')

    products_raw = product_pattern.findall(content)
    products = [p.replace('\n', ' ').strip() for p in products_raw]

    prices_raw = price_pattern.findall(content)
    prices = [float(p.replace(' ', '').replace(',', '.').strip()) for p in prices_raw]

    total_match = total_pattern.search(content)
    total = float(total_match.group(1).replace(' ', '').replace(',', '.').strip()) if total_match else 0.0
    
    date_match = date_time_pattern.search(content)
    date_time = date_match.group(1) if date_match else "Not found"
    
    pay_match = payment_pattern.search(content)
    payment_method = pay_match.group(1).strip() if pay_match else "Unknown"

    items = [{"product_name": n, "price": p} for n, p in zip(products, prices)]

    return {
        "store": "EUROPHARMA Астана",
        "date_time": date_time,
        "payment_method": payment_method,
        "items": items,
        "calculated_sum": sum(prices),
        "total_on_receipt": total
    }

if __name__ == "__main__":
    try:
        data = parse_receipt(file_path)
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
