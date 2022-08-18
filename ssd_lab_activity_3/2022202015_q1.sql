select distinct CONCAT(E.Fname,' ',E.Minit,' ',E.Lname) as Fname, D.Dnumber, D.Dname
from EMPLOYEE E, DEPARTMENT D where E.ssn = D.Mgr_ssn and D.Dnumber in (select Dno from EMPLOYEE E2 
where E2.Ssn in (select Essn from WORKS_ON W where W.Hours <= 40.0));
