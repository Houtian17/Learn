package abstractClasses;

public class PersonTest {
    public static void main(String[] args) {

        Person[] people =new Person[2];

        people[0]=new Employee("gg",23333,1991,2,2);
        people[1]=new Student("ii","2012");

        for (Person e:people){
            System.out.println(e.getName()+","+e.getDescription());
        }
    }
}
