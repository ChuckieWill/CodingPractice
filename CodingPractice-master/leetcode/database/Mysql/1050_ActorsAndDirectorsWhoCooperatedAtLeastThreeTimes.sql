/*
* @Author: Yan_Daojiang
* @Date:   2019-10-01 22:31:35
* @Last Modified by:   13738
* @Last Modified time: 2019-10-01 22:31:47
*/
# Write your MySQL query statement below
SELECT ACTOR_ID, DIRECTOR_ID
From ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;