select DL.Dnumber, Dep2.Dname, count(DL.Dnumber) from DEPT_LOCATIONS DL, DEPARTMENT Dep2
where DL.Dnumber in(select Dep.Dnumber from DEPARTMENT Dep
where Dep.Mgr_ssn in (select D.Essn from DEPENDENT D
where D.Sex='F' group by D.Essn having count(D.Sex)>=2)) and DL.Dnumber = Dep2.Dnumber
group by DL.Dnumber;