/*
* @Author: Yan_Daojiang
* @Date:   2019-10-01 22:41:28
* @Last Modified by:   13738
* @Last Modified time: 2019-10-01 22:41:43
*/

# Write your MySQL query statement below
SELECT Email 
FROM Person
GROUP BY Email
HAVING COUNT(Email) >= 2;