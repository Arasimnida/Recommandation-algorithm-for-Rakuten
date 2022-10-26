from Output import index_inverse
from sklearn import ensemble
from traitement_texte import *
from sklearn.linear_model import LogisticRegression
from Output import index_inverse
from creation import *

clf = LogisticRegression()

train_x = "data/filtre/X_filtre_final.csv"
path = "data/filtre/X_filtre.csv"
path_y = "data/filtre/Y_filtre_final.csv"
test_x = "data/filtre/X_eval.csv"
path_y_sol = "data/filtre/Y_eval.csv"

path_2 = "data/filtre/X_filtre.csv"  # document avec tout les docs
path_y_2 = "data/filtre/Y_filtre_final.csv"  # id_doc et classes connu
train_x_2 = "data/filtre/X_eval.csv"  # doc dont class a deviner (on connait)
# doc dont class a deviner qu'on connait ap
train_y_2 = "data/filtre/Y_eval.csv"
k = 20  # nombre de plus proche voisin a connnaitre


def categoriseur(path):
    res = []
    with open(path, 'r') as f:
        obj = f.readlines()
        for ligne in obj:
            if ligne[1] != "prdtypecode":
                res.append(ligne[1])
    return res


print("quel modèle voulez vous utiliser ? Pour le modèle des plus proche voisin taper 1 et 2 pour celui de la regression logistique")
a = input()

if a == '1':
    ensemble_vecteur = creation_ensemble(index_inverse, path)
    vecteur_a_classer = creation_ensemble(index_inverse, train_x)
    id_vecteur_a_classer = obtenir_id(train_x)
    classes = []
    for x in vecteur_a_classer:
        ppv = proche_voisin(euclidienne, x, ensemble_vecteur, k)
        classes.append(trouver_class_ppv(ppv, path_y))
    l = obtenir_id(path_y_2)
    createurcsv(id_vecteur_a_classer, l)
    print("Il faut maintenant lancer le fichier calcul_metricf1 avec le fichier qui vient d'être créer.")

elif a == '2':
    id_vecteur_a_classer = obtenir_id(train_x)
    X_train = creation_ensemble(index_inverse, train_x)
    X_test = creation_ensemble(index_inverse, test_x)
    Y_train = categoriseur(path_y)
    y = categoriseur(path_y_sol)
    clf.fit(X_train, Y_train)
    y_pred = clf.predict(X_test)
    createurcsv(id_vecteur_a_classer, y_pred)
    print("Il faut maintenant lancer le fichier calcul_metricf1 avec le fichier qui vient d'être créer.")

else print("la valeur rentrée n'est pas bonne il faut réssayer")
