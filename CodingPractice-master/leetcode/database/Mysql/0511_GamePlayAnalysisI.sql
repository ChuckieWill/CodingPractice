/*
* @Author: Yan_Daojiang
* @Date:   2019-10-09 19:20:04
* @Last Modified by:   13738
* @Last Modified time: 2019-10-09 19:20:18
*/
SELECT  player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;