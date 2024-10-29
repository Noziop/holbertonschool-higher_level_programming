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

## Guide des Jointures SQL - Quand utiliser quoi ? 🔮

Les jointures SQL sont comme différents sorts pour combiner les tables de notre base de données :

- **INNER JOIN** : Utilise-le quand tu veux uniquement les données qui correspondent dans les deux tables. Par exemple, pour lister uniquement les villes qui ont un état correspondant. C'est comme chercher les fantômes qui ont à la fois un nom ET un pouvoir !

- **LEFT JOIN** : Parfait quand tu veux garder toutes les données de la table de gauche, même si elles n'ont pas de correspondance dans la table de droite. Comme quand tu veux lister tous les shows TV, même ceux qui n'ont pas encore de genre assigné.

- **RIGHT JOIN** : L'inverse du LEFT JOIN, utilise-le quand tu veux garder toutes les données de la table de droite. C'est plus rare, on préfère souvent réorganiser la requête en LEFT JOIN.

- **FULL JOIN** : Pour les cas où tu veux absolument tout garder des deux tables, même sans correspondance. C'est comme faire l'inventaire complet de ta maison !




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

## Jointures et Relations Avancées 🔮

### Types de Jointures
```
-- INNER JOIN : Uniquement les correspondances
SELECT * FROM table1
INNER JOIN table2 ON table1.id = table2.table1_id;

-- LEFT JOIN : Garde tout de la table de gauche
SELECT * FROM table1
LEFT JOIN table2 ON table1.id = table2.table1_id;

-- RIGHT JOIN : Garde tout de la table de droite
SELECT * FROM table2
RIGHT JOIN table1 ON table1.id = table2.table1_id;

-- FULL JOIN : Garde tout des deux tables
SELECT * FROM table1
FULL JOIN table2 ON table1.id = table2.table1_id;
```

### Relations Entre Tables 📚
```
-- Clé Primaire (PRIMARY KEY)
CREATE TABLE states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Clé Étrangère (FOREIGN KEY)
CREATE TABLE cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Relation Many-to-Many
CREATE TABLE show_genres (
    show_id INT,
    genre_id INT,
    PRIMARY KEY (show_id, genre_id),
    FOREIGN KEY (show_id) REFERENCES shows(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);
```

### Requêtes Complexes 🎯
```
-- Jointure Multiple
SELECT cities.name, states.name, countries.name
FROM cities
JOIN states ON cities.state_id = states.id
JOIN countries ON states.country_id = countries.id;

-- Sous-requêtes
SELECT name FROM cities 
WHERE state_id = (
    SELECT id FROM states 
    WHERE name = 'California'
);

-- Groupement avec Jointure
SELECT genres.name, COUNT(show_genres.show_id) as show_count
FROM genres
LEFT JOIN show_genres ON genres.id = show_genres.genre_id
GROUP BY genres.id;
```

### Cas d'Utilisation 🌟

1. **One-to-One** (1:1)
- Un utilisateur a un profil unique
- Utilise une clé étrangère unique

2. **One-to-Many** (1:N)
- Un état a plusieurs villes
- La clé étrangère est dans la table "many"

3. **Many-to-Many** (N:N)
- Des shows peuvent avoir plusieurs genres
- Des genres peuvent être liés à plusieurs shows
- Nécessite une table de jonction

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