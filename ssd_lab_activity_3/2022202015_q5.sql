select Dep.Mgr_ssn as 'manager ssn', Dep.Dnumber as 'Dept id', count(D.Relationship)
from DEPARTMENT Dep, DEPENDENT D
where Dep.Mgr_ssn = D.Essn and 
Dep.Dnumber in (Select DL.Dnumber from DEPT_LOCATIONS DL group by DL.Dnumber having count(*) >= 2)
group by Dep.Dnumber;