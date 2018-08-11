import javax.swing.event.TableColumnModelListener;
import javax.swing.event.TableModelListener;
import javax.swing.table.TableModel;

public class KCBData implements TableModel {
    private String[] title = {
            "周一", "周二", "周三", "周四", "周五", "周六", "周日"
    };

    private String[][] data = new String[8][7];

    public KCBData() {
        for (int i = 0; i < data.length; i++) {
            for (int j = 0; j < data[i].length; j++) {
                data[i][j] = "";
            }
        }
    }

    @Override
    public int getRowCount() {
        return 8;
    }

    @Override
    public int getColumnCount() {
        return 7;
    }

    @Override
    public String getColumnName(int arg0) {
        return title[arg0];
    }

    @Override
    public Class<?> getColumnClass(int columnIndex) {
        return String.class;
    }

    @Override
    public boolean isCellEditable(int rowIndex, int columnIndex) {
        return true;
    }

    @Override
    public Object getValueAt(int arg0, int arg1) {
        return data[arg0][arg1];
    }

    @Override
    public void setValueAt(Object arg0, int arg1, int arg2) {
        data[arg1][arg2] = (String) arg0;
    }

    @Override
    public void addTableModelListener(TableModelListener l) {

    }

    @Override
    public void removeTableModelListener(TableModelListener l) {

    }
}
