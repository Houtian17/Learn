package equals;

public class EqualsTest {
    public static void main(String[] args) {
        Employee alice1 = new Employee("alice", 75000, 1991, 5, 5);
        Employee alice2 = alice1;
        Employee alice3 = new Employee("alice", 75000, 1987, 12, 15);
        Employee bob = new Employee("bob", 5000, 2000, 10, 13);


        System.out.println("alice1==alice2" + (alice1 == alice2));

        System.out.println("alice1==alice3" + (alice1 == alice3));

        System.out.println("alice1.equals(alice3)" + alice1.equals(alice3));

        System.out.println("alice.equals(bob)" + alice1.equals(bob));

        System.out.println("bob.toString():" + bob.toString());

        Manager carl = new Manager("carl", 800, 1971, 1, 1);
        Manager boss = new Manager("carl", 800, 1971, 1, 1);
        boss.setBonus(5000);
        System.out.println("boss.toString()=" + boss.toString());
        System.out.println("carl.equals(boss)=" + carl.equals(boss));
        System.out.println("alice1.hashCode()=" + alice1.hashCode());
        System.out.println("alice3.hashCode()=" + alice3.hashCode());
        System.out.println("bob.hashCode()=" + bob.hashCode());
        System.out.println("carl.hashCode()=" + carl.hashCode());
    }


}
