CREATE TABLE expenses(
    id INTEGER PRIMARY KEY,
    date VARCHAR(50),
    category VARCHAR(50),
    item VARCHAR(50),
    price DECIMAL
);

INSERT INTO expenses(
    id,
    date,
    category,
    item,
    price
)
VALUES (1, '2026-08-08', 'Food', 'Carrot', 1.1),
       (2, '2026-02-03', 'Transport', 'Bus ticket', 2.30),
       (3, '2026-02-19', 'Entertainment', 'Cinema', 9.95),
       (4, '2026-03-07', 'Shopping', 'T-shirt', 18.40),
       (5, '2026-03-22', 'Food', 'Coffee', 3.65),
       (6, '2026-04-11', 'Sport', 'Football', 14.90),
       (7, '2026-05-02', 'Bills', 'Internet', 21.99),
       (8, '2026-05-22', 'Entertainment', 'Football ticket', 10.52),
       (9, '2026-06-26', 'Shopping', 'Backpack', 32.70),
       (10, '2026-07-06', 'Shopping', 'Headphones', 51.89);


-- Task 1
SELECT *
FROM expenses
WHERE category = 'Food';
-- Task 2
SELECT * 
FROM expenses
ORDER BY price DESC;
-- Task 3
SELECT *
FROM expenses 
WHERE price < 10
-- Task 4
SELECT *
FROM expenses
WHERE price > 20
-- Task 5
SELECT *
FROM expenses
WHERE category = 'Food'
ORDER BY price
-- Task 6
SELECT *
FROM expenses
WHERE category = 'Shopping'
ORDER BY price DESC
-- Task 7
SELECT * 
FROM expenses 
WHERE price > 10
ORDER BY price DESC
-- Task 8
SELECT * 
FROM expenses 
WHERE category = 'Food' or category = 'Sport'
-- Task 9
SELECT * 
FROM expenses 
WHERE category = 'Shopping' AND price > 20
ORDER BY price DESC
-- Agregate methods
-- Task 1
SELECT COUNT(*)
FROM expenses
-- Task 2
SELECT SUM(price)
FROM expenses
-- Task 3
SELECT MAX(price)
FROM expenses
-- Task 4
SELECT MIN(price)
FROM expenses
-- Task 5
SELECT AVG(price)
FROM expenses
-- Task 6
SELECT SUM(price)
FROM expenses
WHERE category = 'Shopping'
-- Task 7
SELECT COUNT(*)
FROM expenses
WHERE category = 'Food'
-- Task 8
SELECT MAX(price)
FROM expenses
WHERE category = 'Food'
-- Task 9
SELECT SUM(price)
FROM expenses
WHERE category IN('Food', 'Shopping')
-- Task 10
SELECT AVG(price)
FROM expenses 
WHERE category = 'Entertainment' and price < 20
-- Task 11
SELECT SUM(price)
FROM expenses
WHERE price BETWEEN 5 AND 30
-- Task 12
SELECT AVG(price)
FROM expenses
WHERE category = 'Shopping' OR category ='Food'
-- Advanced agregate methods GROUP BY, HAVING
-- Task 1
SELECT category, SUM(price)
FROM expenses 
GROUP BY category
-- Task 2
SELECT category, COUNT(*) AS count
FROM expenses 
GROUP BY category 
-- Task 3
SELECT category, AVG(price) AS average_price
FROM expenses
GROUP BY category
-- Task 4
SELECT category, SUM(price) AS sum
FROM expenses
GROUP BY category
HAVING sum > 30
-- Task 5
SELECT category, COUNT(*) AS count
FROM expenses
GROUP BY category
HAVING COUNT(*) > 1
-- Task 6
SELECT 
category,
COUNT(*) AS count,
AVG(price) AS average_price,
SUM(price) AS sum
FROM expenses
GROUP BY category
HAVING count > 1 AND average_price > 10