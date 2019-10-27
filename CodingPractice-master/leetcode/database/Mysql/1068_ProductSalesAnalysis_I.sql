/*
* @Author: Yan_Daojiang
* @Date:   2019-09-28 19:06:46
* @Last Modified by:   13738
* @Last Modified time: 2019-09-28 19:06:58
*/

# Write your MySQL query statement below
#考查连接查询
SELECT Product.product_name, Sales.year, Sales.price
FROM Product INNER JOIN Sales
ON Product.product_id = Sales.product_id;
