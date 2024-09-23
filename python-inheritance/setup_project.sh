#!/bin/bash

# Créer le répertoire tests s'il n'existe pas
mkdir -p tests

# Fonction pour créer un fichier Python avec shebang
create_python_file() {
    echo "#!/usr/bin/python3" > "$1"
    echo "# $1" >> "$1"
    echo "Creating $1"
}

# Créer les fichiers Python avec les noms spécifiques
create_python_file "0-lookup.py"
create_python_file "1-my_list.py"
create_python_file "2-is_same_class.py"
create_python_file "3-is_kind_of_class.py"
create_python_file "4-inherits_from.py"
create_python_file "5-base_geometry.py"
create_python_file "6-base_geometry.py"
create_python_file "7-base_geometry.py"
create_python_file "8-rectangle.py"
create_python_file "9-rectangle.py"
create_python_file "10-square.py"
create_python_file "11-square.py"

# Créer les fichiers de test
touch tests/1-my_list.txt
touch tests/7-base_geometry.txt

# Créer les fichiers main
cat << EOF > 0-main.py
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
EOF

cat << EOF > 1-main.py
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
EOF

cat << EOF > 2-main.py
#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
EOF

cat << EOF > 3-main.py
#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
EOF

cat << EOF > 4-main.py
#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
EOF

cat << EOF > 5-main.py
#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))
EOF

cat << EOF > 6-main.py
#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
EOF

cat << EOF > 7-main.py
#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
EOF

cat << EOF > 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
EOF

cat << EOF > 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())
EOF

cat << EOF > 10-main.py
#!/usr/bin/python3
Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())
EOF

cat << EOF > 11-main.py
#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
EOF

# Créer le README.md détaillé
cat << EOF > README.md
# Python - Inheritance

Ce projet explore le concept d'héritage en Python, un aspect fondamental de la programmation orientée objet. L'héritage permet à une classe de hériter des attributs et méthodes d'une autre classe.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer :

- Ce qu'est une superclasse, classe de base ou classe parente.
- Ce qu'est une sous-classe.
- Comment lister tous les attributs et méthodes d'une classe ou d'une instance.
- Comment hériter une classe d'une autre.
- Comment définir une classe avec plusieurs classes de base.
- Quelle est la classe par défaut dont toute classe hérite.
- Comment remplacer une méthode ou un attribut hérité de la classe de base.
- Quels attributs ou méthodes sont disponibles par héritage pour les sous-classes.
- Quel est le but de l'héritage.
- Comment utiliser les fonctions intégrées isinstance, issubclass, type et super.

## Fichiers du projet

1. \`0-lookup.py\`: Fonction pour retourner la liste des attributs et méthodes d'un objet.
2. \`1-my_list.py\`: Classe MyList qui hérite de list avec une méthode pour imprimer la liste triée.
3. \`2-is_same_class.py\`: Fonction pour vérifier si un objet est exactement une instance d'une classe spécifiée.
4. \`3-is_kind_of_class.py\`: Fonction pour vérifier si un objet est une instance ou hérite d'une classe spécifiée.
5. \`4-inherits_from.py\`: Fonction pour vérifier si un objet est une instance d'une classe qui a hérité d'une classe spécifiée.
6. \`5-base_geometry.py\`: Classe BaseGeometry vide.
7. \`6-base_geometry.py\`: Classe BaseGeometry avec une méthode area() non implémentée.
8. \`7-base_geometry.py\`: Classe BaseGeometry avec une méthode de validation d'entier.
9. \`8-rectangle.py\`: Classe Rectangle qui hérite de BaseGeometry.
10. \`9-rectangle.py\`: Classe Rectangle avec implémentation de area() et __str__().
11. \`10-square.py\`: Classe Square qui hérite de Rectangle.
12. \`11-square.py\`: Classe Square avec __str__() personnalisé.

## Tests

Des fichiers de test sont fournis dans le répertoire \`tests/\`.

## Comment utiliser

Pour exécuter les tests ou utiliser les classes implémentées :

Exemple :

\`\`\`bash
python3 0-main.py
\`\`\`

## Auteur

[Votre nom]

## Licence

Projet réalisé dans le cadre d'un exercice éducatif.
EOF

echo "All files have been created successfully!"