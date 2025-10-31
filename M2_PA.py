import sqlite3
import os
import random
import string

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(data_dir, exist_ok=True)

def random_string(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_integer(min_val=0, max_val=100):
    return random.randint(min_val, max_val)

def random_float(min_val=0, max_val=100):
    return round(random.uniform(min_val, max_val), 2)

def create_mixed_db(db_name, num_rows=15):
    db_path = os.path.join(data_dir, db_name + ".db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create a generic table with mixed types
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS generic_table (
            name TEXT,
            age INTEGER,
            score FLOAT,
            city TEXT
        )
    """)

    # Insert random data
    for _ in range(num_rows):
        row = (
            random_string(),           # name
            random_integer(18, 65),    # age
            random_float(0, 100),      # score
            random_string(5)           # city
        )
        cursor.execute("INSERT INTO generic_table VALUES (?, ?, ?, ?)", row)

    conn.commit()
    conn.close()
    print(f"Created {db_path} with {num_rows} rows.")

# Generate 3 test DBs
for i in range(1, 4):
    create_mixed_db(f"mixed_db_{i}", num_rows=20)
