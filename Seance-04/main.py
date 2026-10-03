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

donnees = ouvrirUnFichier("data/Echantillonnage-100-Echantillons.csv")
print(donnees)

moyenne_pour =  round(donnees["Pour"].mean())
print("Moyenne pour : ", moyenne_pour)

moyenne_contre =  round(donnees["Contre"].mean())
print("Moyenne contre : ", moyenne_contre)

moyenne_sansopinion =  round(donnees["Sans opinion"].mean())
print("Moyenne sans opinion : ", moyenne_sansopinion)

somme_moyennes = moyenne_pour + moyenne_contre + moyenne_sansopinion
print ("La somme des trois moyennes est", somme_moyennes)

freq_pour = round(moyenne_pour / somme_moyennes, 2)
print("La fréquence de Pour est", freq_pour)

freq_contre = round(moyenne_contre / somme_moyennes, 2)
print("La fréquence de Contre est", freq_contre)

freq_sans = round(moyenne_sansopinion / somme_moyennes, 2)
print("La fréquence de Sans opinion est", freq_sans)

population_mère = 2185
freq_Pour_population_mère = round(852 / population_mère, 2)
print("La fréquence de Pour dans la population mère est", freq_Pour_population_mère)

freq_Contre_population_mère = round(911 / population_mère, 2)
print("La fréquence de Contre dans la population mère est", freq_Contre_population_mère)

freq_Sansopinion_population_mère = round(422 / population_mère, 2)
print("La fréquence de Sans opinion dans la population mère est", freq_Sansopinion_population_mère)

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

# Question 3 : Théorie de la décision (tests d'hypothèse)
# La décision se base sur la notion de risques alpha et bêta.
# Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
print("Question 3")
print("Théorie de la décision")

# Question bonus
print("Question bonus")
