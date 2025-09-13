import sqlite3
import os
from tabulate import tabulate

# Go one level up from this file's directory to find bon_rewards.db
db_path = os.path.join(os.path.dirname(__file__), "..", "bon_rewards.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def print_table(table_name: str):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    col_names = [description[0] for description in cursor.description]

    print(f"\n=== {table_name.upper()} ===")
    if rows:
        print(tabulate(rows, headers=col_names, tablefmt="fancy_grid"))
    else:
        print("(empty)")

print_table("users")
print_table("bills")
print_table("rewards")

conn.close()
