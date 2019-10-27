/*
* @Author: Yan_Daojiang
* @Date:   2019-09-28 19:00:50
* @Last Modified by:   13738
* @Last Modified time: 2019-09-28 19:07:57
*/
# Write your MySQL query statement below
# 考查连接查询和聚集函数的的使用
SELECT Product.product_id, SUM(quantity) AS total_quantity
FROM Product JOIN Sales
ON Product.product_id = Sales.product_id
GROUP BY Product.product_id;