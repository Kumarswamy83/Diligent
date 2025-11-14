# ecom-synthetic-sqlite-project

## Project Overview
This project showcases a complete synthetic e-commerce analytics workflow designed through prompt engineering in Cursor. It covers data generation, ingestion into SQLite, and analytical SQL queries that join multiple tables to surface customer, order, and payment insights.

## Project Structure
```
ecom-synthetic-sqlite-project/
├── data/
├── generate_data.py
├── ingest_to_sqlite.py
├── query_join.sql
├── requirements.txt
├── README.md
└── .gitignore
```

## Dataset Details
- **customers.csv**: `customer_id`, `name`, `email`, `city`, `signup_date`
  - Customer master data including contact and signup information.
- **products.csv**: `product_id`, `name`, `category`, `price`
  - Catalog of available products and pricing.
- **orders.csv**: `order_id`, `customer_id`, `order_date`, `status`
  - High-level order records tied to customers.
- **order_items.csv**: `order_item_id`, `order_id`, `product_id`, `quantity`, `line_total`
  - Detailed line items linking orders to products with quantities and totals.
- **payments.csv**: `payment_id`, `order_id`, `amount`, `method`, `payment_date`
  - Financial transactions corresponding to orders and payment methods.

## How to Generate the Data
```
python generate_data.py
```

## How to Ingest into SQLite
```
python ingest_to_sqlite.py
```

## How to Run the SQL Query
Example using SQLite CLI:
```
sqlite3 ecommerce.db < query_join.sql
```

## Technologies Used
- Cursor IDE
- Python
- Pandas
- Faker
- SQLite

## Why This Project Demonstrates Prompt Engineering
Each deliverable—project scaffold, data generator, ingestion pipeline, and analytical SQL—was produced via precise, structured prompts that guided the Cursor environment to generate production-quality assets. This iterative prompt-driven approach highlights how disciplined prompt engineering can accelerate data engineering workflows while maintaining clarity, reproducibility, and professional standards.

---

This project was created as part of a hands-on assignment demonstrating professional prompt engineering and data workflow automation.

