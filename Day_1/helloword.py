#vérifier la version de python
print("Exercice1: vérifier la version de python")
print("version de python: 3.13.5")

#Opérations avec les opérandes 3 et 4
print("3+4 =",3+4) #addition
print("3-4 =",3-4) #soustraction
print("3*4 =",3*4) #multiplication
print("3%4 =",3%4) #modulo
print("3/4 =",3/4) #division
print("3**4 =",3**4) #exponentielle
print("3//4 =",3//4) #Floor Division

#Afficher des chaînes
print("Votre nom")
print("Votre nom de famille")
print("Votre pays")
print("Je profite de 30jours de python")

#Vérification des types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh','Python','Finlande']))
print(type("Votre nom"))
print(type("Votre nom de famille"))
print(type("Votre Pays"))

#Exemples de différents types de données
#Nombres
entier = 10  #int
print("Entier:", entier, "| Type:",type(entier))
flottant = 9.5 #float
print("Décimale:", flottant, "| Type:",type(flottant))

complexe = 3 + 4j #complex
print("Complexe:", complexe, "| Type:",type(complexe))

#Chaîne
chaîne = "Hello"
print("Chaîne:", chaîne, "| Type:",type(chaîne))

#Booléen
vrai = True
print("Booléen vrai:", vrai, "| Type:",type(vrai))

faux = False
print("Booléen faux:", faux, "| Type:",type(faux))

#Liste
ma_liste = [1,2,3,4,"Python"]
print("Liste:", ma_liste, "| Type:",type(ma_liste))

#Tuple
mon_tuple = (4,5,6)
print("Tuple:",mon_tuple, "| Type:",type(mon_tuple))

#Set
mon_set = {1,2,3,3} # =>{1,2,3}
print("Set:", mon_set, "| Type:",type(mon_set))

#Dictionnaire
mon_dict = {"nom":"Esperanda" ,"métier": "Dev_Web"}
print("Dictionnaire:", mon_dict, "| Type:",type(mon_dict))


#Distance Euclidienne entre (2,3) et (10,8)

import math
x1,y1 = 2,3
x2,y2 = 10,8
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("La distance euclidienne est:", distance)
