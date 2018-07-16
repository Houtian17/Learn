import java.util.*;


public class ConstructorTest {
    public static void main(String[] args) {
        Employeeee[] staff = new Employeeee[3];

        staff[0] = new Employeeee("Harry", 40000);
        staff[1] = new Employeeee(40000);
        staff[2] = new Employeeee();

        for (Employeeee e : staff) {
            System.out.println("name=" + e.getName() + ",id=" + e.getId() + ",salary=" + e.getSalary());
        }

    }

}




class Employeeee {
    private static int nextId;

    private int id;
    private String name = "";
    private double salary;

    static {
        Random generator = new Random();
        nextId = generator.nextInt(10000);
    }

    {
        id = nextId;
    }

    public Employeeee(String n, double s) {
        name = n;
        salary = s;
    }

    public Employeeee(double s) {
        this("Emploeeee #" + nextId, s);
    }

    public Employeeee() {

    }

    public String getName() {
        return name;
    }

    public double getSalary() {
        return salary;
    }

    public int getId() {
        return id;
    }

}
