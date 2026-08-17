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

CREATE TABLE categories(
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    description VARCHAR(100)
);
INSERT INTO categories(
    id,
    name,
    description
)
VALUES (1, 'Food', 'Something to eat or to drink'),
       (2, 'Shopping', 'Clothes or accessories'),
       (3, 'Transport', 'Tickets for any kind of transport'),
       (4, 'Entertainment', 'Any kind of recreation'),
       (5, 'Sport', 'Sport objects and products'),
       (6, 'Bills', 'Money for goods and services');

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
-- new practice with advadnced aggregate methods
-- task 1(easy)
SELECT category, COUNT(*), SUM(price)
FROM expenses
GROUP BY category
-- task 2(easy)
SELECT category
FROM expenses
GROUP BY category
HAVING SUM(price) > 30
-- task 3(medium)
SELECT category, 
COUNT(*) as count,
AVG(price) as average_price,
SUM(price) as sum
FROM expenses
GROUP BY category
HAVING COUNT(*) > 1
-- task 4(medium)
SELECT category
FROM expenses
GROUP BY category
HAVING AVG(price) > 10
-- task 5(hard)
SELECT category,
COUNT(*) as count,
SUM(price) as sum,
AVG(price) as average_price
FROM expenses
GROUP BY category
HAVING COUNT(*) > 1 
AND SUM(price) > 20
AND AVG(price) > 5
-- task 6(hard)
SELECT category,
COUNT(*) as count,
MIN(price) as min_price,
MAX(price) as max_price,
AVG(price) as average_price,
SUM(price) as sum
FROM expenses
GROUP BY category
HAVING COUNT(*) > 1
ORDER BY SUM(price) DESC
--
SELECT *
FROM categories
-- join to of my tables
SELECT 
ex.date,
c.id,
c.name as category,
ex.item,
ex.price
FROM expenses ex
JOIN categories c
    ON ex.category = c.name
-- Task1
SELECT 
ex.item,
ex.price,
c.name as category
FROM expenses ex
JOIN categories c
    ON ex.category = c.name
-- Task 2
SELECT *
FROM expenses ex
JOIN categories c
    ON ex.category = c.name
WHERE category == 'Food'
-- Task 3
SELECT 
c.name as category,
COUNT(*) as count,
SUM(price) as sum
FROM expenses ex
JOIN categories c
    ON ex.category = c.name
GROUP BY category
-- Task 4
SELECT *
FROM expenses ex
JOIN categories c
    ON ex.category = c.name
GROUP BY category
HAVING SUM(price) > 20
-- Task 5
SELECT 
c.name as category,
AVG(price) as average_price,
MAX(price) as max_price,
MIN(price) as min_price
FROM expenses ex
JOIN categories c
    ON ex.category = c.name
GROUP BY category
ORDER BY price DESC
-- Task 6
SELECT 
ex.date,
c.id,
c.name as category,
ex.item,
ex.price
FROM expenses ex
LEFT JOIN categories c
    ON ex.category = c.name
GROUP BY category
HAVING 
COUNT(*) > 1 
AND SUM(price) > 30
AND AVG(price) > 10
-- Task 7
SELECT 
c.name as category,
COUNT(*) as count,
SUM(price) sum
FROM expenses ex
LEFT JOIN categories c
    ON ex.category = c.name
GROUP BY category
-- Task 8
SELECT 
ex.date,
c.id,
c.name as category,
ex.item,
ex.price
FROM expenses ex
LEFT JOIN categories c
    ON ex.category = c.name
GROUP BY category
ORDER BY price DESC
-- subquaries
-- Task 1
SELECT *
FROM expenses
WHERE price > (SELECT AVG(price) FROM expenses) 
-- Task 2
SELECT *  
FROM expenses
WHERE price = 
(SELECT MAX(price) AS max_price FROM expenses)
-- Task 3
SELECT *
FROM expenses 
GROUP BY category
HAVING SUM(price) > (SELECT AVG(price) FROM expenses) 
-- Task 4
SELECT *
FROM expenses
WHERE category IN
(SELECT name
FROM categories
WHERE name is 'Food')
-- Task 5
SELECT item,
category,
price
FROM expenses 
WHERE price > (SELECT AVG(price) as avg
FROM expenses 
WHERE category = expenses.category)
-- day 2 of practicing subqueries
-- Task 1 
SELECT *
FROM expenses
WHERE price < 
(SELECT AVG(price)
 FROM expenses) 
 -- Task 2
SELECT *
FROM expenses
WHERE price = (
SELECT MAX(price) as max
FROM expenses)
-- Task 3
SELECT *
FROM expenses
WHERE price = (
SELECT MIN(price) as min
FROM expenses)
-- Task 4
SELECT *
FROM expenses
WHERE price IS NOT (
SELECT MAX(price) as max
FROM expenses)
-- Task 5
SELECT *
FROM expenses
WHERE price > (
SELECT MIN(price) as min
FROM expenses)
-- Task 6
SELECT *
FROM expenses
WHERE price BETWEEN (
SELECT AVG(price) as avg
FROM expenses) 
AND (
SELECT MAX(price) as max
FROM expenses) 
-- correlated queries
SELECT item,
category,
price
FROM expenses as e
WHERE price > (SELECT AVG(price)
FROM expenses
WHERE category = e.category)
-- Task 1
SELECT item,
category,
price
FROM expenses as e
WHERE price < (SELECT AVG(price)
FROM expenses
WHERE category = e.category)
-- Task 2
SELECT item,
category,
price
FROM expenses as e
WHERE price = (SELECT MAX(price)
FROM expenses
WHERE category = e.category)
-- Task 3
SELECT item,
category, 
price,
(SELECT AVG(price)
FROM expenses
WHERE category = e.category) 
as avg_price
FROM expenses as e
-- correlated subqueries day 2
-- Task 1
SELECT item,
category, 
price
FROM expenses as e
WHERE price > 
(SELECT AVG(price)
FROM expenses
WHERE category = e.category)
-- Task 2
SELECT item,
category, 
price
FROM expenses as e
WHERE price <
(SELECT AVG(price)
FROM expenses
WHERE category = e.category)
-- Task 3
SELECT item,
category,
price
FROM expenses as e
WHERE price = 
(SELECT MIN(price)
FROM expenses
WHERE category = e.category)
-- Task 4
SELECT item,
category,
price
FROM expenses as e
WHERE price > 
(SELECT AVG(price)
FROM expenses)
AND price < 
(SELECT AVG(price)
FROM expenses
WHERE category = e.category)
-- window functions 
-- Task 1
SELECT item, 
category,
price,
AVG(price) OVER(
PARTITION BY category) as category_avg
FROM expenses
-- Task 2
SELECT item, 
category,
price,
SUM(price) OVER(
PARTITION BY category) as category_sum
FROM expenses
-- Task 3
SELECT item,
category,
price,
ROW_NUMBER() OVER(
PARTITION BY category
ORDER BY price ASC) as row_num
FROM expenses
-- Task 4
SELECT item, 
category,
price,
RANK() OVER(
PARTITION BY category
ORDER BY price DESC) as rank_num
FROM expenses
-- Task 5
SELECT item, 
category,
price,
DENSE_RANK() OVER(
PARTITION BY category
ORDER BY price DESC) as rank_num
FROM expenses
-- Task 6
SELECT item,
category,
price,
AVG(price) OVER(
PARTITION BY category) as avg_category,
SUM(price) OVER(
PARTITION BY category) as sum_category,
RANK() OVER(
PARTITION BY category
ORDER BY PRICE DESC) as rank_num
FROM expenses
-- window functions + subqueries
-- Task
SELECT *
FROM
(SELECT item,
category,
price,
RANK() OVER(
PARTITION BY category
ORDER BY price DESC) as rank_num
FROM expenses)
WHERE rank_num == 1 
-- CTE practice
-- Task 1
WITH CTE1 AS
(SELECT 
item,
category,
price
FROM expenses
)
SELECT *
FROM CTE1
-- Task 2
WITH CTE1 AS
(SELECT 
item,
category,
price
FROM expenses
WHERE price > 10
)
SELECT *
FROM CTE1
-- Task 3 CTE + AVG
WITH CTE1 AS
(SELECT 
category,
AVG(price) avg_price
FROM expenses e
WHERE category = e.category
GROUP BY category
)
SELECT *
FROM CTE1
-- Task  4 CTE + Window function
WITH CTE1 AS
(SELECT 
item,
category,
price,
RANK() OVER(
PARTITION BY category
ORDER BY price DESC) as rank_num
FROM expenses
)
SELECT *
FROM CTE1
WHERE rank_num = 1
-- Task 5 CTE + Window function + filtration
WITH CTE1 AS
(SELECT 
item,
category,
price,
RANK() OVER(
PARTITION BY category
ORDER BY price DESC) as rank_num
FROM expenses
)
SELECT *
FROM CTE1
WHERE rank_num <= 2
-- Task 6
WITH CTE1 AS
(SELECT category,
AVG(price) AS avg_price
FROM expenses
GROUP BY category
),
CTE2 AS
(SELECT item,
category,
price
FROM expenses
)
SELECT 
c2.item,
c2.category,
c2.price,
c1.avg_price
FROM CTE1 c1
JOIN CTE2 c2
    ON c1.category = c2.category
WHERE c2.price > c1.avg_price
-- Lead and Lag window functions
-- Task 1
SELECT 
id,
item, 
category,
price,
LAG(price, 1, 0) OVER(PARTITION BY category 
ORDER BY id DESC) as previous_price
FROM expenses
-- Task 2
SELECT 
item, 
category,
price,
LAG(price, 1, 0) OVER(PARTITION BY category 
ORDER BY price DESC) as price_difference
FROM expenses
-- Task 3
SELECT 
id,
item, 
price,
LEAD(price, 1, 0) OVER(PARTITION BY category
ORDER BY id DESC) as next_price
FROM expenses
-- Task 4
WITH expenses_with_previous AS(
SELECT
    item,
    category,
    price,
    LAG(price, 1, 0) OVER(
    PARTITION BY category
    ORDER BY id) AS previous_price
FROM expenses)
SELECT
    item, 
    category,
    price,
    previous_price,
    price > previous_price AS more_expensive_than_previous
FROM expenses_with_previous
-- Task 5
WITH expenses_with_previous AS(
SELECT
    item,
    category,
    price,
    LAG(price, 1, 0) OVER(
    PARTITION BY category
    ORDER BY id) AS previous_price
FROM expenses
)
SELECT
    item, 
    category,
    price,
    previous_price
FROM expenses_with_previous
WHERE price > previous_price