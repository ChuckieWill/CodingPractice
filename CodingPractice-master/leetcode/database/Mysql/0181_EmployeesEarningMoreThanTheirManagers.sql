/*
* @Author: Yan_Daojiang
* @Date:   2019-10-01 23:20:07
* @Last Modified by:   13738
* @Last Modified time: 2019-10-01 23:20:17
*/
# Write your MySQL query statement below
# 通过自联结建立判断条件
SELECT Employee1.Name AS Employee
FROM Employee AS Employee1 JOIN Employee AS Employee2
WHERE Employee1.ManagerId = Employee2.Id AND Employee1.Salary > Employee2.Salary;