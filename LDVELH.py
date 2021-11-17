import mysql.connector
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",    
    password="mysql",
    database="ldvelh")

class MainWindow(QMainWindow):


    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(600, 300))    
        self.setWindowTitle("PyQt") 

        self.nom = QLabel(self)
        self.nom.setText('Name:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nom.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)        

        self.citoyen = QLabel(self)
        self.citoyen.setText('Information Citoyen:       ')
        self.ligne = QLabel(self)
        self.ligne.setText(self.line.text())

        self.ligne.move(180, 160)
        self.ligne.resize(150, 32)
        self.citoyen.move(10, 160)
        
        
       
        
    def clickMethod(self):
        mycursor = mydb.cursor()
        sql = "SELECT texte FROM chapitre WHERE numero_chapitre = %s"

        mycursor.execute(sql,(self.line.text(),))

        myresult = mycursor.fetchall()
        for (texte) in myresult:
            self.ligne.setText('{}'.format(texte))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )