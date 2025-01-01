CREATE DATABASE products_db;
USE products_db;
CREATE TABLE product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    is_recyclable BIT,
    is_low_fat BIT
);

INSERT INTO product (product_id, product_name, is_recyclable, is_low_fat)
VALUES
(1, 'Product A', 1, 1),
(2, 'Product B', 1, 0),
(3, 'Product C', 0, 1),
(4, 'Product D', 1, 1);

SELECT product_id, product_name
FROM product
WHERE is_recyclable = 1 AND is_low_fat = 1;
