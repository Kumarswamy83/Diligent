from pathlib import Path
import sqlite3

import pandas as pd


DB_NAME = "ecommerce.db"
DATA_FILES = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "payments": "payments.csv",
}


CREATE_TABLE_QUERIES = {
    "customers": """
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            city TEXT,
            signup_date TEXT
        );
    """,
    "products": """
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price REAL
        );
    """,
    "orders": """
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            order_date TEXT,
            status TEXT
        );
    """,
    "order_items": """
        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id INTEGER PRIMARY KEY,
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            line_total REAL
        );
    """,
    "payments": """
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY,
            order_id INTEGER,
            amount REAL,
            method TEXT,
            payment_date TEXT
        );
    """,
}


def create_tables(connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()
    try:
        for query in CREATE_TABLE_QUERIES.values():
            cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()


def ingest_csv_to_sqlite(connection: sqlite3.Connection, table_name: str, csv_path: Path) -> None:
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, connection, if_exists="replace", index=False)


def main() -> None:
    project_root = Path(__file__).resolve().parent
    data_dir = project_root / "data"
    db_path = project_root / DB_NAME

    with sqlite3.connect(db_path) as conn:
        create_tables(conn)
        for table_name, filename in DATA_FILES.items():
            csv_path = data_dir / filename
            ingest_csv_to_sqlite(conn, table_name, csv_path)

    print("SQLite ingestion completed successfully.")


if __name__ == "__main__":
    main()


