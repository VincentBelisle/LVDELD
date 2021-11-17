import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="hero",    
    password="hero",
    database="ldvelh")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Login")
        button = QPushButton("Connection")
        self.setFixedSize(QSize(400, 200))
        button.setCheckable(True)
        self.inputName = QLineEdit()
        self.inputPass = QLineEdit()
        self.labelNom = QLabel('Login :')
        self.labelNom.setFixedSize(QSize(400,25))
        self.inputPass.setFixedSize(QSize(400,25))
        self.login = QLineEdit()
        self.login.setFixedSize(QSize(377,25))
        self.labelpassword = QLabel('Password :')
        self.password = QLineEdit()
        self.login.setFixedSize(QSize(400,25))
        





        layout = QVBoxLayout()
        layout.addWidget(self.labelNom)
        layout.addWidget(self.login)
        layout.addWidget(self.labelpassword)
        layout.addWidget(self.password)
        layout.addWidget(button)

        

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
        
        
       
        
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