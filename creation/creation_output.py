from sklearn import ensemble
from traitement_texte import *
from distance import *
path = "data/X_filtre.csv"  # document avec tout les docs


L = calcul_L(path)
var = hachage(L)

with open("Output.txt", "w") as text_file:
    var = str(var)
    text_file.write(var)
