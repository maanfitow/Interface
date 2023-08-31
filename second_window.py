from PyQt5 import uic
from PyQt5.QtWidgets import *
import pandas as pd

dfC = pd.read_csv('Interface/dataset.csv')
dfC["Name"]= dfC["Name"].astype(str)
df = dfC[:10000].copy()

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("Interface/ui/second_w.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.df_visualize)
        self.bt_del.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.df_clear)

    def df_visualize(self):
        self.df_clear()
        global df
        df = pd.read_csv('Interface/dataset.csv')
        for r in range(len(df['Name'])):
            self.tableWidget.insertRow(r)
            for k in range(5):
                self.tableWidget.setItem(r,k,QTableWidgetItem(str(df.loc[r][k])))

    def df_clear(self):
        for _ in range(self.tableWidget.rowCount()):
            self.tableWidget.clear()
        # Delete all rows
        self.tableWidget.setRowCount(0)
        # Set column names
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Height', 'Width', 'Volume', 'Water'])
        
    def delete(self):
        # Delete the row from the dataframe
        global df
        df.drop(df.index[self.tableWidget.currentRow()], inplace=True)
        df.to_csv('Interface/dataset.csv', index=False)
        # Delete the selected row
        self.tableWidget.removeRow(self.tableWidget.currentRow())

def main():
    app = QApplication([])
    window= MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()
