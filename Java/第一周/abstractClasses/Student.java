package abstractClasses;

public class Student extends Person {

    private String marjor;

    public Student(String name, String major) {
        super(name);
        this.marjor = major;
    }

    @Override
    public String getDescription() {
        return "a student majoring in " + marjor;
    }

}
