/*
* @Author: Yan_Daojiang
* @Date:   2019-09-21 22:53:47
* @Last Modified by:   13738
* @Last Modified time: 2019-09-28 19:08:26
*/


# Write your MySQL query statement below
# 考查行的选择条件的结果的输出顺序
SELECT id , movie , description , rating
FROM cinema 
WHERE description <> 'boring' AND MOD(id,2)=1
ORDER BY rating DESC ;