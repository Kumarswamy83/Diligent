import random
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import pandas as pd
from faker import Faker


NUM_CUSTOMERS = 2000
NUM_PRODUCTS = 500
NUM_ORDERS = 5000
MIN_ORDER_ITEMS = 1
MAX_ORDER_ITEMS = 5
MIN_ITEM_QUANTITY = 1
MAX_ITEM_QUANTITY = 5

CURRENCY_QUANTIZER = Decimal("0.01")


def quantize(amount: Decimal) -> Decimal:
    return amount.quantize(CURRENCY_QUANTIZER, rounding=ROUND_HALF_UP)


def generate_customers(fake: Faker, num_customers: int):
    customers = []
    signup_dates = {}

    for customer_id in range(1, num_customers + 1):
        signup_date = fake.date_between(start_date="-3y", end_date="today")
        customers.append(
            {
                "customer_id": customer_id,
                "name": fake.name(),
                "email": fake.unique.email(),
                "city": fake.city(),
                "signup_date": signup_date.isoformat(),
            }
        )
        signup_dates[customer_id] = signup_date

    fake.unique.clear()  # reset uniqueness constraints for subsequent generators
    return customers, signup_dates


def generate_products(fake: Faker, num_products: int):
    categories = [
        "Electronics",
        "Home",
        "Apparel",
        "Sports",
        "Beauty",
        "Books",
        "Toys",
        "Automotive",
        "Garden",
        "Grocery",
    ]
    product_types = ["Widget", "Gadget", "Device", "Accessory", "Set", "Kit", "Bundle"]

    products = []
    product_prices = {}

    for product_id in range(1, num_products + 1):
        category = random.choice(categories)
        base_name = random.choice(product_types)
        name = f"{fake.color_name()} {base_name}"

        price_cents = random.randint(500, 50000)
        price = quantize(Decimal(price_cents) / Decimal("100"))

        products.append(
            {
                "product_id": product_id,
                "name": name,
                "category": category,
                "price": float(price),
            }
        )
        product_prices[product_id] = price

    return products, product_prices


def generate_orders_and_related(
    fake: Faker,
    num_orders: int,
    customer_signup_dates,
    product_prices,
):
    statuses = ["pending", "processing", "shipped", "delivered", "returned"]
    status_weights = [0.1, 0.2, 0.35, 0.25, 0.1]
    payment_methods = [
        "credit_card",
        "paypal",
        "bank_transfer",
        "gift_card",
        "apple_pay",
        "google_pay",
    ]

    orders = []
    order_items = []
    payments = []

    order_item_id = 1
    customer_ids = list(customer_signup_dates.keys())
    product_ids = list(product_prices.keys())

    for order_id in range(1, num_orders + 1):
        customer_id = random.choice(customer_ids)
        signup_date = customer_signup_dates[customer_id]
        order_date = fake.date_between_dates(
            date_start=signup_date, date_end=date.today()
        )
        status = random.choices(statuses, weights=status_weights, k=1)[0]

        orders.append(
            {
                "order_id": order_id,
                "customer_id": customer_id,
                "order_date": order_date.isoformat(),
                "status": status,
            }
        )

        num_items = random.randint(MIN_ORDER_ITEMS, MAX_ORDER_ITEMS)
        order_total = Decimal("0.00")

        for _ in range(num_items):
            product_id = random.choice(product_ids)
            quantity = random.randint(MIN_ITEM_QUANTITY, MAX_ITEM_QUANTITY)
            unit_price = product_prices[product_id]
            line_total = quantize(unit_price * quantity)
            order_total += line_total

            order_items.append(
                {
                    "order_item_id": order_item_id,
                    "order_id": order_id,
                    "product_id": product_id,
                    "quantity": quantity,
                    "line_total": float(line_total),
                }
            )

            order_item_id += 1

        order_total = quantize(order_total)
        payment_date = order_date + timedelta(days=random.randint(0, 5))
        payments.append(
            {
                "payment_id": order_id,
                "order_id": order_id,
                "amount": float(order_total),
                "method": random.choice(payment_methods),
                "payment_date": payment_date.isoformat(),
            }
        )

    return orders, order_items, payments


def save_csv(dataframe: pd.DataFrame, path: Path):
    dataframe.to_csv(path, index=False)


def main():
    fake = Faker()
    random.seed(42)
    Faker.seed(42)

    data_dir = Path(__file__).resolve().parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    customers, customer_signup_dates = generate_customers(fake, NUM_CUSTOMERS)
    products, product_prices = generate_products(fake, NUM_PRODUCTS)
    orders, order_items, payments = generate_orders_and_related(
        fake,
        NUM_ORDERS,
        customer_signup_dates,
        product_prices,
    )

    save_csv(pd.DataFrame(customers), data_dir / "customers.csv")
    save_csv(pd.DataFrame(products), data_dir / "products.csv")
    save_csv(pd.DataFrame(orders), data_dir / "orders.csv")
    save_csv(pd.DataFrame(order_items), data_dir / "order_items.csv")
    save_csv(pd.DataFrame(payments), data_dir / "payments.csv")

    print(f"Generated datasets in {data_dir}")


if __name__ == "__main__":
    main()

