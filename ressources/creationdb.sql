CREATE DATABASE LVDELH;

USE LVDELH;

CREATE TABLE `hero` (
  `id_hero` int PRIMARY KEY,
  `chapitre_id` int
);

CREATE TABLE `chapitre` (
  `id_chapitre` int PRIMARY KEY,
  `livre_id` int,
  `numero_chapitre` int,
  `texte` text
);

CREATE TABLE `livre` (
  `id_livre` int PRIMARY KEY,
  `titre` varchar(255),
  `prenom_auteur` varchar(255),
  `nom_auteur` varchar(255)
);

ALTER TABLE `chapitre` ADD FOREIGN KEY (`livre_id`) REFERENCES `livre` (`id_livre`);

ALTER TABLE `hero` ADD FOREIGN KEY (`chapitre_id`) REFERENCES `chapitre` (`id_chapitre`);


