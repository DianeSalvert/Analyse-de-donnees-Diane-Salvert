#coding:utf8

from nltk import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding = "utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

# Question 1
print("Question 1")
# Visualisation des données
# Pour résoudre le problème posé dans la question 1, il faut utiliser l'opérateur NaN de la bibliothèque Numpy dans une boucle.

donnees = ouvrirUnFichier ("src/data/pib-vs-energie.csv")
print(donnees.shape)
print(donnees.tail())

colonne_PIB_2022 = donnees['PIB_2022']
colonne_Utilisation_energie_2022 = donnees['Utilisation_d_energie_2022']

donnees_pib_manquantes = 0
donnees_energie_manquantes = 0
for i in range(len(donnees)):
    if np.isnan(colonne_PIB_2022[i]):
        donnees_pib_manquantes += 1
    if np.isnan(colonne_Utilisation_energie_2022[i]):
        donnees_energie_manquantes += 1

print("PIB manquants :", donnees_pib_manquantes)
print("Énergie manquante :", donnees_energie_manquantes)

# Question 2
print("Question 2")

donnees_pib_completes = []
donnees_energie_completes = []

for i in range(len(donnees)):
    if not np.isnan(colonne_PIB_2022[i]) and not np.isnan(colonne_Utilisation_energie_2022[i]):
        donnees_pib_completes.append(colonne_PIB_2022[i])
        donnees_energie_completes.append(colonne_Utilisation_energie_2022[i])


print("Nombre de données complètes :", len(donnees_pib_completes))
print("Données PIB complètes (5 premières) :", donnees_pib_completes[:5])
print("Données Énergie complètes (5 premières) :", donnees_energie_completes[:5])

# Question 3
print("Question 3")

x = donnees_pib_completes
y = donnees_energie_completes

params = scipy.stats.linregress(x, y)
pente = params[0]
ordonnee = params[1]
correlation = params[2]
pvalue = params[3]
deviationstandard = params[4]

print("Pente :", pente)
print("Ordonnée :", ordonnee)
print("Corrélation (r) :", correlation)
print("p-value :", pvalue)
print("Écart-type pente :", deviationstandard)

# Question 4
print("Question 4")

from scipy.stats import pearsonr
variable1 = list(donnees_pib_completes)
variable2 = list(donnees_energie_completes)
print(round(pearsonr(variable1, variable2)[0], 2))

# Question 5
print("Question 5")

y_modele = []
for i in range(0, len(donnees_pib_completes)):
    y_modele.append(pente * donnees_pib_completes[i] + ordonnee)

fig, plot = plt.subplots()
plot.scatter(donnees_pib_completes, donnees_energie_completes, c = "blue", s = 15, alpha = 0.7)
plot.plot(donnees_pib_completes, y_modele, color = "red")
plot.set_title("Régression linéaire entre le PIB et la consommation énergétique (2022)")
plot.set_xlabel("PIB (dollars courants)")
plot.set_ylabel("Consommation énergétique (kg équivalent pétrole)")
plt.savefig("./regression.png")
plt.show()

# Question 6
print("Question 6")

print("Résultats et graphique dans le rapport")