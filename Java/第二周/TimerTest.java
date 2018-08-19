import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Date;
import java.sql.SQLOutput;
import javax.swing.*;

public class TimerTest {
    public static void main(String[] args) {
        ActionListener listener = new TimerPrinter();
        Timer t=new Timer(1000,listener);
        t.start();
        JOptionPane.showMessageDialog(null,"quit program?");
        System.exit(0);

    }
    static class TimerPrinter implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
            System.out.println("At the tone ,the time is"+ new Date(1));
            Toolkit.getDefaultToolkit().beep();
        }
    }
}
