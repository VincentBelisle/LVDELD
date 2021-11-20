import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import mysql.connector

#connecteur a la db
mydb = mysql.connector.connect(
    host="localhost",
    user="hero",    
    password="hero",
    database="ldvelh")

#Gestion de la page du livre
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
        self.buttondeco.clicked.connect(self.Deconnection)
        self.buttondeco.setCheckable(True)

        self.buttondee = QPushButton("Lancer le dée")
        self.buttondee.clicked.connect(self.Randomdee)
        self.buttondee.setCheckable(True)

        self.buttonpage = QPushButton("Ajouter le nombre de page lue :)")
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

    #permet de changer la page afficher dans le livre    
    def Changerchapitre(self,checked):
        chapitre = self.recherche.text()
        argument = chapitre
        cursor = mydb.cursor()
        #on appel la procédure qui affiche les pages
        cursor.callproc('afficher_chapitre',[argument,])
         # print out the result
        print(argument)
        for result in cursor.stored_results():
            self.text.setText(str(result.fetchone()[0]))
      
    
    def Deconnection(self, checked):
        #on met la session a 1, normalement on va chercher le # de user avec le label du début, mais on avait des overflow avec des fonctions qui s'appelaient entre eux
        # session = session = self.nomuser.text()
        session = 1
        sql = "SELECT sac_a_dos_id FROM fiche_personnage WHERE session_id = %s"
        mycursor = mydb.cursor()
        mycursor.execute(sql,(session,))

        sql_aventure = "SELECT aventure_id FROM fiche_personnage WHERE session_id = %s"
        mycursor.execute(sql_aventure,(session,))
        id_aventure = (str(mycursor.fetchone()[0]))

        sql_personnage = "SELECT fiche_personnage.id FROM fiche_personnage WHERE session_id = %s"
        mycursor.execute(sql_personnage,(session,))
        id_personnage = (str(mycursor.fetchone()[0]))
        #ici on déclare toute les variables avec les labels de l'application pour utiliser la procédures stockée
        id_sac =  str(mycursor.fetchone()[0])
        objet1 = self.objet1.text()
        objet2 = self.objet2.text()
        objet3 = self.objet3.text()
        objet4 = self.objet4.text()
        objet5 = self.objet5.text()
        objet6 = self.objet6.text()
        objet7 = self.objet7.text()
        objet8 = self.objet8.text()
        repas = self.repas.text()
        argent = self.argent.text()
        discipline1 = self.discipline1.text()
        discipline2 = self.discipline2.text()
        discipline3 = self.discipline3.text()
        discipline4 = self.discipline4.text()
        discipline5 = self.discipline5.text()
        endurance = self.endurance.text()
        arme = self.arme1.texT()

        cursor = mydb.cursor(bufferred=True)
        cursor = mydb.cursor()
        #procédure stockée qui permet de stocker tous les nouveaux enregistrements à ajouter à la DB
        cursor.callproc('enregistrer_donnees',[id_sac,],[objet1,],[objet2,],[objet3,],[objet4,],[objet5,],[objet6,],[objet7,],[objet8,],[repas,],[argent,],[id_aventure,],[discipline1,],[discipline2,],[discipline3,],[discipline4,],[discipline5,],[arme,],[id_personnage,],[endurance,])       
        self.close()
    
    #permet de lancer un dée aléatoire
    def Randomdee(self, checked):
        mycursor = mydb.cursor()
        funcdee = "SELECT dee()"
        mycursor.execute(funcdee)
        result = str(mycursor.fetchone()[0])
        self.dee.setText(result)
    #permet d'afficher le nombre de page lue du user, encore une fois normalement on choisit le user en fonction de celui qui est connecté, mais problème d'overflow
    def Nbpage(self, checked):
        mycursor = mydb.cursor()
        funcpage = "SELECT page_lue(1)"
        mycursor.execute(funcpage)
        result = str(mycursor.fetchone()[0])
        self.nbpage.setText(result)

#window pour connecter le user
class ConnectionUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.livre = Livre()
        self.setWindowTitle("Login")
        self.setFixedSize(QSize(600, 400))
        self.labeluser = QLabel('Nom user (Le id du user) Example: 1 :')
        self.nomuser = QLineEdit()
        self.buttonuser = QPushButton("Sélectionner la session")
        self.buttonuser.clicked.connect(self.Selectionner)
        self.buttonuser.setCheckable(True)


        layout = QVBoxLayout()
        layout.addWidget(self.labeluser)
        layout.addWidget(self.nomuser)
        layout.addWidget(self.buttonuser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)



    #permet d'afficher les valeurs de la database aussitot qu'on entre le user et qu'on clique sur connecter        
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

        sqlbouffe = "SELECT repas FROM sac_a_dos WHERE id = %s"
        mycursor.execute(sqlbouffe,(id_sac,))
        bouffe_texte = str(mycursor.fetchone()[0])
        self.livre.repas.setText(bouffe_texte)


        sqlendurance = "SELECT endurance FROM fiche_personnage WHERE id = %s"
        mycursor.execute(sqlendurance,(id_aventure,))
        endurance = str(mycursor.fetchone()[0])
        print(endurance)
        self.livre.endurance.setText(endurance)

        sqlbouffe = "SELECT repas FROM sac_a_dos WHERE id = %s"
        mycursor.execute(sqlbouffe,(id_sac,))
        bouffe_texte = str(mycursor.fetchone()[0])
        self.livre.repas.setText(bouffe_texte)


    def Creer(self, checked):
        if self.isVisible():
            self.hide()
            self.connection.show()


app = QApplication(sys.argv)
mainWin = ConnectionUser()
mainWin.show()
sys.exit( app.exec_() )