package clone;

import java.sql.Date;
import java.util.GregorianCalendar;

public class Employee {
    private String name;
    private double salary;
    private Date hireDay;

    public Employee(String name,double salary){
        this.name=name;
        this.salary=salary;
        hireDay=new Date(2018,8,20);
    }

    public Employee clone() throws CloneNotSupportedException{
        Employee cloned=(Employee)super.clone();
        cloned.hireDay=(Date)hireDay.clone();
        return cloned;
    }

    public void setHireDay(int year,int month,int day){
        Date newHireDay= (Date) new GregorianCalendar(year,month-1,day).getTime();
        hireDay.setTime(newHireDay.getTime());
    }

    public void raiseSalary(double byPercent){
        double raise=salary*byPercent/100;
        salary+=raise;
    }

    public String toString(){
        return "Employee[name="+name+",salary="+salary+",hireDay="+hireDay+"]";
    }

}
