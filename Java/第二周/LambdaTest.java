import javax.swing.*;
import java.sql.Date;
import java.util.Arrays;
import java.util.Timer;

import static java.lang.System.*;

public class LambdaTest {
    public static void main(String[] args) {
        String[] planets = new String[]{"Mercury", "Venus", "Earth", "Mars"};
        out.println(Arrays.toString(planets));
        out.println("Sorted in dictionary order:");
        Arrays.sort(planets);
        out.println(Arrays.toString(planets));
        out.println("Sorted by length:");
        Arrays.sort(planets, (first, second) -> first.length() - second.length());
        out.println(Arrays.toString(planets));

        Timer t = new Timer(1000, event ->
                System.out.println("the time is"+new Date()));
        t.start();

        JOptionPane.showMessageDialog(null,"quit program?");
        exit(0);
    }
}
