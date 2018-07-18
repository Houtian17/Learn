import java.util.*;

public class ArrayListTest {
    public static void main(String[] args) {
        ArrayList<Employee> staff = new ArrayList<>();

        staff.add(new Employee("carl",100,1971,7,7));
        staff.add(new Employee("Harry",1000,1972,7,7));
        staff.add(new Employee("fuck",10000,1973,7,7));

        for (Employee e:staff){
            e.raiseSalary(5);
        }

        for (Employee e:staff){
            System.out.println("name="+e.getName()+",salary="+e.getSalary()+"hireDay="+e.getHireDay());
        }
    }

}
