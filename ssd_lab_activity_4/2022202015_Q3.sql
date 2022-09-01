/*
Write multi-parameterised stored procedure to get the names, grades of customers whose sum
 of opening amount and receive amount is greater than 10000.
*/

DELIMITER $$
create procedure `Question3` ()
BEGIN
  select c.CUST_NAME, c.GRADE from customer c where c.CUST_NAME in( select CUST_NAME  from customer c group by CUST_NAME having sum(c.OPENING_AMT+c.RECEIVE_AMT)>10000);
END$$
DELIMITER ;

Call Question3();


/*
#result
'Holmes', '2'
'Albert', '3'
'Ravindran', '2'
'Cook', '2'
'Stuart', '1'
'Bolt', '3'
'Fleming', '2'
'Jacks', '1'
'Yearannaidu', '1'
'Sasikant', '1'
'Ramanathan', '1'
'Avinash', '2'
'Winston', '1'
'Shilton', '1'
'Srinivas', '2'
'Steven', '1'
'Karolina', '1'
'Martin', '2'
'Ramesh', '3'
'Rangarappa', '2'
'Venkatpati', '2'
'Sundariya', '3'

*/