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

1. `0-lookup.py`: Fonction pour retourner la liste des attributs et méthodes d'un objet.
2. `1-my_list.py`: Classe MyList qui hérite de list avec une méthode pour imprimer la liste triée.
3. `2-is_same_class.py`: Fonction pour vérifier si un objet est exactement une instance d'une classe spécifiée.
4. `3-is_kind_of_class.py`: Fonction pour vérifier si un objet est une instance ou hérite d'une classe spécifiée.
5. `4-inherits_from.py`: Fonction pour vérifier si un objet est une instance d'une classe qui a hérité d'une classe spécifiée.
6. `5-base_geometry.py`: Classe BaseGeometry vide.
7. `6-base_geometry.py`: Classe BaseGeometry avec une méthode area() non implémentée.
8. `7-base_geometry.py`: Classe BaseGeometry avec une méthode de validation d'entier.
9. `8-rectangle.py`: Classe Rectangle qui hérite de BaseGeometry.
10. `9-rectangle.py`: Classe Rectangle avec implémentation de area() et __str__().
11. `10-square.py`: Classe Square qui hérite de Rectangle.
12. `11-square.py`: Classe Square avec __str__() personnalisé.

## Tests

Des fichiers de test sont fournis dans le répertoire `tests/`.

## Comment utiliser

Pour exécuter les tests ou utiliser les classes implémentées :

Exemple :

```bash
python3 0-main.py
```

## Auteur

[Votre nom]

## Licence

Projet réalisé dans le cadre d'un exercice éducatif.
