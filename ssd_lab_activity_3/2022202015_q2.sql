select CONCAT(E.Fname,' ',E.Minit,' ',E.Lname) as Fname, E.Ssn, E.Dno as 'Dept. id', count(*) as 'Number of Employees' from EMPLOYEE E, EMPLOYEE E2
where E.Ssn = E2.Super_ssn
group by E2.Super_ssn;