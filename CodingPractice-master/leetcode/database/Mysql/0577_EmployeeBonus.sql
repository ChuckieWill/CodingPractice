/*
* @Author: Yan_Daojiang
* @Date:   2019-10-01 23:31:43
* @Last Modified by:   13738
* @Last Modified time: 2019-10-01 23:31:55
*/
# Write your MySQL query statement below
# 注意连接条件和过滤条件
SELECT name, bonus
FROM Employee LEFT OUTER JOIN Bonus
ON Employee.empId = bonus.empID
WHERE bonus is NULL OR bonus < 1000;