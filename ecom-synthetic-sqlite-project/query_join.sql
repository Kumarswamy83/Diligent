SELECT
    c.name AS customer_name,
    c.email AS customer_email,
    o.order_id,
    o.order_date,
    p.name AS product_name,
    oi.quantity,
    oi.line_total,
    pay.amount AS total_payment,
    pay.method AS payment_method
FROM orders AS o
JOIN customers AS c ON o.customer_id = c.customer_id
JOIN order_items AS oi ON o.order_id = oi.order_id
JOIN products AS p ON oi.product_id = p.product_id
JOIN payments AS pay ON o.order_id = pay.order_id
ORDER BY o.order_date DESC;


