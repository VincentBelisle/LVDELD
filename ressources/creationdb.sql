CREATE DATABASE LDVELH;

USE LDVELH;


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

