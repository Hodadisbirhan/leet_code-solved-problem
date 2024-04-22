write the sql query the fetch the Nth highest salary in the Employee table
create function getNthHighestSalary(N INT)
begin
  set N= N-1;
 Return (Select distinct( Salary) from Employee order by salary desc limit 1 offset n);
end;
