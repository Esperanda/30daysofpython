# 1. Déclarez votre âge comme variable entière
age = 25
print("Moi, j'ai:", age , "ans.")

# 2. Déclarez votre taille en tant que variable flottante
taille = 1.68
print("Ma taille est de:", taille)

# 3. Déclarez une variable qui stocke un numéro complexe
complex_number = 3 + 5j
print("La valeur complexe est:", complex_number)

# 4. Script pour calculer l'aire d'un triangle
base = float(input("Entrez la base du triangle: "))
hauteur = float(input("Entrez la hauteur du triangle: "))
area_triangle = 0.5 * base * hauteur
print("La zone du triangle est de", area_triangle)

# 5. Script pour calculer le périmètre du triangle
a = float(input("Entrez le côté A: "))
b = float(input("Entrez le côté B: "))
c = float(input("Entrez le côté C: "))
perimetre = a + b + c
print("Le périmètre du triangle est", perimetre)

# 6. Surface et périmètre d’un rectangle
longueur = float(input("Entrez la longueur du rectangle: "))
largeur = float(input("Entrez la largeur du rectangle: "))
surface_rectangle = longueur * largeur
perimetre_rectangle = 2 * (longueur + largeur)
print("Surface:", surface_rectangle)
print("Périmètre:", perimetre_rectangle)
# day_3/exercices.py

# 7. Rayon d’un cercle - calcul de la surface et de la circonférence
import math

rayon = float(input("Entrez le rayon du cercle: "))
area_cercle = math.pi * rayon ** 2
circumference_cercle = 2 * math.pi * rayon

print("Aire du cercle:", area_cercle)
print("Circonférence du cercle:", circumference_cercle)

# 8. Calcul de la pente, ordonnée X et ordonnée y de y = 2x - 2
x = float(input("Entrez la valeur de x: "))
y = 2 * x - 2
print("La valeur de y est :", y)

# 9. Trouver la pente et la distance euclidienne entre les points (2, 2) et (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calcul de la pente
pente = (y2 - y1) / (x2 - x1)
print("La pente est :", pente)

# Calcul de la distance euclidienne
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("La distance euclidienne est :", distance)

# 10. Comparaison des pentes dans les tâches 8 et 9
if pente == (2):  # Valeur de pente de la fonction y = 2x - 2
    print("La pente est la même.")
else:
    print("Les pentes sont différentes.")

# 11. Calcul de la valeur de y dans l’équation y = x^2 + 6x + 9 pour différentes valeurs de x
x_val = float(input("Entrez la valeur de x pour calculer y: "))
y_val = x_val ** 2 + 6 * x_val + 9
print("La valeur de y est :", y_val)

# 12. Longueur de "Python" et "Dragon" et comparaison falsy
longueur_python = len("Python")
longueur_dragon = len("Dragon")
print("Longueur de 'Python':", longueur_python)
print("Longueur de 'Dragon':", longueur_dragon)

if longueur_python != longueur_dragon:
    print("Les longueurs de 'Python' et 'Dragon' ne sont pas égales.")
else:
    print("Les longueurs de 'Python' et 'Dragon' sont égales.")

# 13. Utiliser l’opérateur "and" pour vérifier si 'on' est dans 'python' et 'dragon'
if 'on' in 'python' and 'on' in 'dragon':
    print("'on' est présent dans 'python' et 'dragon'")
else:
    print("'on' n'est pas présent dans 'python' et 'dragon'")

# 14. Vérifiez si "jargon" est dans la phrase
phrase = "I hope this course is not full of jargon."
if "jargon" in phrase:
    print("'jargon' est dans la phrase.")
else:
    print("'jargon' n'est pas dans la phrase.")

# 15. Vérification qu'il n'y a pas de 'on' dans 'dragon' et 'python'
if 'on' not in 'dragon' and 'on' not in 'python':
    print("Il n'y a pas de 'on' dans 'dragon' et 'python'.")

# 16. Trouver la longueur de "python", la convertir en float puis en string
python_length = len("python")
python_length_float = float(python_length)
python_length_str = str(python_length_float)
print("Longueur de 'python' en float:", python_length_float)
print("Longueur de 'python' convertie en string:", python_length_str)

# 17. Vérification si un nombre est divisible par 2 (le reste est zéro)
num = int(input("Entrez un nombre pour vérifier s'il est divisible par 2: "))
if num % 2 == 0:
    print(f"{num} est divisible par 2.")
else:
    print(f"{num} n'est pas divisible par 2.")

# 18. Vérifier si la division de plancher de 7 par 3 est égale à la valeur convertie en int de 2.7
if 7 // 3 == int(2.7):
    print("La division de plancher de 7 par 3 est égale à la valeur convertie de 2.7.")
else:
    print("La division de plancher de 7 par 3 n'est pas égale à la valeur convertie de 2.7.")

# 19. Vérifier si le type de "10" est égal au type de 10
if type("10") == type(10):
    print("Le type de '10' est égal au type de 10.")
else:
    print("Le type de '10' n'est pas égal au type de 10.")

# 20. Vérifier si int('9.8') est égal à 10
if int(float('9.8')) == 10:
    print("int('9.8') est égal à 10.")
else:
    print("int('9.8') n'est pas égal à 10.")

# 21. Calculer la rémunération hebdomadaire d'une personne
heures = float(input("Entrez le nombre d'heures travaillées: "))
taux_par_heure = float(input("Entrez le taux par heure: "))
rémunération = heures * taux_par_heure
print("Votre gain hebdomadaire est de :", rémunération)

# 22. Calculer le nombre de secondes qu'une personne peut vivre
années = int(input("Entrez le nombre d'années que vous avez vécu: "))
secondes = années * 365 * 24 * 60 * 60
print(f"Vous avez vécu pendant {secondes} secondes.")

# 23. Afficher un tableau spécifique
for i in range(1, 6):
    print(f"{i}\t{i*i}\t{i*i*i}")