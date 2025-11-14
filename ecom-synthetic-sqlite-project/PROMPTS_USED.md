1)You are a senior software engineer. Create a new project named `ecom-synthetic-sqlite-project`. Inside it, create a `data/` folder and these files with the exact content shown:

1. `requirements.txt` 
2. `.gitignore`
3. `README.md` (initial stub)



#step 2— Synthetic Dataset Generator Prompt

You are a senior data engineer.  
Create a new file named `generate_data.py` inside the `ecom-synthetic-sqlite-project` folder.  
Write Python code that generates 5 synthetic e-commerce CSV datasets and saves them into the `data/` folder:

Files:
- customers.csv
- products.csv
- orders.csv
- order_items.csv
- payments.csv

Data requirements:
- At least 2,000 customers  
- At least 500 products  
- At least 5,000 orders  
- Each order has 1–5 order items  
- Payments must match orders (amount = sum of line_totals)  
- All foreign keys valid  
- Use Faker for realistic values  
- Use pandas to save CSV files  

Columns per file:

customers: customer_id, name, email, city, signup_date  
products: product_id, name, category, price  
orders: order_id, customer_id, order_date, status  
order_items: order_item_id, order_id, product_id, quantity, line_total  
payments: payment_id, order_id, amount, method, payment_date  

After writing the file, respond with:  
**“generate_data.py created successfully — ready for Step 3.”**

---

#  Step 3 — SQLite Ingestion Script Prompt

You are a senior backend engineer.  
Create a new file named `ingest_to_sqlite.py`.

The script must:

1. Connect to SQLite and create `ecommerce.db`
2. Create tables:
   - customers(customer_id, name, email, city, signup_date)
   - products(product_id, name, category, price)
   - orders(order_id, customer_id, order_date, status)
   - order_items(order_item_id, order_id, product_id, quantity, line_total)
   - payments(payment_id, order_id, amount, method, payment_date)
3. Read CSVs from `data/` using pandas  
4. Insert into SQLite using `df.to_sql()`  
5. Print `"SQLite ingestion completed successfully."`

Respond with:  
**“ingest_to_sqlite.py created — ready to run.”**

---

# Step 4 — SQL Join Query Prompt

Create a file named `query_join.sql`.

Write an SQL query that joins:
- customers  
- orders  
- order_items  
- products  
- payments  

Output columns:
- customers.name  
- customers.email  
- orders.order_id  
- orders.order_date  
- products.name AS product_name  
- order_items.quantity  
- order_items.line_total  
- payments.amount AS total_payment  
- payments.method AS payment_method  

Sort by `orders.order_date` DESC.

Respond with:  
**“query_join.sql created — ready for Step 5.”**

---

# Step 5 — Final README Prompt

Rewrite the existing README.md into a complete, professional document including:

1. Project overview  
2. Folder structure  
3. Dataset details  
4. Commands to generate data  
5. Commands to ingest into SQLite  
6. How to run SQL join  
7. Technologies used  
8. Explanation of how prompt engineering was applied  

Respond with:  
**“README.md updated — ready for commit.”**

---

# ✔️ End of Prompts
This document contains the full prompt engineering workflow used to build the project.
