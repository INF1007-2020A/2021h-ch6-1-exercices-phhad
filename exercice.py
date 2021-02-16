#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:

    if values is None:
        # TODO: demander les valeurs ici
        values = []
        while len(values)<10:
            values.append(int(input("Veuillez entrer une valeur")))

    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = []
        while (len(words)) < 2:
            words.append((input("Veuillez entrer une chaîne de caractères")))

    return sorted(words[0]) == sorted(words[1])


def contains_doubles(items: list) -> bool:
    return len(set(items)) != len(items)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_students = {}
    for key, value in student_grades.items():
        average = sum(value) / len(value)

        if len(best_students)==0 or list(best_students.values())[0] < average:
            best_students = {key: average}

    return {student_grades}


def frequence(sentence: str) -> dict:

    # TODO: Afficher les lettres les plus fréquentes
    # TODO: Retourner le tableau des lettres
    frequency = {letter: sentence.count(letter) for letter in sentence}
    sorted_keys = sorted(frequency, reverse=True, key=frequency.__getitem__())
    for key in sorted_keys:
        if frequency[key]> 5:
            print({key} + "" + {frequency[key]})
    #       Retourner le tableau de lettres
    input("Veuillez écrire une phrase")
    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    nom = input("Veuillez écrire le nom d'une recette")
    ingredient = input(" Enter la liste d'ingrédients? Séparer les ingrédients par une ,\n").split(",")
    return {nom, ingredient}



def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom = input("Veuillez écrire le nom d'une recette")
    if nom in ingredients:
        print(ingredients[nom])
    else:
        False


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
