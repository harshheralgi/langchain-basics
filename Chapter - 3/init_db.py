import sqlite3

conn = sqlite3.connect("SalesDB/sales.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        product_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        total REAL NOT NULL
    )
""")

cursor.execute("""
    INSERT INTO orders(customer_name, product_name, quantity, price, total)
    VALUES
    ('John Doe', 'Laptop', 1, 1200.00, 1200.00),
    ('Jane Smith', 'Mouse', 2, 25.00, 50.00),
    ('Bob Johnson', 'Keyboard', 1, 75.00, 75.00),
    ('Alice Williams', 'Monitor', 2, 300.00, 600.00),
    ('Charlie Brown', 'Webcam', 1, 50.00, 50.00)
""")

conn.commit()
conn.close()