
Table Person 

personId    int
lastName    varchar 
firstName   varchar 

Table Address

addressId   int 
personId    int 
city        varchar 
state       varchar 

Combine and return the following fields 

FirstName, LastName, city, state of each person in Person table. 
Return table in any order 


SELECT p.firstName, p.lastName, a.city, a.state from Person p 
LEFT JOIN Address a 
ON p.personId = a.personId 