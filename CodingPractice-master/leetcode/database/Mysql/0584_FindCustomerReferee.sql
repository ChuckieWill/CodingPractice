/*
* @Author: Yan_Daojiang
* @Date:   2019-10-01 22:23:06
* @Last Modified by:   13738
* @Last Modified time: 2019-10-01 22:23:30
*/
# Write your MySQL query statement below
SELECT name
FROM customer 
WHERE referee_id IS NULL OR referee_id <> 2;