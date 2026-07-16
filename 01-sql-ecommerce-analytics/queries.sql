-- ============================================================
-- E-commerce Analytics — 15 analytical queries
-- Written for PostgreSQL. Also runnable in SQLite via ecommerce.db
-- (SQLite supports CTEs and window functions natively; a couple of
--  notes below flag PostgreSQL-only syntax where it differs).
-- ============================================================

-- 1. Total revenue and order count by month
SELECT
    DATE_TRUNC('month', o.order_date) AS month,
    COUNT(DISTINCT o.order_id)        AS total_orders,
    ROUND(SUM(oi.line_total), 2)      AS total_revenue
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.status = 'Completed'
GROUP BY 1
ORDER BY 1;

-- 2. Revenue by region
SELECT
    c.region,
    ROUND(SUM(oi.line_total), 2) AS revenue,
    COUNT(DISTINCT o.order_id)   AS orders
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.status = 'Completed'
GROUP BY c.region
ORDER BY revenue DESC;

-- 3. Top 10 products by revenue
SELECT
    p.product_name,
    p.category,
    ROUND(SUM(oi.line_total), 2) AS revenue,
    SUM(oi.quantity)             AS units_sold
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
JOIN orders o ON o.order_id = oi.order_id
WHERE o.status = 'Completed'
GROUP BY p.product_name, p.category
ORDER BY revenue DESC
LIMIT 10;

-- 4. Category share of total revenue
WITH category_revenue AS (
    SELECT p.category, SUM(oi.line_total) AS revenue
    FROM order_items oi
    JOIN products p ON p.product_id = oi.product_id
    JOIN orders o ON o.order_id = oi.order_id
    WHERE o.status = 'Completed'
    GROUP BY p.category
)
SELECT
    category,
    revenue,
    ROUND(100.0 * revenue / SUM(revenue) OVER (), 2) AS pct_of_total_revenue
FROM category_revenue
ORDER BY revenue DESC;

-- 5. Customer lifetime value (CLV), ranked
WITH clv AS (
    SELECT
        c.customer_id,
        c.customer_name,
        ROUND(SUM(oi.line_total), 2) AS lifetime_value,
        COUNT(DISTINCT o.order_id)   AS total_orders
    FROM customers c
    JOIN orders o ON o.customer_id = c.customer_id
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'Completed'
    GROUP BY c.customer_id, c.customer_name
)
SELECT *,
       RANK() OVER (ORDER BY lifetime_value DESC) AS clv_rank
FROM clv
ORDER BY clv_rank
LIMIT 20;

-- 6. Repeat purchase rate (% of customers with 2+ completed orders)
WITH order_counts AS (
    SELECT customer_id, COUNT(*) AS n_orders
    FROM orders
    WHERE status = 'Completed'
    GROUP BY customer_id
)
SELECT
    ROUND(100.0 * SUM(CASE WHEN n_orders > 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS repeat_purchase_rate_pct
FROM order_counts;

-- 7. Monthly cohort retention (signup-month cohorts, active by order month)
WITH cohorts AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', signup_date) AS cohort_month
    FROM customers
),
activity AS (
    SELECT
        o.customer_id,
        DATE_TRUNC('month', o.order_date) AS order_month
    FROM orders o
    WHERE o.status = 'Completed'
)
SELECT
    ch.cohort_month,
    a.order_month,
    COUNT(DISTINCT a.customer_id) AS active_customers
FROM cohorts ch
JOIN activity a ON a.customer_id = ch.customer_id
GROUP BY ch.cohort_month, a.order_month
ORDER BY ch.cohort_month, a.order_month;

-- 8. Running total of daily revenue (window function)
WITH daily AS (
    SELECT o.order_date, SUM(oi.line_total) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'Completed'
    GROUP BY o.order_date
)
SELECT
    order_date,
    revenue,
    SUM(revenue) OVER (ORDER BY order_date) AS running_total_revenue
FROM daily
ORDER BY order_date;

-- 9. Month-over-month revenue growth (%)
WITH monthly AS (
    SELECT DATE_TRUNC('month', o.order_date) AS month, SUM(oi.line_total) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'Completed'
    GROUP BY 1
)
SELECT
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_month_revenue,
    ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
          / NULLIF(LAG(revenue) OVER (ORDER BY month), 0), 2) AS mom_growth_pct
FROM monthly
ORDER BY month;

-- 10. Cancellation / return rate by category
SELECT
    p.category,
    COUNT(*) FILTER (WHERE o.status = 'Cancelled') AS cancelled,
    COUNT(*) FILTER (WHERE o.status = 'Returned')  AS returned,
    COUNT(*)                                       AS total_line_items,
    ROUND(100.0 * COUNT(*) FILTER (WHERE o.status IN ('Cancelled', 'Returned')) / COUNT(*), 2) AS problem_rate_pct
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
JOIN products p ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY problem_rate_pct DESC;
-- Note: COUNT(*) FILTER (...) is PostgreSQL syntax.
-- SQLite equivalent: SUM(CASE WHEN o.status = 'Cancelled' THEN 1 ELSE 0 END)

-- 11. Average order value (AOV) by customer region
SELECT
    c.region,
    ROUND(AVG(order_total), 2) AS avg_order_value
FROM (
    SELECT o.order_id, o.customer_id, SUM(oi.line_total) AS order_total
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'Completed'
    GROUP BY o.order_id, o.customer_id
) order_totals
JOIN customers c ON c.customer_id = order_totals.customer_id
GROUP BY c.region
ORDER BY avg_order_value DESC;

-- 12. Top 3 products per category (window function: ROW_NUMBER)
WITH ranked_products AS (
    SELECT
        p.category,
        p.product_name,
        SUM(oi.line_total) AS revenue,
        ROW_NUMBER() OVER (PARTITION BY p.category ORDER BY SUM(oi.line_total) DESC) AS rn
    FROM order_items oi
    JOIN products p ON p.product_id = oi.product_id
    JOIN orders o ON o.order_id = oi.order_id
    WHERE o.status = 'Completed'
    GROUP BY p.category, p.product_name
)
SELECT category, product_name, ROUND(revenue, 2) AS revenue
FROM ranked_products
WHERE rn <= 3
ORDER BY category, revenue DESC;

-- 13. Customers who haven't ordered in the last 90 days (churn risk)
WITH last_order AS (
    SELECT customer_id, MAX(order_date) AS last_order_date
    FROM orders
    WHERE status = 'Completed'
    GROUP BY customer_id
)
SELECT
    c.customer_id,
    c.customer_name,
    lo.last_order_date,
    (DATE '2023-12-31' - lo.last_order_date) AS days_since_last_order
FROM last_order lo
JOIN customers c ON c.customer_id = lo.customer_id
WHERE (DATE '2023-12-31' - lo.last_order_date) > 90
ORDER BY days_since_last_order DESC;

-- 14. New vs. returning customer revenue split, per month
WITH first_order AS (
    SELECT customer_id, MIN(DATE_TRUNC('month', order_date)) AS first_month
    FROM orders
    WHERE status = 'Completed'
    GROUP BY customer_id
),
monthly_orders AS (
    SELECT o.customer_id, DATE_TRUNC('month', o.order_date) AS month, SUM(oi.line_total) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'Completed'
    GROUP BY o.customer_id, DATE_TRUNC('month', o.order_date)
)
SELECT
    mo.month,
    ROUND(SUM(CASE WHEN mo.month = fo.first_month THEN mo.revenue ELSE 0 END), 2) AS new_customer_revenue,
    ROUND(SUM(CASE WHEN mo.month > fo.first_month THEN mo.revenue ELSE 0 END), 2) AS returning_customer_revenue
FROM monthly_orders mo
JOIN first_order fo ON fo.customer_id = mo.customer_id
GROUP BY mo.month
ORDER BY mo.month;

-- 15. Percentile ranking of customers by total spend (NTILE)
WITH spend AS (
    SELECT c.customer_id, c.customer_name, SUM(oi.line_total) AS total_spend
    FROM customers c
    JOIN orders o ON o.customer_id = c.customer_id
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'Completed'
    GROUP BY c.customer_id, c.customer_name
)
SELECT
    *,
    NTILE(4) OVER (ORDER BY total_spend DESC) AS spend_quartile  -- 1 = top 25% spenders
FROM spend
ORDER BY total_spend DESC;
