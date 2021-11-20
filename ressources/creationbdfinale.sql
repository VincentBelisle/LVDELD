
/*
* Fichier: creationdb.sql
* Auteurs: Félix Michaud, Vincent Bélisle, Maxime Boucher
* Date: 08 novembre 2021,
* Description: Création de la base de données LDVELH et de son user.
*/
DROP DATABASE LDVELH; 
CREATE DATABASE LDVELH;
USE LDVELH;

CREATE TABLE `hero` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `nom` varchar(255),
  `page_lue` int	
);

CREATE TABLE `fiche_personnage` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `session_id` int,
  `vie` int,
  `endurance` int,
  `sac_a_dos_id` int,
  `aventure_id` int
);

CREATE TABLE `aventure` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `discipline_1` varchar(255),
  `discipline_2` varchar(255),
  `discipline_3` varchar(255),
  `discipline_4` varchar(255),
  `discipline_5` varchar(255),
  `arme` varchar(255)
);

CREATE TABLE `sac_a_dos` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `objet_1` varchar(255),
  `objet_2` varchar(255),
  `objet_3` varchar(255),
  `objet_4` varchar(255),
  `objet_5` varchar(255),
  `objet_6` varchar(255),
  `objet_7` varchar(255),
  `objet_8` varchar(255),
  `repas` varchar(255),
  `argent` int
);

CREATE TABLE `chapitre` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `livre_id` int,
  `numero_chapitre` int,
  `texte` text
);

CREATE TABLE `livre` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `titre` varchar(255),
  `prenom_auteur` varchar(255),
  `nom_auteur` varchar(255)
);

CREATE TABLE `session` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `hero_id` int,
  `chapitre_id` int,
  `nom` varchar(255)
);

ALTER TABLE `session` ADD FOREIGN KEY (`hero_id`) REFERENCES `hero` (`id`);

ALTER TABLE `fiche_personnage` ADD FOREIGN KEY (`session_id`) REFERENCES `session` (`id`);

ALTER TABLE `session` ADD FOREIGN KEY (`chapitre_id`) REFERENCES  `chapitre` (`id`);

ALTER TABLE `chapitre` ADD FOREIGN KEY (`livre_id`) REFERENCES `livre` (`id`);

ALTER TABLE `fiche_personnage` ADD FOREIGN KEY  (`sac_a_dos_id`) REFERENCES `sac_a_dos` (`id`);

ALTER TABLE `fiche_personnage`  ADD FOREIGN KEY  (`aventure_id`) REFERENCES `aventure`(`id`);

# Insertion initiales
INSERT INTO livre (titre,prenom_auteur,nom_auteur)
VALUES ("Les-maitres-des-tenebres","Jean","Bozo");

INSERT INTO hero (nom) VALUES("Michel");

# Création de l'usager pour la bd.
#CREATE USER 'hero'@'localhost' IDENTIFIED BY 'hero';
GRANT SELECT, UPDATE, EXECUTE, INSERT ON ldvelh.* TO 'hero'@'localhost';

DELIMITER $$
CREATE FUNCTION dee() RETURNS INT NO SQL
BEGIN
	DECLARE dee_aleatoire INT; 
	SET dee_aleatoire = FLOOR(RAND()*(7-1)+1);
	RETURN dee_aleatoire;
END $$
DELIMITER ; 

DELIMITER $$
CREATE FUNCTION enlever_vie (montant INT, id_personnage INT) RETURNS VARCHAR(255) READS SQL DATA DETERMINISTIC
BEGIN

SELECT fiche_personnage.vie = fiche_personnage.vie - montant WHERE id = fiche_personnage.id;
RETURN 1; 
END $$
DELIMITER ;

DELIMITER $$
CREATE FUNCTION ajouter_vie (montant INT, id_personnage INT) RETURNS VARCHAR(255) READS SQL DATA DETERMINISTIC
BEGIN
SELECT fiche_personnage.vie = fiche_personnage.vie - montant WHERE id = fiche_personnage.id;
RETURN 1;
END $$
DELIMITER ;

DELIMITER $$ 

DELIMITER $$ 
CREATE TRIGGER gestion_point_vie AFTER UPDATE ON hero FOR EACH ROW

BEGIN
	if vie <= 0 THEN
		SET vivant = 0; 
	END IF 
END $
DELIMITER ;

DELIMITER $$
CREATE TRIGGER suivi_page_lue AFTER UPDATE ON session FOR EACH ROW
BEGIN
	IF !(NEW.chapitre_id <=> OLD.chapitre_id) THEN 
		hero.page_lue = hero.page_lue +1; 
	END IF
END $
DELIMITER ; 

DELIMITER $$
DROP PROCEDURE IF EXISTS afficher_chapitre$$
CREATE PROCEDURE afficher_chapitre(IN _numero_chapitre INT)
BEGIN

SELECT texte FROM chapitre WHERE chapitre.id = _numero_chapitre;

END $$
DELIMITER ;

DELIMITER $$ 
DROP PROCEDURE IF EXISTS enregistrer_donnees$$
CREATE PROCEDURE enregistrer_donnees(IN id_sac INT, IN objet_1 INT, IN objet_2 INT, IN objet_3 INT, IN objet_4 INT,
			IN objet_5 INT,IN objet_6 INT,IN objet_7 INT,IN objet_8 INT, IN repas VARCHAR(255), IN argent INT, IN id_aventure INT,
            IN discipline_1 INT, IN discipline_2 INT, IN discipline_3 INT, IN discipline_4 INT, IN discipline_5 INT,
            IN arme INT,IN id_personnage INT, IN endurance INT, IN vie INT) 
            BEGIN
				UPDATE sac_a_dos 
                SET objet_1 = objet_1, 
                objet_2 = objet_2, 
                objet_3 = objet_3, 
                objet_4 = objet_4, 
                objet_5 = objet_5, 
                objet_6 = objet_6, 
                objet_7 = objet_7, 
                objet_8 = objet_8,
                repas = repas,
                argent = repas
                WHERE sac_a_dos.id = id_sac;
                
                UPDATE aventure
                SET discipline_1 = discipline1,
                discipline_2 = discipline2,
                discipline_3 = discipline3,
                discipline_4 = discipline4,
				discipline_5 = discipline5,
                arme = arme
                WHERE aventure.id = id_aventure;
                
                UPDATE fiche_personnage
                SET endurance = endurance, 
					vie = vie 
                    WHERE fiche_personnage.id = id_personnage; 
                
            END $$fiche_personnage
DELIMITER ;


CALL afficher_chapitre(0);

SELECT chapitre_id FROM session WHERE id = 4; 
SELECT * FROM hero; 
SELECT * FROM chapitre; 
SELECT * FROM session; 
SELECT * FROM fiche_personnage;
INSERT INTO session (hero_id, chapitre_id, nom) VALUES (1,2,'test'); 
INSERT INTO sac_a_dos (objet_1) VALUES ('test1'); 
INSERT INTO aventure (id) VALUES (1); 
INSERT INTO  fiche_personnage (id, session_id, vie, endurance, sac_a_dos_id, aventure_id) VALUES (1, 4,10, 30, 1,1);

UPDATE session
SET chapitre_id = 1
WHERE id = 4; 
SELECT * FROM chapitre WHERE id = 141;
SELECT endurance FROM fiche_personnage WHERE id = 1; 
