SELECT product_id,
      SUM(qty)
FROM orders
WHERE order_dt >= '2022-03-01'
  AND order_dt < '2022-04-01'
GROUP BY product_id;

-- or with the between function

SELECT product_id,
       SUM(qty)
FROM orders
WHERE order_dt BETWEEN '2022-03-01' AND '2022-03-31'
GROUP BY product_id;
