/*
* Fichier: creationdb.sql
* Auteurs: Félix Michaud, Vincent Bélisle, Maxime Boucher
* Date: 08 novembre 2021,
* Description: Création de la base de données LDVELH et de son user.
*/

DROP DATABASE LDVELH_test;

CREATE DATABASE LDVELH_test;

USE LDVELH_test;

# Création des tables de la bd.

CREATE TABLE `hero` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `nom` varchar(255)
);

CREATE TABLE `fiche_personnage` (
	`id` int PRIMARY KEY AUTO_INCREMENT,
	`session_id` int,
	`vie` int,
	`endurance` int,
	`equipement` varchar(255)
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

ALTER TABLE `session` ADD FOREIGN KEY (`chapitre_id`) REFERENCES `chapitre` (`id`);

ALTER TABLE `fiche_personnage` ADD FOREIGN KEY (`session_id`) REFERENCES `session` (`id`);

ALTER TABLE `chapitre` ADD FOREIGN KEY (`session_id`) REFERENCES `session` (`id`);




# Insertion initiales
INSERT INTO livre (titre,prenom_auteur,nom_auteur)
VALUES ("Les-maitres-des-tenebres","Jean","Bozo");

INSERT INTO hero (nom) VALUES("Michel");

INSERT INTO session (hero_id,chapitre_id,nom) VALUES (1,1,"session_1");



# Création de l'usager pour la bd.
CREATE USER 'hero'@'localhost' IDENTIFIED BY 'hero';
GRANT SELECT, UPDATE, INSERT ON ldvelh_test.* TO 'hero'@'localhost';





DELIMITER $$
CREATE FUNCTION dee() RETURNS INT NO SQL
BEGIN
	DECLARE dee_aleatoire INT; 
	SET dee_aleatoire = FLOOR(RAND()*(7-1)+1);
	RETURN dee_aleatoire;
END $$
DELIMITER ; 

DELIMITER $$
CREATE FUNCTION calcul_vie(perte_vie INT, id_hero INT) RETURNS INT READS SQL DATA DETERMINISTIC
BEGIN
DECLARE vie_personnage INT; 
SET vie_personnage = (SELECT vie FROM hero WHERE id = id_hero);

RETURN vie_personnage = perte_vie; 
END $$
DELIMITER ; 


