DELIMITER $$
CREATE PROCEDURE `SumTwo`(
	IN `num1` INT,
	IN `num2` INT,
	OUT `result` INT
)
BEGIN
	Set result = num1 + num2;
END$$
DELIMITER ;

Call SumTwo(3,53,@output);
SELECT @output;
#result-->56
