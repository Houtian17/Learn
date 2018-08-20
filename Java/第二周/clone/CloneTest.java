package clone;

public class CloneTest {
    public static void main(String[] args) {
        try{
            Employee original=new Employee("John Q. public",500);
            original.setHireDay(2000,1,1);
            Employee copy=original.clone();
            copy.raiseSalary(10);
            copy.setHireDay(2002,12,31);

        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }
    }
}
