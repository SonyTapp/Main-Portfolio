
CREATE TABLE customers (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20)
);


CREATE TABLE inventory (
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    product_name VARCHAR(100),
    quantity INT,
    price DECIMAL(10, 2)
);


CREATE TABLE sales (
    sale_id INT IDENTITY(1,1) PRIMARY KEY,
    product_id INT,
    customer_id INT,
    quantity INT,
    sale_date DATETIME
);

INSERT INTO customers (first_name, last_name, email, phone) VALUES
('John', 'Doe', 'john.doe@example.com', '07442866499'),
('Jane', 'Smith', 'jane.smith@example.com', '0796442870');


INSERT INTO inventory (product_name, quantity, price) VALUES
('Laptop', 50, 999.99),
('Smartphone', 100, 799.99);


INSERT INTO sales (product_id, customer_id, sale_date, quantity) VALUES
(1, 1, '2024-06-22 14:00:00', 1),
(1, 2, '2024-06-22 15:30:00', 2);


SELECT
    customers.customer_id,
    customers.first_name,
    customers.last_name,
    SUM(sales.quantity * inventory.price) AS total
FROM customers

JOIN sales ON customers.customer_id = sales.customer_id
JOIN inventory ON sales.product_id = inventory.product_id
GROUP BY customers.customer_id, customers.first_name, customers.last_name;



SELECT
    customers.customer_id,
    customers.first_name,
    customers.last_name,
    inventory.product_name,
    SUM(sales.quantity) AS total_quantity,
    SUM(sales.quantity * inventory.price) AS total_amount
FROM customers

JOIN sales ON customers.customer_id = sales.customer_id
JOIN inventory ON sales.product_id = inventory.product_id
GROUP BY customers.customer_id, customers.first_name, customers.last_name, inventory.product_name;




-- Examples:


DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20)
);

SELECT * FROM customers


----------------------------------------------------------------------


INSERT INTO customers (first_name, last_name, email, phone) VALUES
('John', 'Doe', 'john.doe@example.com', '07442866499'),
('Jane', 'Smith', 'jane.smith@example.com', '0796442870');


--


SELECT SUM(quantity * price) AS total
FROM inventory;


----------------------------------------------------------------------


UPDATE customers
SET phone = '07123456789'
WHERE customer_id = 1;


--


-- RETRIEVES ALL CUSTOMERS WHO PURCHASED A LAPTOP

--





