import csv
import matplotlib.pyplot as plt
import numpy as np

path = "data/Y_train_CVw08PX.csv"
file = open('data/Y_filtre.csv', 'w', newline='')
doc_y = open('data/Y_filtre.csv', 'r', encoding='utf-8')
doc_x = open('data/X_train_update.csv', 'r', encoding='utf-8')
file_X = open('data/X_filtre.csv', 'w', newline='', encoding='utf-8')
x_filtre_open = open('data/X_filtre.csv', 'r', encoding='utf-8')
x_eval_writer = open('data/X_eval.csv', 'w', newline='', encoding='utf-8')
x_eval_open = open('data/X_eval.csv', 'r', encoding='utf-8')
y_eval_writer = open('data/Y_eval.csv', 'w', newline='', encoding='utf-8')


def filtrage_csv(path):
    """
    prend un fichier csv en entrée de data de sortie et retourne pour chaque catégorie les elements dedans avec un maximum de 2000 élements
    """
    res = {}
    with open(path, 'r') as f:
        obj = csv.reader(f)

        for i in obj:
            if i[0] == "":
                continue
            a = int(i[0])
            b = int(i[1])
            if b in res:
                if len(res[b]) < 2000:
                    res[b].append(a)
            else:
                res[b] = [a]
    return(res)


def importation_csv(file, filtre):
    """ Importe dans le fichier csv file les éléments du dictionnaire filtre"""
    with file:
        writer = csv.writer(file)
        for obj in filtre:
            l = filtre[obj]
            for i in l:
                writer.writerow([i, obj])


filtre = filtrage_csv(path)
importation_csv(file, filtre)


def lien_doc(doc_x, doc_y):
    """Renvoie la liste des lignes de doc_x correspondant à l'ID dans doc_y"""
    liste = []
    content = []
    with doc_y as f:
        obj = csv.reader(f)
        for i in obj:
            liste.append(i[0])
    with doc_x as x:
        obj_x = csv.reader(x)

        for i in obj_x:
            for j in liste:
                if i[0] == j:
                    content.append(i)
    return content


content = lien_doc(doc_x, doc_y)


def importation_csv_X(file, content):
    with file:
        writer = csv.writer(file)
        for obj in content:
            writer.writerow(obj)


importation_csv_X(file_X, content)


def separation_csv(doc, fileto):
    """Permet de séparer un fichier csv en 10%/90% où les 10% vont dans le fichier fileto"""
    count = 0
    liste = []
    with doc as f:
        reader = csv.reader(f)
        for obj in reader:
            while count < 4600:
                """ 4600 représente 10% de X_filtre"""
                liste.append(obj)
                count += 1
    with fileto as w:
        writer = csv.writer(w)
        for obj in liste:
            writer.writerow(obj)


def harmonisation(path):
    """
    prend un fichier csv en entrée de data de sortie et retourne pour chaque catégorie le nombre d'elements dedans avec une borne à 2000
    """
    res = {}
    with open(path, 'r') as f:
        obj = csv.reader(f)

        for i in obj:
            if i[0] == "":
                continue
            a = int(i[0])
            b = int(i[1])
            if b in res:
                if res[b] < 2000:
                    res[b] += 1
            else:
                res[b] = 1
    return(res)


def classe_cat(path):
    """
    prend un fichier csv en entrée de data de sortie et retourne pour chaque catégorie le nombre d'elements dedans
    """
    res = {}
    with open(path, 'r') as f:
        obj = csv.reader(f)

        for i in obj:
            if i[0] == "":
                continue
            a = int(i[0])
            b = int(i[1])
            if b in res:
                res[b] += 1
            else:
                res[b] = 1
    return(res)


res = harmonisation(path)
non_harmonise = classe_cat(path)

keys = res.keys()
keys_nh = non_harmonise.keys()
first_x = []
first_y = []
sc_x = []
sc_y = []
first_X = []
sc_X = []
width = 0.3

for i in keys:
    first_y.append(res[i])
    first_x.append(i)

for i in keys_nh:
    sc_y.append(non_harmonise[i])
    sc_x.append(i)

for i in first_x:
    first_X.append(str(i))

for i in sc_x:
    sc_X.append(str(i))


plt.figure('')
plt.bar(sc_X, sc_y, width, color='b')
plt.title('Nombre de doc dans chaque catégorie sans filtrage')
plt.yticks(np.arange(0, 10000, 1000))
"""plt.show()"""


fig = plt.figure()
plt.bar(first_X, first_y, width, color='r')
plt.title('Nombre de doc dans chaque catégorie avec filtrage')
plt.yticks(np.arange(0, 10000, 1000))
"""plt.show()"""
