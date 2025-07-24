# Jour 2:30 Days of Python Programmings

#Niveau1
first_name="Esperanda"
last_name="KPONOU"
full_name=first_name+""+last_name
country="BENIN"
city="Porto-Novo"
age=22
is_married="False"
is_true="True"
is_light_on="True"

#Déclaration multiple sur une seule ligne
a,b,c=5,4,3.14

#Niveau2
#Types
print("Type de first_name:",type(first_name))
print("Type de last_name:",type(last_name))
print("Type de full_name:",type(full_name))
print("Type de age:",type(age))
print("Type de country:",type(country))
print("Type de city:",type(city))
print("Type de is_married:",type(is_married))
print("Type de is_true:",type(is_true))
print("Type de is_light_on:",type(is_light_on))
print("Type de a:",type(a))
print("Type de b:",type(b))
print("Type de c:",type(c))

#Longueur
print("Longueur du prénom:",len(first_name))
print("Longueur du nom de famille:",len(last_name))
print("Prénom plus long que nom de famille?:",len(first_name)>len(last_name))

#Calculs
num_one=5
num_two=4
total=num_one+num_two
diff=num_two-num_one
product=num_two*num_one
division=num_one/num_two
remainder=num_two%num_one
floor_division=num_one//num_two
print("Total:",total)
print("Différence:",diff)
print("Produit:",product)
print("Division:",division)
print("Reste:",remainder)
print("Division entière:",floor_division)

#Aire et Circonférence d'un cercle
pi=3.14159
rayon=30
area_of_circle=pi*rayon**2
circum_of_circle=2*pi*rayon
print("Aire du cercle:",area_of_circle)
print("Circonférence du cercle:",circum_of_circle)

#Rayon entré par un utilisateur et calcul de la zone
user_rayon=float(input("Entrez le rayon du cercle:"))
user_area=pi*user_rayon**2
print("Aire pour le rayon donné:",user_area)

#Infos utilisateur
first_name_input=input("Entrez votre prénom:")
last_name_input=input("Entrez votre nom de famille:")
country_input=input("Entrez votre pays:")
age_input=input("Entrez votre âge:")

print("Bienvenue",first_name_input,last_name_input,"du",country_input,"âgé(e) de",age_input,"ans")

#Mots-clés réservés en Python
import keyword
print("Mots-clés Python:",keyword.kwlist)

