<<<<<<<< Updated upstream:Seance4main.py
#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats

# C'est la partie la plus importante dans l'analyse de données. D'une part, elle n'est pas simple à comprendre tant mathématiquement que pratiquement. D'autre, elle constitue une application des probabilités. L'idée consiste à comparer une distribution de probabilité (théorique) avec des observations concrètes. De fait, il faut bien connaître les distributions vues dans la séance précédente afin de bien pratiquer cette comparaison. Les probabilités permettent de définir une probabilité critique à partir de laquelle les résultats ne sont pas conformes à la théorie probabiliste.
# Il n'est pas facile de proposer des analyses de données uniquement dans un cadre univarié. Vous utiliserez la statistique inférentielle principalement dans le cadre d'analyses multivariées. La statistique univariée est une statistique descriptive. Bien que les tests y soient possibles, comprendre leur intérêt et leur puissance d'analyse dans un tel cadre peut être déroutant.
# Peu importe dans quelle théorie vous êtes, l'idée de la statistique inférentielle est de vérifier si ce que vous avez trouvé par une méthode de calcul est intelligent ou stupide. Est-ce que l'on peut valider le résultat obtenu ou est-ce que l'incertitude qu'il présente ne permet pas de conclure ? Peu importe également l'outil, à chaque mesure statistique, on vous proposera un test pour vous aider à prendre une décision sur vos résultats. Il faut juste être capable de le lire.

# Par convention, on place les fonctions locales au début du code après les bibliothèques.
def ouvrirUnFichier(nom):
    with open(nom, "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

# Question 1 : Théorie de l'échantillonnage (intervalles de fluctuation)
# L'échantillonnage se base sur la répétitivité.
print("Question 1")

donnees = ouvrirUnFichier("src/data/Echantillonnage-100-Echantillons.csv")
print(donnees)

moyenne_pour =  round(donnees["Pour"].mean())
moyenne_contre =  round(donnees["Contre"].mean())
moyenne_sansopinion =  round(donnees["Sans opinion"].mean())

print("Moyenne pour : ", moyenne_pour)
print("Moyenne contre : ", moyenne_contre)
print("Moyenne sans opinion : ", moyenne_sansopinion)

somme_moyennes = moyenne_pour + moyenne_contre + moyenne_sansopinion
print ("La somme des trois moyennes est", somme_moyennes)

freq_pour = round(moyenne_pour / somme_moyennes, 2)
freq_contre = round(moyenne_contre / somme_moyennes, 2)
freq_sans = round(moyenne_sansopinion / somme_moyennes, 2)

print("La fréquence de Pour est", freq_pour)
print("La fréquence de Contre est", freq_contre)
print("La fréquence de Sans opinion est", freq_sans)

population_mère = 2185
freq_Pour_population_mere = round(852 / population_mère, 2)
freq_Contre_population_mere = round(911 / population_mère, 2)
freq_Sansopinion_population_mere = round(422 / population_mère, 2)

print("La fréquence de Pour dans la population mère est", freq_Pour_population_mere)
print("La fréquence de Contre dans la population mère est", freq_Contre_population_mere)
print("La fréquence de Sans opinion dans la population mère est", freq_Sansopinion_population_mere)

zc = 1.96
n = somme_moyennes
p_pour = 852 / population_mère
p_contre = 911 / population_mère
p_sans = 422 / population_mère

Intervalle_fluctuation_pour = round(p_pour - zc * math.sqrt((p_pour * (1 - p_pour)) / n), 2), round(p_pour + zc * math.sqrt((p_pour * (1 - p_pour)) / n), 2)
Intervalle_fluctuation_contre = round(p_contre - zc * math.sqrt((p_contre * (1 - p_contre)) / n), 2), round(p_contre + zc * math.sqrt((p_contre * (1 - p_contre)) / n), 2)
Intervalle_fluctuation_sans = round(p_sans - zc * math.sqrt((p_sans * (1 - p_sans)) / n), 2), round(p_sans + zc * math.sqrt((p_sans * (1 - p_sans)) / n), 2)

print("Résultat sur le calcul d'un intervalle de fluctuation")

print("Intervalle de fluctuation pour :", Intervalle_fluctuation_pour)
print("Intervalle de fluctuation contre :", Intervalle_fluctuation_contre)
print("Intervalle de fluctuation sans opinion :", Intervalle_fluctuation_sans)

# Question 2 : Théorie de l'estimation (intervalles de confiance)
#L'estimation se base sur l'effectif.
print("Question 2")
print("Résultat sur le calcul d'un intervalle de confiance")

premier_echantillon = list(donnees.iloc[0])
print("Premier échantillon :", premier_echantillon)

n_echantillon = sum(premier_echantillon)
print("Taille de l'échantillon :", n_echantillon)

freq_pour = premier_echantillon[0] / n_echantillon
freq_contre = premier_echantillon[1] / n_echantillon
freq_sans = premier_echantillon[2] / n_echantillon

print("Fréquence Pour :", round(freq_pour, 2))
print("Fréquence Contre :", round(freq_contre, 2))
print("Fréquence Sans opinion :", round(freq_sans, 2))

IntervalleConfiance_pour = round(freq_pour - zc * math.sqrt((freq_pour * (1 - freq_pour)) / n_echantillon), 2), round(freq_pour + zc * math.sqrt((freq_pour * (1 - freq_pour)) / n_echantillon), 2)
IntervalleConfiance_contre = round(freq_contre - zc * math.sqrt((freq_contre * (1 - freq_contre)) / n_echantillon), 2), round(freq_contre + zc * math.sqrt((freq_contre * (1 - freq_contre)) / n_echantillon), 2)
IntervalleConfiance_sans = round(freq_sans - zc * math.sqrt((freq_sans * (1 - freq_sans)) / n_echantillon), 2), round(freq_sans + zc * math.sqrt((freq_sans * (1 - freq_sans)) / n_echantillon), 2)

print("Intervalle de confiance pour :", IntervalleConfiance_pour)
print("Intervalle de confiance contre :", IntervalleConfiance_contre)
print("Intervalle de confiance sans opinion :", IntervalleConfiance_sans)


# Question 3 : Théorie de la décision (tests d'hypothèse)
# La décision se base sur la notion de risques alpha et bêta.
# Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
print("Question 3")
print("Théorie de la décision")

test1 = ouvrirUnFichier("src/data/Loi-normale-Test-1.csv")
test2 = ouvrirUnFichier("src/data/Loi-normale-Test-2.csv")
print(test1)
print(test2)

resultat1 = scipy.stats.shapiro(test1["Test"])
resultat2 = scipy.stats.shapiro(test2["Test"])
print("Test 1 :", resultat1)
print("Test 2 :", resultat2)

alpha = 0.05

print("Test 1 : W =", round(resultat1.statistic, 3), "; p-value =", resultat1.pvalue)
if resultat1.pvalue > alpha:
    print("Test 1 : on garde H0, distribution normale")
else:
    print("Test 1 : on rejette H0, distribution non normale")

print("Test 2 : W =", round(resultat2.statistic, 3), "; p-value =", resultat2.pvalue)
if resultat2.pvalue > alpha:
    print("Test 2 : on garde H0, distribution normale")
else:
    print("Test 2 : on rejette H0, distribution non normale")

print(test1["Test"].value_counts().sort_index())
print(test2["Test"].value_counts().sort_index())

# Question bonus
print("Question bonus")

import numpy as np

effectifs = test2["Test"].value_counts()

print("Effectifs des différentes valeurs :")
print(effectifs)


somme_effectifs = effectifs.sum()

frequences = effectifs / somme_effectifs

print("Fréquences des différentes valeurs :")
print(frequences)

rangs = np.arange(1, len(frequences) + 1)

print("Rangs :")
print(rangs)

somme_harmonique = 0

for rang in rangs:
    somme_harmonique = somme_harmonique + 1 / rang

K = 1 / somme_harmonique

print("K (Zipf pur) :", round(K, 3))

frequence_rang_1_prevue = K
frequence_rang_1_observee = frequences.iloc[0]

print(
    "Fréquence du rang 1 prévue par Zipf pur :",
    round(frequence_rang_1_prevue, 3)
)

print(
    "Fréquence du rang 1 observée :",
    round(frequence_rang_1_observee, 3)
)

pente, ordonnee = np.polyfit(
    np.log(rangs),
    np.log(frequences),
    1
)

c = -pente

========
#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats

# C'est la partie la plus importante dans l'analyse de données. D'une part, elle n'est pas simple à comprendre tant mathématiquement que pratiquement. D'autre, elle constitue une application des probabilités. L'idée consiste à comparer une distribution de probabilité (théorique) avec des observations concrètes. De fait, il faut bien connaître les distributions vues dans la séance précédente afin de bien pratiquer cette comparaison. Les probabilités permettent de définir une probabilité critique à partir de laquelle les résultats ne sont pas conformes à la théorie probabiliste.
# Il n'est pas facile de proposer des analyses de données uniquement dans un cadre univarié. Vous utiliserez la statistique inférentielle principalement dans le cadre d'analyses multivariées. La statistique univariée est une statistique descriptive. Bien que les tests y soient possibles, comprendre leur intérêt et leur puissance d'analyse dans un tel cadre peut être déroutant.
# Peu importe dans quelle théorie vous êtes, l'idée de la statistique inférentielle est de vérifier si ce que vous avez trouvé par une méthode de calcul est intelligent ou stupide. Est-ce que l'on peut valider le résultat obtenu ou est-ce que l'incertitude qu'il présente ne permet pas de conclure ? Peu importe également l'outil, à chaque mesure statistique, on vous proposera un test pour vous aider à prendre une décision sur vos résultats. Il faut juste être capable de le lire.

# Par convention, on place les fonctions locales au début du code après les bibliothèques.
def ouvrirUnFichier(nom):
    with open(nom, "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

# Question 1 : Théorie de l'échantillonnage (intervalles de fluctuation)
# L'échantillonnage se base sur la répétitivité.
print("Question 1")

donnees = ouvrirUnFichier("src/data/Echantillonnage-100-Echantillons.csv")
print(donnees)

moyenne_pour =  round(donnees["Pour"].mean())
moyenne_contre =  round(donnees["Contre"].mean())
moyenne_sansopinion =  round(donnees["Sans opinion"].mean())

print("Moyenne pour : ", moyenne_pour)
print("Moyenne contre : ", moyenne_contre)
print("Moyenne sans opinion : ", moyenne_sansopinion)

somme_moyennes = moyenne_pour + moyenne_contre + moyenne_sansopinion
print ("La somme des trois moyennes est", somme_moyennes)

freq_pour = round(moyenne_pour / somme_moyennes, 2)
freq_contre = round(moyenne_contre / somme_moyennes, 2)
freq_sans = round(moyenne_sansopinion / somme_moyennes, 2)

print("La fréquence de Pour est", freq_pour)
print("La fréquence de Contre est", freq_contre)
print("La fréquence de Sans opinion est", freq_sans)

population_mère = 2185
freq_Pour_population_mere = round(852 / population_mère, 2)
freq_Contre_population_mere = round(911 / population_mère, 2)
freq_Sansopinion_population_mere = round(422 / population_mère, 2)

print("La fréquence de Pour dans la population mère est", freq_Pour_population_mere)
print("La fréquence de Contre dans la population mère est", freq_Contre_population_mere)
print("La fréquence de Sans opinion dans la population mère est", freq_Sansopinion_population_mere)

zc = 1.96
n = somme_moyennes
p_pour = 852 / population_mère
p_contre = 911 / population_mère
p_sans = 422 / population_mère

Intervalle_fluctuation_pour = round(p_pour - zc * math.sqrt((p_pour * (1 - p_pour)) / n), 2), round(p_pour + zc * math.sqrt((p_pour * (1 - p_pour)) / n), 2)
Intervalle_fluctuation_contre = round(p_contre - zc * math.sqrt((p_contre * (1 - p_contre)) / n), 2), round(p_contre + zc * math.sqrt((p_contre * (1 - p_contre)) / n), 2)
Intervalle_fluctuation_sans = round(p_sans - zc * math.sqrt((p_sans * (1 - p_sans)) / n), 2), round(p_sans + zc * math.sqrt((p_sans * (1 - p_sans)) / n), 2)

print("Résultat sur le calcul d'un intervalle de fluctuation")

print("Intervalle de fluctuation pour :", Intervalle_fluctuation_pour)
print("Intervalle de fluctuation contre :", Intervalle_fluctuation_contre)
print("Intervalle de fluctuation sans opinion :", Intervalle_fluctuation_sans)

# Question 2 : Théorie de l'estimation (intervalles de confiance)
#L'estimation se base sur l'effectif.
print("Question 2")
print("Résultat sur le calcul d'un intervalle de confiance")

premier_echantillon = list(donnees.iloc[0])
print("Premier échantillon :", premier_echantillon)

n_echantillon = sum(premier_echantillon)
print("Taille de l'échantillon :", n_echantillon)

freq_pour = premier_echantillon[0] / n_echantillon
freq_contre = premier_echantillon[1] / n_echantillon
freq_sans = premier_echantillon[2] / n_echantillon

print("Fréquence Pour :", round(freq_pour, 2))
print("Fréquence Contre :", round(freq_contre, 2))
print("Fréquence Sans opinion :", round(freq_sans, 2))

IntervalleConfiance_pour = round(freq_pour - zc * math.sqrt((freq_pour * (1 - freq_pour)) / n_echantillon), 2), round(freq_pour + zc * math.sqrt((freq_pour * (1 - freq_pour)) / n_echantillon), 2)
IntervalleConfiance_contre = round(freq_contre - zc * math.sqrt((freq_contre * (1 - freq_contre)) / n_echantillon), 2), round(freq_contre + zc * math.sqrt((freq_contre * (1 - freq_contre)) / n_echantillon), 2)
IntervalleConfiance_sans = round(freq_sans - zc * math.sqrt((freq_sans * (1 - freq_sans)) / n_echantillon), 2), round(freq_sans + zc * math.sqrt((freq_sans * (1 - freq_sans)) / n_echantillon), 2)

print("Intervalle de confiance pour :", IntervalleConfiance_pour)
print("Intervalle de confiance contre :", IntervalleConfiance_contre)
print("Intervalle de confiance sans opinion :", IntervalleConfiance_sans)


# Question 3 : Théorie de la décision (tests d'hypothèse)
# La décision se base sur la notion de risques alpha et bêta.
# Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
print("Question 3")
print("Théorie de la décision")

test1 = ouvrirUnFichier("src/data/Loi-normale-Test-1.csv")
test2 = ouvrirUnFichier("src/data/Loi-normale-Test-2.csv")
print(test1)
print(test2)

resultat1 = scipy.stats.shapiro(test1["Test"])
resultat2 = scipy.stats.shapiro(test2["Test"])
print("Test 1 :", resultat1)
print("Test 2 :", resultat2)

alpha = 0.05

print("Test 1 : W =", round(resultat1.statistic, 3), "; p-value =", resultat1.pvalue)
if resultat1.pvalue > alpha:
    print("Test 1 : on garde H0, distribution normale")
else:
    print("Test 1 : on rejette H0, distribution non normale")

print("Test 2 : W =", round(resultat2.statistic, 3), "; p-value =", resultat2.pvalue)
if resultat2.pvalue > alpha:
    print("Test 2 : on garde H0, distribution normale")
else:
    print("Test 2 : on rejette H0, distribution non normale")

print(test1["Test"].value_counts().sort_index())
print(test2["Test"].value_counts().sort_index())

# Question bonus
print("Question bonus")

import numpy as np

effectifs = test2["Test"].value_counts()

print("Effectifs des différentes valeurs :")
print(effectifs)


somme_effectifs = effectifs.sum()

frequences = effectifs / somme_effectifs

print("Fréquences des différentes valeurs :")
print(frequences)

rangs = np.arange(1, len(frequences) + 1)

print("Rangs :")
print(rangs)

somme_harmonique = 0

for rang in rangs:
    somme_harmonique = somme_harmonique + 1 / rang

K = 1 / somme_harmonique

print("K (Zipf pur) :", round(K, 3))

frequence_rang_1_prevue = K
frequence_rang_1_observee = frequences.iloc[0]

print(
    "Fréquence du rang 1 prévue par Zipf pur :",
    round(frequence_rang_1_prevue, 3)
)

print(
    "Fréquence du rang 1 observée :",
    round(frequence_rang_1_observee, 3)
)

pente, ordonnee = np.polyfit(
    np.log(rangs),
    np.log(frequences),
    1
)

c = -pente

>>>>>>>> Stashed changes:Portfolio/Rendu_seance_04/main.py
print("Exposant c :", round(c, 2))