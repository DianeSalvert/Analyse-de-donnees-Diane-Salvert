#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math

def ouvrirUnFichier(nom):
    with open(nom, "r", encoding='utf-8') as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

def conversionLog(liste):
    log = []
    for element in liste:
        log.append(math.log(element))
    return log

def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(0, len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(0, len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop

def classementPays(ordre1, ordre2):
    classement = []
    if len(ordre1) <= len(ordre2):
        for element1 in range(0, len(ordre2) - 1):
            for element2 in range(0, len(ordre1) - 1):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1) - 1):
            for element2 in range(0, len(ordre2) - 1):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element][1]])
    return classement

# Question 2
print("Question 2")

tableau = ouvrirUnFichier("src/data/island-index.csv")
print (tableau.head())
print (tableau.columns)

# Question 3
print("Question 3")

colonneSurface = list(tableau["Surface (km²)"])
colonneSurface.append(float(85545323)) #Asie/Af/Eur
colonneSurface.append(float(37856841)) #Ame
colonneSurface.append(float(7768030)) #Antarctique
colonneSurface.append(float(7605049)) #Australie

print("Nombre de surfaces :", len(colonneSurface))
print("Plus grande surface :", max(colonneSurface))

# Question 4
print("Question 4")

tableau2 = ordreDecroissant(colonneSurface)
print ("Début du nouveau tableau :", tableau2[:3])
print ("Fin du nouveau tableau :", tableau2[-3:])

# Question 5
print("Question 5")

rangs = list(range(1, len(tableau2) + 1))
print("Premier rang :", rangs[0])
print("Dernier rang :", rangs[-1])

plt.plot(rangs, tableau2)
plt.xlabel("Rang")
plt.ylabel("Surface (km²)")
plt.title("Loi rang-taille des îles")
plt.savefig("src/data/loi-rang-taille-iles.png")
plt.close()

# Question 6
print("Question 6")

logSurface = conversionLog(colonneSurface)
logRangs = conversionLog(rangs)
print(logRangs[0], logRangs[-1])
print(logSurface[0])

plt.plot(logRangs, logSurface)
plt.xlabel("logRang")
plt.ylabel("logSurface (km²)")
plt.title("Loi rang-taille des îles_2")
plt.savefig("src/data/loi-rang-taille-iles_2.png")
plt.close()

# Question 7
print("Question 7")

#On sait que les tests servent à effectuer des comparaisons entre deux classements.
#Or, ici, le rang est obtenu à partir de la surface, et non d'un classement. 
#Donc corréler le rang et la surface revient à comparer le rang avec lui-même. Pour pouvoir effectuer un test, il faudrait un deuxième classement indépendant mais avec les mêmes îles.

# Question 8
print("Question 8")

# Question 9
print("Question 9")

tableau3 = ouvrirUnFichier("src/data/Etatdumonde2007-2026-LeMondeHS.csv")
print (tableau3.head())
print (tableau3.columns)

# Question 10
print("Question 10")

colonneEtat = tableau3["État"]
colonnePopulation2007 = tableau3["Pop 2007"]
colonnePopulation2026 = tableau3["Pop 2026"]
colonneDensité2007 = tableau3["Densité 2007"]
colonneDensité2026 = tableau3["Densité 2026"]

Etat = list(colonneEtat)
pop2007 = list(pd.to_numeric(colonnePopulation2007, errors="coerce"))
pop2026 = list(pd.to_numeric(colonnePopulation2026, errors="coerce"))
densité2007 = list(pd.to_numeric(colonneDensité2007, errors="coerce"))
densité2026 = list(pd.to_numeric(colonneDensité2026, errors="coerce"))

print(len(Etat))
print(pop2007[:3])
print(densité2007[:3])

# Question 11
print("Question 11")

classementPop2007 = ordrePopulation(pop2007, Etat)
classementPop2026 = ordrePopulation(pop2026, Etat)
classementDensité2007 = ordrePopulation(densité2007, Etat)
classementDensité2026 = ordrePopulation(densité2026, Etat)

print(len(classementPop2007), classementPop2007[:3])
print(len(classementPop2026), classementPop2026[:3])
print(len(classementDensité2007), classementDensité2007[:3])
print(len(classementDensité2026), classementDensité2026[:3])

# Question 12
print("Question 12")

comparaison2007 = classementPays(classementPop2007, classementDensité2007)
comparaison2007.sort()

comparaison2026 = classementPays(classementPop2026, classementDensité2026)
comparaison2026.sort()

print(len(comparaison2007), comparaison2007[:3])
print(len(comparaison2026), comparaison2026[:3])

# Question 13
print("Question 13")

rangsPop2007 = []
rangsDens2007 = []
for ligne in comparaison2007:
    rangsPop2007.append(ligne[0])
    rangsDens2007.append(ligne[1])

rangsPop2026 = []
rangsDens2026 = []
for ligne in comparaison2026:
    rangsPop2026.append(ligne[0])
    rangsDens2026.append(ligne[1])

print(len(rangsPop2007), rangsPop2007[:3], rangsDens2007[:3])
print(len(rangsPop2026), rangsPop2026[:3], rangsDens2026[:3])

# Question 14
print("Question 14")

spearman2007 = scipy.stats.spearmanr(rangsPop2007, rangsDens2007)
kendall2007 = scipy.stats.kendalltau(rangsPop2007, rangsDens2007)
print("2007 - Spearman :", spearman2007)
print("2007 - Kendall :", kendall2007)

spearman2026 = scipy.stats.spearmanr(rangsPop2026, rangsDens2026)
kendall2026 = scipy.stats.kendalltau(rangsPop2026, rangsDens2026)
print("2026 - Spearman :", spearman2026)
print("2026 - Kendall :", kendall2026)
