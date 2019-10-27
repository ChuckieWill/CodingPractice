/*
* @Author: Yan_Daojiang
* @Date:   2019-09-21 22:41:40
* @Last Modified by:   13738
* @Last Modified time: 2019-09-28 19:07:34
*/

# Write your MySQL query statement below
#考查条件的书写
SELECT name , population , area
FROM World
WHERE area > 3000000 OR population >25000000 ;