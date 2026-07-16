-- ============================================================
-- E-commerce Analytics — Schema (PostgreSQL)
-- Run this first, then load the CSVs in /data via \copy, e.g.:
--   \copy customers FROM 'data/customers.csv' DELIMITER ',' CSV HEADER;
--   \copy products   FROM 'data/products.csv'   DELIMITER ',' CSV HEADER;
--   \copy orders     FROM 'data/orders.csv'     DELIMITER ',' CSV HEADER;
--   \copy order_items FROM 'data/order_items.csv' DELIMITER ',' CSV HEADER;
-- ============================================================

DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id   INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email         TEXT,
    region        TEXT,
    signup_date   DATE
);

CREATE TABLE products (
    product_id   INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category     TEXT,
    unit_price   NUMERIC(10, 2)
);

CREATE TABLE orders (
    order_id    INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    order_date  DATE,
    status      TEXT CHECK (status IN ('Completed', 'Cancelled', 'Returned'))
);

CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id      INTEGER REFERENCES orders(order_id),
    product_id    INTEGER REFERENCES products(product_id),
    quantity      INTEGER,
    line_total    NUMERIC(10, 2)
);

CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_items_order ON order_items(order_id);
CREATE INDEX idx_items_product ON order_items(product_id);
