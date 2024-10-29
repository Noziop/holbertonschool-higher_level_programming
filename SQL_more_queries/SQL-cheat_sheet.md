# SQL CheatSheet

## Bases de données 🏰

### Création et Suppression
```
-- Créer une base de données
CREATE DATABASE IF NOT EXISTS database_name;

-- Supprimer une base de données
DROP DATABASE IF EXISTS database_name;

-- Utiliser une base de données
USE database_name;
```

## Tables et Structure 📚

### Création de Table
```
-- Créer une table basique
CREATE TABLE IF NOT EXISTS table_name (
    id INT,
    name VARCHAR(256)
);

-- Créer une table avec contraintes
CREATE TABLE IF NOT EXISTS table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    score INT DEFAULT 0,
    email VARCHAR(256) UNIQUE
);
```

## Contraintes et Types de Données 🔒

### Types Courants
- INT : Nombres entiers
- VARCHAR(n) : Chaînes de caractères variables
- TEXT : Texte long
- DATE : Date
- BOOLEAN : Vrai/Faux

### Contraintes
- PRIMARY KEY : Clé primaire unique
- FOREIGN KEY : Clé étrangère pour les relations
- NOT NULL : Valeur obligatoire
- UNIQUE : Valeur unique
- DEFAULT : Valeur par défaut
- AUTO_INCREMENT : Incrémentation automatique

## Manipulation des Données 🎯

### SELECT - Lecture
```
-- Sélectionner toutes les colonnes
SELECT * FROM table_name;

-- Sélectionner des colonnes spécifiques
SELECT column1, column2 FROM table_name;

-- Filtrer avec WHERE
SELECT * FROM table_name WHERE condition;

-- Trier avec ORDER BY
SELECT * FROM table_name ORDER BY column_name DESC;

-- Grouper avec GROUP BY
SELECT column, COUNT(*) FROM table_name GROUP BY column;
```

### INSERT - Création
```
-- Insérer une ligne
INSERT INTO table_name (column1, column2) VALUES (value1, value2);

-- Insérer plusieurs lignes
INSERT INTO table_name (column1, column2) VALUES 
    (value1, value2),
    (value3, value4);
```

### UPDATE - Modification
```
-- Mettre à jour des données
UPDATE table_name SET column1 = value1 WHERE condition;
```

### DELETE - Suppression
```
-- Supprimer des données
DELETE FROM table_name WHERE condition;
```

## Jointures et Relations 👻

### Types de JOIN
```
-- INNER JOIN
SELECT * FROM table1
JOIN table2 ON table1.id = table2.table1_id;

-- LEFT JOIN
SELECT * FROM table1
LEFT JOIN table2 ON table1.id = table2.table1_id;

-- Sous-requêtes
SELECT * FROM table1 WHERE id IN (
    SELECT table1_id FROM table2 WHERE condition
);
```

## Gestion des Utilisateurs 👑

### Création et Privilèges
```
-- Créer un utilisateur
CREATE USER IF NOT EXISTS 'user'@'localhost' IDENTIFIED BY 'password';

-- Donner tous les privilèges
GRANT ALL PRIVILEGES ON database_name.* TO 'user'@'localhost';

-- Donner des privilèges spécifiques
GRANT SELECT ON database_name.* TO 'user'@'localhost';

-- Appliquer les changements
FLUSH PRIVILEGES;
```

## Fonctions Utiles 🌟

### Agrégation
```
-- Compter
SELECT COUNT(*) FROM table_name;

-- Moyenne
SELECT AVG(column) FROM table_name;

-- Maximum
SELECT MAX(column) FROM table_name;

-- Minimum
SELECT MIN(column) FROM table_name;
```