package inheritance;
import java.time.*;

public class ManagerTest {
    public static void main(String[] args) {
        Manager boss=new Manager("ffff",10000,1971,7,7);
        boss.setBonus(2000);

        Employee[] staff=new Employee[3];

        staff[0]=boss;
        staff[1]=new Employee("gggg",20000,1981,7,7);
        staff[2]=new Employee("hhhh",30000,1000,1,1);

        for (Employee e:staff){
            System.out.println("name="+e.getName()+",salary="+e.getSalary());
        }
    }
}
