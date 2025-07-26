# day_4/exercices.py

# 1. Concaténer la chaîne "trente", "jours", "de", "python"
chaine1 = "trente" + " " + "jours" + " " + "de" + " " + "python"
print(chaine1)

# 2. Concaténer la chaîne "codage", "pour", "all"
chaine2 = "codage" + " " + "pour" + " " + "tous"
print(chaine2)

# 3. Déclarez une variable nommée société et attribuez-lui la valeur "codage pour tous"
societe = "codage pour tous"

# 4. Imprimez la variable société
print(societe)

# 5. Imprimez la longueur de la chaîne de l'entreprise
print("Longueur de la société:", len(societe))

# 6. Changez tous les caractères en majuscules
print(societe.upper())

# 7. Changez tous les caractères en minuscules
print(societe.lower())

# 8. Utilisez des méthodes capitalize(), title(), swapcase() pour formater la valeur de la chaîne
chaine = "coding for all"
print(chaine.capitalize())  # Première lettre en majuscule
print(chaine.title())       # Première lettre de chaque mot en majuscule
print(chaine.swapcase())    # Inverse la casse

# 9. Trancher sur le premier mot de la chaîne "Coding For All"
first_word = chaine.split()[0]
print("Premier mot:", first_word)

# 10. Vérifiez si la chaîne "Coding For All" contient "coding" en utilisant l'index ou find()
if "coding" in chaine:
    print("'coding' est présent dans la chaîne.")
else:
    print("'coding' n'est pas dans la chaîne.")

# 11. Remplacez le mot "codage" dans "codage pour tous" par "Python"
chaine3 = "codage pour tous"
chaine3 = chaine3.replace("codage", "Python")
print(chaine3)

# 12. Remplacez "Python" par "tout le monde" dans "Python pour tous"
chaine4 = "Python pour tous"
chaine4 = chaine4.replace("Python", "tout le monde")
print(chaine4)

# 13. Divisez la chaîne "codage pour tous" en utilisant l'espace comme séparateur
words = "codage pour tous".split()
print(words)

# 14. Diviser "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" sur la virgule
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", ")
print(companies)

# 15. Quel est le caractère à l'index 0 dans la chaîne "Coding For All"
first_char = "Coding For All"[0]
print("Caractère à l'index 0:", first_char)

# 16. Quel est le dernier index de la chaîne "Coding For All"
last_index = len("Coding For All") - 1
print("Dernier index:", last_index)

# 17. Quel caractère est à l'index 10 dans la chaîne "codage pour tous"
char_at_index_10 = "codage pour tous"[10]
print("Caractère à l'index 10:", char_at_index_10)

# 18. Créez un acronyme pour "Python pour tout le monde"
acronyme1 = "".join([mot[0].upper() for mot in "Python pour tout le monde".split()])
print("Acronyme:", acronyme1)

# 19. Créez un acronyme pour "codage pour tous"
acronyme2 = "".join([mot[0].upper() for mot in "codage pour tous".split()])
print("Acronyme:", acronyme2)

# 20. Utilisez index() pour déterminer la position de la première occurrence de "C" dans "codage pour tous"
if "C" in "codage pour tous":
    index_C = "codage pour tous".index("C")
    print("Index de 'C':", index_C)
else:
    print("'C' n'est pas présent dans la chaîne.")

# 21. Utilisez index() pour déterminer la position de la première occurrence de "F" dans "codage pour tous"
if "F" in "codage pour tous":
    index_F = "codage pour tous".index("F")
    print("Index de 'F':", index_F)
else:
    print("'F' n'est pas présent dans la chaîne.")


# 22. Utilisez rfind() pour trouver la position de la dernière occurrence de "L"
index_L = "codage pour tous".rfind("L")
print("Position de la dernière occurrence de 'L':", index_L)

# 23. Utilisez index() ou find() pour trouver la position de la première occurrence de "parce que" dans une phrase
phrase = "Vous ne pouvez pas mettre fin à une phrase avec parce que parce que c'est une conjonction"
index_pourquoi = phrase.find("parce que")
print("Position de la première occurrence de 'parce que':", index_pourquoi)

# 24. Utilisez rindex() pour trouver la position de la dernière occurrence de "car"

if "car" in phrase:
    index_car = phrase.rindex("car")
    print("Position de la dernière occurrence de 'car':", index_car)
else:
    print("'car' n'est pas présent dans la phrase.")


# 25. Trancher l'expression "parce que parce que" dans la phrase
tranche = phrase[33:52]  # "parce que parce que"
print("Trancher l'expression:", tranche)

# 26. Trouvez la position de la première occurrence du mot "parce que"
position_parce_que = phrase.find("parce que")
print("Position de 'parce que' dans la phrase:", position_parce_que)

# 27. Trancher l'expression "parce que parce que" à partir de la phrase
tranche_2 = phrase[33:52]  # "parce que parce que"
print("Trancher l'expression encore:", tranche_2)

# 28. "codage pour tous" commence-t-il par "Coding"?
starts_with_coding = "codage pour tous".startswith("Coding")
print("Commence-t-il par 'Coding'?", starts_with_coding)

# 29. "codage pour tous" se termine-t-il par "coding"?
ends_with_coding = "codage pour tous".endswith("coding")
print("Se termine-t-il par 'coding'?", ends_with_coding)

# 30. Retirer les espaces de fuite gauche et droit dans la chaîne " codage pour tous "
chaine_espaces = " codage pour tous ".strip()
print("Chaîne après avoir retiré les espaces:", chaine_espaces)

# 31. Méthode isidentifier()
var1 = "30daysofpython"
var2 = "Thirty_days_of_python"
print(f"'{var1}' est un identifiant valide?", var1.isidentifier())
print(f"'{var2}' est un identifiant valide?", var2.isidentifier())

# 32. Rejoindre la liste des bibliothèques Python
bibliotheques = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
joined_bibliotheques = " ".join(bibliotheques)
print("Bibliothèques:", joined_bibliotheques)

# 33. Utilisez la séquence d'échappement de ligne pour séparer les phrases
phrase1 = "J'apprécie ce défi."
phrase2 = "Je me demande juste quelle est la prochaine étape."
print(phrase1 + "\n" + phrase2)

# 34. Utilisez une séquence d'échappement d'onglet pour écrire les lignes suivantes
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35. Utilisez la méthode de formatage de chaîne
RADIUS = 10
area_of_circle = 3.14 * RADIUS ** 2
print(f"La zone d'un cercle avec le rayon {RADIUS} est de {area_of_circle} mètres carrés.")

# 36. Faites les calculs avec des méthodes de formatage de chaîne
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")