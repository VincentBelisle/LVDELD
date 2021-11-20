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
        self.bouttonrecherche.clicked.connect(self.Changerchapitre)
        self.bouttonrecherche.setCheckable(True)
        self.recherche = QLineEdit()

        self.tab = QLabel(" ")

        self.textendurance = QLabel("Endurance: ")
        self.endurance = QTextEdit()

        self.textrepas = QLabel("Repas: ")
        self.repas = QTextEdit()

        self.textargent = QLabel("Argent: ")
        self.argent = QLineEdit("")

        self.textnbpage = QLabel("Nombre de page lue: ")
        self.nbpage = QLineEdit("")

        self.textdee = QLabel("Dée: ")
        self.dee = QLineEdit("6")

        self.buttondeco = QPushButton("Déconnection")
        self.buttondeco.setFixedSize(QSize(700,75))
        self.buttondeco.clicked.connect(self.Clicked)
        self.buttondeco.setCheckable(True)

        self.buttondee = QPushButton("Lancer le dée")
        self.buttondee.clicked.connect(self.Randomdee)
        self.buttondee.setCheckable(True)

        self.buttonpage = QPushButton("Calculer le nombre de page")
        self.buttonpage.clicked.connect(self.Nbpage)
        self.buttonpage.setCheckable(True)

       

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
        self.objet1 = QTextEdit()
        self.objet2 = QTextEdit()
        self.objet3 = QTextEdit()
        self.objet4 = QTextEdit()
        self.objet5 = QTextEdit()
        self.objet6 = QTextEdit()
        self.objet7 = QTextEdit()
        self.objet8 = QTextEdit()

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

        layoutdroitdroit.addWidget(self.tab)

        layoutdroitdroit.addWidget(self.textobjet)
        layoutdroitdroit.addWidget(self.objet1)
        layoutdroitdroit.addWidget(self.objet2)
        layoutdroitdroit.addWidget(self.objet3)
        layoutdroitdroit.addWidget(self.objet4)
        layoutdroitdroit.addWidget(self.objet5)
        layoutdroitdroit.addWidget(self.objet6)
        layoutdroitdroit.addWidget(self.objet7)
        layoutdroitdroit.addWidget(self.objet8)

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

        layoutdroitgauche.addWidget(self.textdee)
        layoutdroitgauche.addWidget(self.dee)
        layoutdroitgauche.addWidget(self.buttondee)

        layoutdroitgauche.addWidget(self.tab)

        layoutdroitgauche.addWidget(self.textargent)
        layoutdroitgauche.addWidget(self.argent)

        layoutdroitgauche.addWidget(self.tab)

        layoutdroitgauche.addWidget(self.textnbpage)
        layoutdroitgauche.addWidget(self.nbpage)
        layoutdroitgauche.addWidget(self.buttonpage)

        layoutdroitgauche.addWidget(self.tab)

        layoutHori.addLayout(layoutgauche)
        layoutHori.addLayout(layoutdroitgauche)
        layoutHori.addLayout(layoutdroitdroit)

        container = QWidget()
        container.setLayout(layoutHori)
        self.setCentralWidget(container)
        
    def Changerchapitre(self,checked):
        chapitre = self.recherche.text()
        argument = chapitre
        cursor = mydb.cursor()
        cursor.callproc('afficher_chapitre',[argument,])
         # print out the result
        print(argument)
        for result in cursor.stored_results():
            self.text.setText(str(result.fetchone()[0]))
      
    
    def Clicked(self, checked):
        self.close()
    
    def Randomdee(self, checked):
        mycursor = mydb.cursor()
        funcdee = "SELECT dee()"
        mycursor.execute(funcdee)
        result = str(mycursor.fetchone()[0])
        self.dee.setText(result)
        
    def Nbpage(self, checked):
        mycursor = mydb.cursor()
        funcdee = "SELECT dee()"
        mycursor.execute(funcdee)
        result = str(mycursor.fetchone()[0])
        self.dee.setText(result)


class ConnectionUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.livre = Livre()
        self.setWindowTitle("Login")
        self.setFixedSize(QSize(600, 400))
        self.labeluser = QLabel('Nom user :')
        self.nomuser = QLineEdit()
        self.labelcreeuser = QLabel('Nouveau user :')
        self.nouveauuser = QLineEdit()
        self.buttonuser = QPushButton("Sélectionner la session")
        self.buttonuser.clicked.connect(self.Selectionner)
        self.buttonuser.setCheckable(True)
        self.buttoncreeuser = QPushButton("Créer la session")
        self.buttoncreeuser.clicked.connect(self.Creer)
        self.buttoncreeuser.setCheckable(True)

        layout = QVBoxLayout()
        layout.addWidget(self.labeluser)
        layout.addWidget(self.nomuser)
        layout.addWidget(self.buttonuser)
        layout.addWidget(self.labelcreeuser)
        layout.addWidget(self.nouveauuser)
        layout.addWidget(self.buttoncreeuser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)



            
    def Selectionner(self, checked):
        session = self.nomuser.text()
        sql = "SELECT sac_a_dos_id FROM fiche_personnage WHERE session_id = %s"
        mycursor = mydb.cursor()
        mycursor.execute(sql,(session,))
        id_sac =  str(mycursor.fetchone()[0])

        sql_aventure = "SELECT aventure_id FROM fiche_personnage WHERE session_id = %s"
        mycursor.execute(sql_aventure,(session,))
        id_aventure = (str(mycursor.fetchone()[0]))

        sql1 = "SELECT objet_1 FROM sac_a_dos WHERE id = %s"
        mycursor.execute(sql1,(id_sac,))
        objet1_text = str(mycursor.fetchone()[0])
        self.livre.objet1.setText(objet1_text)
        
        sql2 = "SELECT objet_2 FROM sac_a_dos WHERE id = %s"
        mycursor.execute(sql2,(id_sac,))
        objet2_text = str(mycursor.fetchone()[0])
        self.livre.objet2.setText(objet2_text)
 
    
        sql3 = "SELECT objet_3 FROM sac_a_dos WHERE id = %s"
        mycursor.execute(sql3,(id_sac,))
        objet3_text = str(mycursor.fetchone()[0])
        self.livre.objet3.setText(objet3_text)

        sql4 = "SELECT objet_4 FROM sac_a_dos WHERE id = %s"
        mycursor.execute(sql4,(id_sac,))
        objet4_text = str(mycursor.fetchone()[0])
        self.livre.objet4.setText(objet4_text)


        sql5 = "SELECT objet_5 FROM sac_a_dos WHERE id = %s"
        mycursor.execute(sql5,(id_sac,))
        objet5_text = str(mycursor.fetchone()[0])
        self.livre.objet5.setText(objet5_text)

        sql6 = "SELECT objet_6 FROM sac_a_dos WHERE id = %s"
        mycursor.execute(sql6,(id_sac,))
        objet6_text = str(mycursor.fetchone()[0])
        self.livre.objet6.setText(objet6_text)


        sql7 = "SELECT objet_7 FROM sac_a_dos WHERE id = %s"
        mycursor.execute(sql7,(id_sac,))
        objet7_text = str(mycursor.fetchone()[0])
        self.livre.objet7.setText(objet7_text)


        sql8 = "SELECT objet_8 FROM sac_a_dos WHERE id = %s"
        mycursor.execute(sql8,(id_sac,))
        objet8_text = str(mycursor.fetchone()[0])
        self.livre.objet8.setText(objet8_text)

        sqlargent = "SELECT argent FROM sac_a_dos WHERE id = %s"
        mycursor.execute(sqlargent,(id_sac,))
        argent_text = str(mycursor.fetchone()[0])
        self.livre.argent.setText(argent_text)

        sql_chapitre_id = "SELECT chapitre_id FROM session WHERE id = %s"
        mycursor.execute(sql_chapitre_id,(session,))
        id_chapitre = str(mycursor.fetchone()[0])
        argument = id_chapitre
        cursor = mydb.cursor()
        cursor.callproc('afficher_chapitre',[argument,])
         # print out the result
        for result in cursor.stored_results():
             self.livre.text.setText(str(result.fetchone()[0]))
        if self.isVisible():
            self.hide()
            self.livre.show()

        sqldiscipline_1 = "SELECT discipline_1 FROM aventure WHERE id = %s"
        mycursor.execute(sqldiscipline_1,(id_aventure,))
        discipline1_text = str(mycursor.fetchone()[0])
        self.livre.discipline1.setText(discipline1_text)

        sqldiscipline_2 = "SELECT discipline_2 FROM aventure WHERE id = %s"
        mycursor.execute(sqldiscipline_2,(id_aventure,))
        discipline2_text = str(mycursor.fetchone()[0])
        self.livre.discipline2.setText(discipline2_text)

        sqldiscipline_3 = "SELECT discipline_3 FROM aventure WHERE id = %s"
        mycursor.execute(sqldiscipline_3,(id_aventure,))
        discipline3_text = str(mycursor.fetchone()[0])
        self.livre.discipline3.setText(discipline3_text)

        sqldiscipline_4 = "SELECT discipline_4 FROM aventure WHERE id = %s"
        mycursor.execute(sqldiscipline_4,(id_aventure,))
        discipline4_text = str(mycursor.fetchone()[0])
        self.livre.discipline4.setText(discipline4_text)

        sqldiscipline_5 = "SELECT discipline_5 FROM aventure WHERE id = %s"
        mycursor.execute(sqldiscipline_5,(id_aventure,))
        discipline5_text = str(mycursor.fetchone()[0])
        self.livre.discipline5.setText(discipline5_text)

        sqlarme1 =  "SELECT arme FROM aventure WHERE id = %s"
        mycursor.execute(sqlarme1,(id_aventure,))
        arme_text = str(mycursor.fetchone()[0])
        self.livre.arme1.setText(arme_text)


        sqlendurance = "SELECT endurance FROM fiche_personnage WHERE id = %s"
        mycursor.execute(sqlendurance,(id_aventure,))
        endurance = str(mycursor.fetchone()[0])
        print(endurance)
        self.livre.endurance.setText(endurance)

        

       

    def Creer(self, checked):
        if self.isVisible():
            self.hide()
            self.connection.show()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connection = ConnectionUser()
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
                self.connection.show()
        else:
            self.login.setText("")
            self.password.setText("")

    def ConnectionUser(self, checked):
            print("")

    def aller_page(self,checked):
        print("")
        
    def call_find_all_sp(self,checked):
            argument = self.text
            db_config = mydb
            cursor = mydb.cursor()
            args = [argument]
            cursor.callproc('afficher_chapitre')

            # print out the result
            for result in cursor.stored_results():
                print(result.fetchall())

app = QApplication(sys.argv)
mainWin = ConnectionUser()
mainWin.show()
sys.exit( app.exec_() )