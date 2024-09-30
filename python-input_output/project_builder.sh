#!/bin/bash

# Créer les fichiers d'exercices avec le shebang
files=(
    "0-read_file.py"
    "1-write_file.py"
    "2-append_write.py"
    "3-to_json_string.py"
    "4-from_json_string.py"
    "5-save_to_json_file.py"
    "6-load_from_json_file.py"
    "7-add_item.py"
    "8-class_to_json.py"
    "9-student.py"
    "10-student.py"
    "11-student.py"
    "12-pascal_triangle.py"
)

for file in "${files[@]}"; do
    echo '#!/usr/bin/python3' > "$file"
done

# Créer les fichiers main avec leur contenu
cat << EOF > 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")
EOF

cat << EOF > 1-main.py
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
EOF

cat << EOF > 2-main.py
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)
EOF

cat << EOF > 3-main.py
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
EOF

cat << EOF > 4-main.py
#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = """
{"is_active": true, "info": {"age": 36, "average": 3.14}, 
"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = """
    {"is_active": true, 12 }
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
EOF

cat << EOF > 5-main.py
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
EOF

cat << EOF > 6-main.py
#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
EOF

# Créer 8-my_class.py
cat << EOF > 8-my_class.py
#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
EOF

# Créer 8-main.py
cat << EOF > 8-main.py
#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
EOF

# Créer 8-my_class_2.py
cat << EOF > 8-my_class_2.py
#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)
EOF

# Créer 8-main_2.py
cat << EOF > 8-main_2.py
#!/usr/bin/python3
MyClass = __import__('8-my_class_2').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
EOF

# Créer 9-main.py
cat << EOF > 9-main.py
#!/usr/bin/python3
Student = __import__('9-student').Student

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))
EOF

# Créer 10-main.py
cat << EOF > 10-main.py
#!/usr/bin/python3
Student = __import__('10-student').Student

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)
EOF

# Créer 11-main.py
cat << EOF > 11-main.py
#!/usr/bin/python3
import os
import sys

Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))

save_to_json_file(j_student_1, path)
read_file(path)
print("\nSaved to disk")

print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
EOF

# Créer 12-main.py
cat << EOF > 12-main.py
#!/usr/bin/python3
"""
12-main
"""
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
EOF

echo "Fichiers main pour les exercices 9, 10, 11 et 12 créés avec succès!"

# Créer le fichier README.md
cat << EOF > README.md
# Python - Input/Output

Ce projet couvre les opérations d'entrée/sortie en Python, y compris la manipulation de fichiers, la sérialisation et la désérialisation JSON.

## Fichiers

0. **0-read_file.py**: Fonction qui lit un fichier texte et l'imprime sur stdout.
1. **1-write_file.py**: Fonction qui écrit une chaîne dans un fichier texte.
2. **2-append_write.py**: Fonction qui ajoute une chaîne à la fin d'un fichier texte.
3. **3-to_json_string.py**: Fonction qui retourne la représentation JSON d'un objet.
4. **4-from_json_string.py**: Fonction qui retourne un objet Python représenté par une chaîne JSON.
5. **5-save_to_json_file.py**: Fonction qui écrit un objet dans un fichier texte en utilisant une représentation JSON.
6. **6-load_from_json_file.py**: Fonction qui crée un objet à partir d'un fichier JSON.
7. **7-add_item.py**: Script qui ajoute tous les arguments à une liste Python et les sauvegarde dans un fichier.
8. **8-class_to_json.py**: Fonction qui retourne la description du dictionnaire pour la sérialisation JSON d'un objet.
9. **9-student.py**: Classe Student qui définit un étudiant et inclut une méthode pour le convertir en JSON.
10. **10-student.py**: Version améliorée de la classe Student avec un filtre pour les attributs à récupérer.
11. **11-student.py**: Version finale de la classe Student avec des méthodes pour sauvegarder et recharger en JSON.
12. **12-pascal_triangle.py**: Fonction qui génère le triangle de Pascal.

## Utilisation

Chaque fichier peut être exécuté individuellement pour tester sa fonctionnalité. Par exemple :

\`\`\`
$ ./0-main.py
\`\`\`


## Auteur

[Votre nom]

EOF

echo "Fichiers créés avec succès!"