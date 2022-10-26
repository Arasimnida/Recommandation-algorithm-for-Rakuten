from Output import index_inverse
from sklearn import ensemble
from traitement.traitement_texte import *
from sklearn.linear_model import LogisticRegression
from Output import index_inverse

clf = LogisticRegression()

test_x = "data/filtre/X_eval.csv"
train_x = "data/filtre/X_filtre_final.csv"
path = "data/filtre/X_filtre.csv"

# a choisir pour savoir quels documents il faut classer
path_y = ""


def categoriseur(path):
    res = []
    with open(path, 'r') as f:
        obj = f.readlines()
        for ligne in obj:
            if ligne[1] != "prdtypecode":
                res.append(ligne[1])
    return res


if __name__ == '__main__':
    if path_y == "":
        raise "Il faut préciser path_y pour savoir quels documents on veut classer"
    X_train = creation_ensemble(index_inverse, train_x)
    X_test = creation_ensemble(index_inverse, test_x)
    Y_train = categoriseur(path_y)
    clf.fit(X_train, Y_train)
    y_pred = clf.predict(X_test)
    print(y_pred)
