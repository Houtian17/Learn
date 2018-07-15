public class ParamTest {

    public static void main(String[] args) {
        System.out.println("Testing tripleValue");
        double percent = 10;
        System.out.println("Before: percent=" + percent);

        System.out.println("\nTesting tripleSalary");
        Employeee harry = new Employeee("Harry", 5000);
        System.out.println("Before:salary=" + harry.getSalary());
        tripleSalary(harry);
        System.out.println("After:salary=" + harry.getSalary());

        System.out.println("\nTesting swap");
        Employeee a = new Employeee("Alice", 70000);
        Employeee b = new Employeee("Bob", 80000);
        System.out.println("Before a=" + a.getName());
        System.out.println("Before b=" + b.getName());
        swap(a, b);
        System.out.println("After a=" + a.getName());
        System.out.println("After b=" + b.getName());

    }

    public static void tripleValue(double x) {
        x = 3 * x;
        System.out.println("End of method:x=" + x);
    }

    public static void tripleSalary(Employeee x) {
        x.raiseSalary(200);
        System.out.println("End of method:salary=" + x.getSalary());
    }

    public static void swap(Employeee x, Employeee y) {
        Employeee temp = x;
        x = y;
        y = temp;
        System.out.println("End of method: x=" + x.getName());
        System.out.println("End of method: y=" + y.getName());
    }

}

class Employeee {

    private String name;
    private double salary;

    public Employeee(String n, double s) {
        name = n;
        salary = s;
    }

    public String getName() {
        return name;
    }

    public double getSalary() {
        return salary;
    }

    public void raiseSalary(double byPercent) {
        double raise = salary * byPercent / 100;
        salary += raise;
    }
}