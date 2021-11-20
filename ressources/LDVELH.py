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


class Livre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Livre")
        self.setFixedSize(QSize(1900, 1000))
        self.text = QTextEdit()

        self.division = QLabel("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        self.bouttonrecherche = QPushButton("Aller au chapitre")
        self.recherche = QLineEdit()

        self.tab = QLabel(" ")

        self.textendurance = QLabel("Endurance: ")
        self.endurance = QTextEdit()

        self.textrepas = QLabel("Repas: ")
        self.repas = QTextEdit()

        self.textargent = QLabel("Argent: ")
        self.argent = QLineEdit()

        self.textvie = QLabel("Vie: ")
        self.vie = QLineEdit()

        self.buttondeco = QPushButton("Déconnection")
        self.buttondeco.setFixedSize(QSize(700,75))
        self.buttondeco.clicked.connect(self.Clicked)
        self.buttondeco.setCheckable(True)

        self.textarme = QLabel("Arme: ")
        self.arme1 = QLineEdit()
        self.arme2 = QLineEdit()

        self.textdiscipline = QLabel("Disciplines Kai: ")
        self.discipline1 = QLineEdit()
        self.discipline2 = QLineEdit()
        self.discipline3 = QLineEdit()
        self.discipline4 = QLineEdit()
        self.discipline5 = QLineEdit()

        self.textobjet = QLabel("Objet: ")
        self.objet = QTextEdit()

        layoutgauche = QVBoxLayout()
        layoutdroitgauche = QVBoxLayout()
        layoutdroitdroit = QVBoxLayout()
        layoutHori = QHBoxLayout()

        layoutgauche.addWidget(self.text)
        layoutgauche.addWidget(self.division)
        layoutgauche.addWidget(self.recherche)
        layoutgauche.addWidget(self.bouttonrecherche)

        layoutdroitdroit.addWidget(self.textarme)
        layoutdroitdroit.addWidget(self.arme1)
        layoutdroitdroit.addWidget(self.arme2)

        layoutdroitdroit.addWidget(self.tab)

        layoutdroitdroit.addWidget(self.textobjet)
        layoutdroitdroit.addWidget(self.objet)

        layoutdroitdroit.addWidget(self.tab)

        layoutdroitdroit.addWidget(self.textrepas)
        layoutdroitdroit.addWidget(self.repas)

        layoutdroitdroit.addWidget(self.tab)

        layoutdroitdroit.addWidget(self.buttondeco)

        layoutdroitdroit.addWidget(self.tab)

        layoutdroitgauche.addWidget(self.textdiscipline)
        layoutdroitgauche.addWidget(self.discipline1)
        layoutdroitgauche.addWidget(self.discipline2)
        layoutdroitgauche.addWidget(self.discipline3)
        layoutdroitgauche.addWidget(self.discipline4)
        layoutdroitgauche.addWidget(self.discipline5)

        layoutdroitgauche.addWidget(self.tab)

        layoutdroitgauche.addWidget(self.textendurance)
        layoutdroitgauche.addWidget(self.endurance)

        layoutdroitgauche.addWidget(self.tab)

        layoutdroitgauche.addWidget(self.textvie)
        layoutdroitgauche.addWidget(self.vie)

        layoutdroitgauche.addWidget(self.tab)

        layoutdroitgauche.addWidget(self.textargent)
        layoutdroitgauche.addWidget(self.argent)

        layoutdroitgauche.addWidget(self.tab)

        layoutHori.addLayout(layoutgauche)
        layoutHori.addLayout(layoutdroitgauche)
        layoutHori.addLayout(layoutdroitdroit)

        container = QWidget()
        container.setLayout(layoutHori)
        self.setCentralWidget(container)
    
    def Clicked(self, checked):
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Livre = Livre()
        self.setWindowTitle("Login")
        self.setFixedSize(QSize(400, 200))
        button = QPushButton("Connection")
        button.clicked.connect(self.Clicked)
        button.setCheckable(True)
        self.labellogin = QLabel('Login :')
        self.login = QLineEdit()
        self.labelpassword = QLabel('Password :')
        self.password = QLineEdit()
        


        layout = QVBoxLayout()
        layout.addWidget(self.labellogin)
        layout.addWidget(self.login)
        layout.addWidget(self.labelpassword)
        layout.addWidget(self.password)
        layout.addWidget(button)

        

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def Clicked(self, checked):
        if self.login.text() == "hero" and self.password.text() == "hero":
            if self.isVisible():
                self.hide()
                self.Livre.show()
        else:
            self.login.setText("")
            self.password.setText("")




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()