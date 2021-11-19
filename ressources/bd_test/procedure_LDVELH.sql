DELIMITER $$
DROP PROCEDURE IF EXISTS afficher_chapitre$$
CREATE PROCEDURE afficher_chapitre(IN _session_id INT)
BEGIN

DECLARE _chapitre_id INT;

SET _chapitre_id = (SELECT chapitre_id FROM session WHERE id = _session_id);

SELECT texte FROM chapitre WHERE id =  _chapitre_id;

END $$
DELIMITER ;


CALL afficher_chapitre(1);
