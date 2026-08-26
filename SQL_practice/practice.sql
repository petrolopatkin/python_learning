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


CREATE TABLE purchases(
    id INTEGER PRIMARY KEY,
    date VARCHAR(50),
    category VARCHAR(50),
    item VARCHAR(50),
    quantity INTEGER,
    purchase_price DECIMAL
);

INSERT INTO purchases(
    id,
    date,
    category,
    item,
    quantity,
    purchase_price
)
VALUES
    (1, '2026-08-09', 'Food', 'Carrot', 3, 1.10),
    (2, '2026-08-10', 'Food', 'Coffee', 1, 3.65),
    (3, '2026-08-11', 'Shopping', 'T-shirt', 2, 18.40),
    (4, '2026-08-12', 'Shopping', 'Backpack', 4, 32.70),
    (5, '2026-08-13', 'Shopping', 'Headphones', 1, 51.89),
    (6, '2026-08-14', 'Sport', 'Football', 2, 14.90),
    (7, '2026-08-15', 'Entertainment', 'Cinema', 3, 9.95),
    (8, '2026-08-16', 'Entertainment', 'Football ticket', 0, 10.52),
    (9, '2026-08-17', 'Transport', 'Bus ticket', 5, 2.30),
    (10, '2026-08-18', 'Bills', 'Internet', 1, 21.99),
    (11, '2026-08-19', 'Food', 'Milk', 3, 1.50),
    (12, '2026-08-20', 'Shopping', 'Shoes', 2, 45.00);
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
-- day 2 of practicing lead and lag functions
-- Task 1
SELECT 
item,
category,
price,
LAG(price, 1, 0) OVER (PARTITION BY category
ORDER BY id) AS previous_price
FROM expenses
-- Task 2
SELECT 
item,
category,
price,
LEAD(price, 1, 0) OVER (PARTITION BY category
ORDER BY id) AS next_price
FROM expenses
-- Task 3
SELECT 
item,
category,
price,
LAG(price, 1, 0) OVER(
PARTITION BY category
ORDER BY id) as previous_price
FROM expenses
-- Task 4
WITH more_expensive AS(
SELECT item, 
category, 
price,
LAG(price, 1, 0) OVER(
PARTITION BY category
ORDER BY id DESC) as previous_price
FROM expenses)
SELECT 
item, 
category, 
price,
previous_price
FROM more_expensive
WHERE price > previous_price
-- first_value and last_value practice
-- Task 1
SELECT 
item,
category,
price,
FIRST_VALUE(price) OVER(
PARTITION BY category 
ORDER BY price DESC) as highest_price
FROM expenses
-- Task 2
SELECT 
item,
category,
price,
FIRST_VALUE(price) OVER(
PARTITION BY category 
ORDER BY price DESC) as highest_price,
FIRST_VALUE(price) OVER(
PARTITION BY category 
ORDER BY price DESC) - price as price_difference
FROM expenses
-- Task 3
SELECT 
item,
category,
price,
LAST_VALUE(price) OVER(
PARTITION BY category 
ORDER BY price DESC
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
) as lowest_price
FROM expenses
-- Task 4
SELECT 
item,
category,
price,
FIRST_VALUE(price) OVER(
PARTITION BY category 
ORDER BY price DESC) as highest_price,
LAST_VALUE(price) OVER(
PARTITION BY category 
ORDER BY price DESC
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
) as lowest_price
FROM expenses
-- NTH_value practice
-- Task 1
SELECT 
item, 
category,
price,
NTH_VALUE(price, 2)  OVER(
PARTITION BY category ORDER BY price 
ROWS BETWEEN UNBOUNDED PRECEDING 
AND UNBOUNDED FOLLOWING) AS second_highest_price
FROM expenses
-- Task 2
SELECT 
item, 
category,
price,
NTH_VALUE(price, 3) OVER(
PARTITION BY category ORDER BY price DESC
ROWS BETWEEN UNBOUNDED PRECEDING 
AND UNBOUNDED FOLLOWING) AS third_lowest_price
FROM expenses
-- Task 3
SELECT 
item, 
category,
price,
NTH_VALUE(price, 1) OVER(
PARTITION BY category ORDER BY price 
ROWS BETWEEN UNBOUNDED PRECEDING 
AND UNBOUNDED FOLLOWING) AS lowest_price,
NTH_VALUE(price, 3) OVER(
PARTITION BY category ORDER BY price DESC
ROWS BETWEEN UNBOUNDED PRECEDING 
AND UNBOUNDED FOLLOWING) AS third_lowest_price
FROM expenses
-- Task 4
SELECT 
item, 
category,
price,
NTH_VALUE(price, 1)  OVER(
PARTITION BY category ORDER BY price
ROWS BETWEEN UNBOUNDED PRECEDING 
AND UNBOUNDED FOLLOWING) AS cheapest_price,
NTH_VALUE(price, 2)  OVER(
PARTITION BY category ORDER BY price
ROWS BETWEEN UNBOUNDED PRECEDING 
AND UNBOUNDED FOLLOWING) AS second_cheapest_price
FROM expenses
-- practice
-- Task 1
SELECT 
item, 
category,
price,
NTH_VALUE(price, 2) OVER(
PARTITION BY category
ORDER BY price DESC
ROWS BETWEEN UNBOUNDED PRECEDING 
AND UNBOUNDED FOLLOWING) as second_cheapest_price
FROM expenses
-- Task 2
SELECT
item, 
category,
price,
NTH_VALUE(price, 3) OVER(
PARTITION BY category
ORDER BY price DESC
ROWS BETWEEN UNBOUNDED PRECEDING 
AND UNBOUNDED FOLLOWING) as third_highest_price
FROM expenses
-- Task 3
SELECT
item, 
category,
price,
LAST_VALUE(price) OVER(
PARTITION BY category
ORDER BY price DESC
ROWS BETWEEN UNBOUNDED PRECEDING 
AND UNBOUNDED FOLLOWING) as cheapest_price,
FIRST_VALUE(price) OVER(
PARTITION BY category
ORDER BY price DESC) as most_expensive_price
FROM expenses
-- NTILE practice
-- Task 1
SELECT 
id, 
item,
category,
price,
NTILE(4) OVER(ORDER BY price DESC)
FROM expenses
-- Task 2
SELECT 
id, 
item,
category,
price,
NTILE(3) OVER(
PARTITION BY category
ORDER BY price DESC)
FROM expenses
-- Task 3
SELECT 
id, 
item,
category,
price,
NTILE(3) OVER(
PARTITION BY category
ORDER BY price ASC)
FROM expenses
-- Task 4
WITH quater_price AS(
SELECT 
id, 
item,
category,
price,
NTILE(4) OVER(
PARTITION BY category
ORDER BY price DESC) as price_groups
FROM expenses
)
SELECT id, 
item,
category,
price
FROM quater_price
WHERE price_groups = 1
-- PERCENT_RANK practice
-- Task 1
SELECT 
item,
category,
price,
PERCENT_RANK() OVER(
ORDER BY price ASC) as percent_rank
FROM expenses
-- Task 2
SELECT 
item,
category,
price,
PERCENT_RANK() OVER(
PARTITION BY category
ORDER BY price ASC) as percent_rank
FROM expenses
-- Task 3
SELECT 
item,
category,
price,
PERCENT_RANK() OVER(
ORDER BY price DESC) as percent_rank
FROM expenses
-- Task 4
WITH highest_category AS(
SELECT 
item, 
category,
price,
NTILE(3) OVER(PARTITION BY category
ORDER BY price DESC) as highest_percentage,
PERCENT_RANK() OVER(
PARTITION BY category
ORDER BY price DESC) as percent_rank
FROM expenses)
SELECT 
item,
category,
price,
highest_percentage,
percent_rank
FROM highest_category
WHERE percent_rank <= 0.20
-- CUME_DIST practice
-- Task 1
SELECT 
item, 
category,
price,
CUME_DIST() OVER(ORDER BY price ASC)
FROM expenses
-- Task 2
SELECT 
item, 
category,
price,
CUME_DIST() OVER(
PARTITION BY category
ORDER BY price ASC)
FROM expenses
-- Task 3
SELECT 
item, 
category,
price,
CUME_DIST() OVER(
PARTITION BY category
ORDER BY price DESC)
FROM expenses
-- Task 4
SELECT
item, 
category,
price,
NTILE(4) OVER(
PARTITION BY category
ORDER BY price) as quater_price,
CUME_DIST() OVER(
PARTITION BY category
ORDER BY price) as cume_dist
FROM expenses
-- Task 5
SELECT 
item,
category,
price,
PERCENT_RANK() OVER(
PARTITION BY category
ORDER BY price) as percent_rank,
CUME_DIST() OVER(
PARTITION BY category
ORDER BY price) as cume_dist
FROM expenses
-- PERCENTILE_CONT and PERCENTILE_DISC pactice
SELECT
item,
category,
price,
PERCENTILE_CONT(price, 0.5)OVER(ORDER BY price) as median
FROM expenses
-- Task 2
SELECT
item,
category,
price,
PERCENTILE_CONT(price, 0.25)OVER(ORDER BY price),
PERCENTILE_CONT(price, 0.5)OVER(ORDER BY price),
PERCENTILE_CONT(price, 0.75)OVER(ORDER BY price)
FROM expenses
-- Task 3
SELECT
item,
category,
price,
PERCENTILE_CONT(price, 0.5)OVER(ORDER BY price) as median,
PERCENTILE_DISC(price, 0.5) OVER(ORDER BY price) as perc_disc
FROM expenses
-- Task 4
SELECT
item,
category,
price,
PERCENTILE_CONT(price, 0.5)OVER(
PARTITION BY category
ORDER BY price) as median
FROM expenses
-- Task 5
SELECT
item,
category,
price,
PERCENTILE_CONT(price, 0.9)OVER(
PARTITION BY category
ORDER BY price) as median
FROM expenses
-- Task 6
SELECT
item,
category,
price,
PERCENTILE_CONT(price, 0.25)OVER(
PARTITION BY category
ORDER BY price) as median,
PERCENTILE_CONT(price, 0.5)OVER(
PARTITION BY category
ORDER BY price),
PERCENTILE_CONT(price, 0.75)OVER(
PARTITION BY category
ORDER BY price),
PERCENTILE_CONT(price, 0.9)OVER(
PARTITION BY category
ORDER BY price)
FROM expenses
--
SELECT sqlite_version();
-- window fnctions practice
-- Task 1
SELECT
item, 
category,
price,
LAG(price, 1, 0) OVER(PARTITION BY category
ORDER BY id) as previous_price
FROM expenses
-- Task 2
WITH CTE1 AS(
SELECT
item, 
category,
price,
LAG(price, 1, 0) OVER(PARTITION BY category
ORDER BY id) as previous_price
FROM expenses)
SELECT 
item,
category,
price,
previous_price,
price - previous_price as price_difference
FROM CTE1
-- Task 3
SELECT
item,
category,
price,
FIRST_VALUE(price) OVER(PARTITION BY category
ORDER BY price) as cheapest_price
FROM expenses
-- Task 4
SELECT
item,
category,
price,
NTH_VALUE(price, 3) OVER(PARTITION BY category
ORDER BY price ASC
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
as third_price
FROM expenses
-- Task 5
SELECT
item,
category,
price,
NTILE(4) OVER(PARTITION BY category
ORDER BY price)
FROM expenses
-- Task 6
SELECT
item, 
category,
price,
PERCENT_RANK() OVER( PARTITION BY category
ORDER BY price ASC)
FROM expenses
-- Task 7
WITH CTE AS(
SELECT
item,
category,
price,
CUME_DIST() OVER(PARTITION BY category
ORDER BY price ASC) as cume_dist
FROM expenses)
SELECT
item, 
category,
price,
cume_dist
FROM CTE 
WHERE cume_dist > 0.5
-- Task 8
SELECT 
item,
category,
price,
FIRST_VALUE(price) OVER(PARTITION BY category
ORDER BY price) as cheapest_price,
LAG(price, 1, 0) OVER (
PARTITION BY category
ORDER BY id) as previous_price,
NTILE(3) OVER(ORDER BY price ASC) as price_group,
PERCENT_RANK() OVER(ORDER BY price) as rank_pice
FROM expenses
-- analytical functions practice day 2
-- Task 1
SELECT
item,
category,
price,
LAG(price, 1, 0) OVER(PARTITION BY category
ORDER BY price) as previous_price
FROM expenses
-- Task 2
SELECT
item,
category,
price,
FIRST_VALUE(price) OVER(PARTITION BY category
ORDER BY price ASC) as cheapest_price
FROM expenses
-- TAsk 3
SELECT 
item,
category,
price,
NTILE(4) OVER(ORDER BY price) as price_groups
FROM expenses
-- Task 4
WITH CTE AS(
SELECT
item,
category,
price,
CUME_DIST() OVER(PARTITION BY category
ORDER BY price ASC) as cume_dist
FROM expenses)
SELECT 
item,
category,
price,
cume_dist
FROM CTE 
WHERE cume_dist > 0.3
-- LEAD practice
SELECT 
item,
category,
price,
LEAD(price, 1, 0) OVER(PARTITION BY category
ORDER BY id) as next_price
FROM expenses
-- Task 2
WITH CTE AS(
SELECT 
item,
category,
price,
LEAD(price, 1, 0) OVER(PARTITION BY category
ORDER BY id) as next_price
FROM expenses)
SELECT
item,
category,
price,
next_price,
price - next_price as price_difference
FROM CTE 
-- Task 3
WITH CTE AS(
SELECT 
item,
category,
price,
LEAD(price, 1, 0) OVER(PARTITION BY category
ORDER BY price ASC) as next_price
FROM expenses)
SELECT
item,
category,
price,
next_price,
price - next_price as price_difference
FROM CTE 
-- Task 4
WITH CTE AS(
SELECT
item,
category,
price,
LAG(price, 1, 0) OVER(
PARTITION BY category
ORDER BY id) as previous_price,
LEAD(price, 1, 0) OVER(
PARTITION BY category
ORDER BY id) as next_price
FROM expenses)
SELECT
item,
category,
price,
previous_price,
next_price,
price - previous_price as price_difference_from_previous,
price - next_price as price_difference_from_next
FROM CTE 
-- Case method practice
-- Task 1
SELECT
item,
category,
price,
CASE 
    WHEN price < 10 THEN 'cheap'
    WHEN price BETWEEN 10 AND 30 THEN 'medium'
    WHEN price > 30 THEN 'expensive'
END AS price_categories
FROM expenses
ORDER BY price
-- Task 2
SELECT
item,
category,
price,
CASE 
    WHEN price < 5 THEN 'group1'
    WHEN price BETWEEN 5 AND 10 THEN 'group2'
    WHEN price BETWEEN 10 AND 30 THEN 'group3'
    WHEN price > 30 THEN 'group4'
END as groupss
FROM expenses
ORDER BY price
-- Task 3
SELECT
item,
category,
price,
CASE 
    WHEN price < 5 THEN 'group1'
    WHEN price BETWEEN 5 AND 10 THEN 'group2'
    WHEN price BETWEEN 10 AND 30 THEN 'group3'
    WHEN price > 30 THEN 'group4'
END as groupss
FROM expenses
GROUP BY category
ORDER BY price
-- case practice + window functions
-- Task 1
WITH CTE AS(
SELECT 
item,
category,
price,
RANK() OVER(PARTITION BY category
ORDER BY price) as price_rank
FROM expenses)
SELECT
item,
category,
price,
price_rank,
CASE 
    WHEN price_rank = 1 THEN 'Cheapest'
    WHEN price_rank = 2 THEN 'Second cheapest'
    WHEN price_rank = 3 THEN 'Third cheapest'
    ELSE 'Other'
    END as ranks
FROM CTE 
-- Task 2
WITH CTE AS(
SELECT
item,
category,
price,
AVG(price) OVER(PARTITION BY category
) as avg_price
FROM expenses) 
SELECT 
item,
category,
price,
avg_price,
CASE 
    WHEN price/avg_price < 0.8 THEN 'Much cheaper'
    WHEN price/avg_price < 0.5 THEN 'Cheaper'
    WHEN price/avg_price > 0.5 THEN 'More expensive'
    WHEN price/avg_price = 0.5 THEN 'Average'
    END AS price_group
FROM CTE
-- Exists/Not exists practice
-- Task 1
SELECT
item,
category,
price
FROM expenses
WHERE EXISTS(
SELECT 1
FROM purchases
WHERE purchases.item = expenses.item
AND purchases.quantity >= 1)
ORDER BY price
-- Task 2
SELECT
item,
category,
price
FROM expenses
WHERE NOT EXISTS(
SELECT 1
FROM purchases
WHERE purchases.item = expenses.item
AND purchases.quantity = 0)
ORDER BY price
-- exists/not exists practice
-- Task 1
SELECT item,
category,
price
FROM expenses
WHERE EXISTS(
SELECT 1
FROM purchases
WHERE purchases.item = expenses.item
AND purchases quantity >= 3)
-- Task 2
SELECT item,
category,
price
FROM expenses
WHERE NOT EXISTS(
SELECT 1 
FROM purchases
WHERE purchases.item = expenses.item AND
expenses.item IN purchases)
-- Task 3
SELECT item,
category,
price
FROM expenses
WHERE EXISTS(
SELECT 1
FROM purchases
WHERE purchases.item = expenses.item AND 
purchases.quantity >= 2 AND
purchases.purchase_price > 100)
-- Task 4
SELECT item,
category,
price
FROM expenses
WHERE NOT EXISTS(
SELECT 1 
FROM purchases
WHERE purchases.item = expenses.item AND
purchases.category = expenses.category AND
purchases.quantity > 0)
-- Task 5
SELECT *
FROM expenses
WHERE category IN(
SELECT category
FROM purchases)
-- Task 6
SELECT category
FROM purchases
WHERE category NOT IN(
SELECT category
FROM expenses
)
