/*
* @Author: Yan_Daojiang
* @Date:   2019-10-01 22:50:37
* @Last Modified by:   13738
* @Last Modified time: 2019-10-01 22:51:26
*/
# Write your MySQL query statement below
SELECT customer_number
FROM orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;