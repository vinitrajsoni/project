import json
import os

DB_FILE = "data/database.db"

def save_result(data):
    os.makedirs("data", exist_ok=True)
    all_data = load_all_results()
    all_data.append(data)
    with open(DB_FILE, "w") as f:
        json.dump(all_data, f, indent=2)

def load_all_results():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)
