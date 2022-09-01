/*
. Write an explicit cursor to get the details(name, city, country, grade) of customers whose agent
 code start with A00.
*/
use `CUSTOMER_DB`;

create table tempTable(`CUST_NAME` varchar(40) NOT NULL,
  `CUST_CITY` varchar(35) DEFAULT NULL,
  `CUST_COUNTRY` varchar(20) NOT NULL,
  `GRADE` decimal(10,0) DEFAULT NULL);


DELIMITER $$
CREATE PROCEDURE `curdemo`()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE a varchar(6);
  DECLARE b varchar(40);
  DECLARE c varchar(35);
  DECLARE d varchar(20);
  DECLARE e decimal(10,0);
  DECLARE cur1 CURSOR FOR SELECT AGENT_CODE,CUST_NAME,CUST_CITY,CUST_COUNTRY,GRADE FROM customer;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  OPEN cur1;

  read_loop: LOOP
    FETCH cur1 INTO a, b, c, d, e;
    IF done THEN
      LEAVE read_loop;
    END IF;
    IF a like "A00%" THEN
      INSERT INTO tempTable VALUES (b,c,d,e);
    END IF;
  END LOOP;

  CLOSE cur1;
END$$

call curdemo();
select * from tempTable;

truncate table tempTable;