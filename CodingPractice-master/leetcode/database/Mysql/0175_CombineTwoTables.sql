/*
* @Author: Yan_Daojiang
* @Date:   2019-10-01 22:59:24
* @Last Modified by:   13738
* @Last Modified time: 2019-10-01 22:59:35
*/
# Write your MySQL query statement below
SELECT FirstName, LastName, City, State
FROM Person LEFT JOIN Address
ON Person.PersonId = Address.PersonId;