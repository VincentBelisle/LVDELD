/*
* Fichier: creationdb.sql
* Auteurs: Félix Michaud, Vincent Bélisle, Maxime Boucher
* Date: 08 novembre 2021,
* Description: Création de la base de données LDVELH et de son user.
*/

CREATE DATABASE LDVELH;

USE LDVELH;

# Création des tables de la bd.

CREATE TABLE `hero` (
  `id_hero` int PRIMARY KEY,
  `vie` int,
  `endurance` int,
  `equipement` varchar(255)
);

CREATE TABLE `fiche_personnage` (
  `hero_id` int,
  `vie` int,
  `endurance` int,
  `equipement` varchar(255)
);

CREATE TABLE `chapitre` (
  `id_chapitre` int PRIMARY KEY,
  `livre_id` int,
  `numero_chapitre` int
);

CREATE TABLE `livre` (
  `id_livre` int PRIMARY KEY,
  `titre` varchar(255),
  `prenom_auteur` varchar(255),
  `nom_auteur` varchar(255)
);

ALTER TABLE `chapitre` ADD FOREIGN KEY (`livre_id`) REFERENCES `livre` (`id_livre`);

ALTER TABLE `hero` ADD FOREIGN KEY (`id_hero`) REFERENCES `livre` (`id_livre`);

ALTER TABLE `fiche_personnage` ADD FOREIGN KEY (`hero_id`) REFERENCES `hero` (`id_hero`);


# Création de l'usager pour la bd.

CREATE USER 'hero'@'localhost' IDENTIFIED BY 'hero';
GRANT SELECT, UPDATE ON lvdelh.* TO 'hero'@'localhost';

