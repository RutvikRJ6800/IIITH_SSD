/*
 Write a parameterised stored procedure to get the names of the customers who live in Bangalore.
*/
DELIMITER $$
create procedure `getCustomerWithCity` (in `cityName` varchar(35))
BEGIN
  select CUST_NAME from customer c where c.WORKING_AREA=cityName;
END$$
DELIMITER ;

Call getCustomerWithCity("Bangalore");

/*
#result
'Ravindran'
'Srinivas'
'Rangarappa'
'Venkatpati'
*/


DROP PROCEDURE getCustomerWithCity;

