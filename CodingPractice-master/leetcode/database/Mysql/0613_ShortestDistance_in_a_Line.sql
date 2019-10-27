/*
* @Author: Yan_Daojiang
* @Date:   2019-10-09 19:08:19
* @Last Modified by:   13738
* @Last Modified time: 2019-10-09 19:08:33
*/
# Write your MySQL query statement below
SELECT MIN(ABS(p1.x-p2.x)) AS shortest
FROM point AS p1 JOIN point AS p2
ON p1.x != p2.x;