import math
from sklearn import ensemble
import csv
import statistics
from distutils.command.clean import clean
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import spacy
import nltk
import re
import numpy as np
from numpy import linalg as la

nltk.download('stopwords')
stopWords = set(stopwords.words('french'))
nlp = spacy.load("fr_core_news_sm")
stemmer = SnowballStemmer(language='french')


def calcul_L(path):
    L = extraction_description(path)
    L_titre = extraction_titre(path)
    if len(L) != len(L_titre):
        print("erreur_longeur")
        print("len(L)" + str(len(L)))
        print("len(L_titre)" + str(len(L_titre)))
    for i in range(min(len(L_titre), len(L))):
        L[i] += L_titre[i]
    return L


def hachage(L):
    """
    retourne le dico avec les mots et leurs occurences dans chaque doc
    """
    res = {}
    for k in range(len(L)):
        for l in range(len(L[k])):
            if L[k][l] in res:
                marqueur = False
                for z in range(len(res[L[k][l]])):
                    if res[L[k][l]][z][0] == k:
                        res[L[k][l]][z][1] += 1
                        marqueur = True
                if not marqueur:
                    res[L[k][l]].append([k, 1])
            else:
                res[L[k][l]] = [[k, 1]]
    return res


def frequency(word, path):
    table = hachage(path)
    if not word in table:
        return 0
    else:
        with open(path, 'r') as f:
            obj = f.readlines()
            N = len(obj)
            a = 0
            for i in range(len(table[word])):
                a += table[word][i][1]
            return math.log(N*1./a)


def extraction_description(path):
    """prend en entrée un fichier de data et renvoie une liste des descriptions

    Args:
        path (fichier): fichier csv avec les datas

    Returns:
        liste : liste de liste de mots séparés ou chaque liste correspond a une description
    """
    import csv
    l = []
    res = []
    i = 0
    with open(path, 'r', encoding='utf-8') as f:
        obj = csv.reader(f)
        for ligne in obj:
            if ligne[2] == "":
                l.append("")
            elif ligne[2] == "description":
                continue
            else:
                l.append(ligne[2])
    for elt in l:
        elt_1 = sans_html(elt)
        elt_2 = traitement(elt_1)
        res.append(elt_2)
        i += 1
        if i//100 != (i-1)//100:
            print("ok" + str(i))
    return res


def extraction_titre(path):
    """prend en entrée un fichier de data et renvoie une liste des descriptions

    Args:
        path (fichier): fichier csv avec les datas

    Returns:
        liste : liste de liste de mots séparés ou chaque liste correspond a un titre
    """
    l = []
    res = []
    i = 0
    with open(path, 'r', encoding='utf-8') as f:
        obj = csv.reader(f)

        for ligne in obj:
            if ligne[1] == "":
                l.append("")
            elif ligne[1] == "designation":
                continue
            else:
                l.append(ligne[1])
    for elt in l:
        elt_1 = sans_html(elt)
        elt_2 = traitement(elt_1)
        res.append(elt_2)
        i += 1
        if i//100 != (i-1)//100:
            print("ok titre" + str(i))
    return res


def transformation(d, lh, keys, path):
    """transforme un docuement par un vecteur représenté dans l'espace du vocab

    Args:
        d (int): id du doc
        hachage (dict): index inversé
        path (str): lien vers le csv avec tout les docuements

    Returns:
        lst : retourne un vecteur représentant d dans l'espace du vocab
    """
    x = [0 for i in range(lh)]
    k = []
    doc = ""
    with open(path, 'r', encoding='utf-8') as f:
        obj = csv.reader(f)
        for ligne in obj:
            if ligne[0] == d:
                doc = ligne[2]
    for elt in keys:
        if elt in k:
            continue
        k.append(elt)
    for elt in doc:
        j = k.index(elt) - 1
        x[j] += 1
    return x


def creation_ensemble(hachage, path):
    """crée l'ensemble de tout les vecteurs qui représente les documents de path

    Args:
        hachage (dict): l'index inversé
        path (str): document contenant tout les documents de l'ensemble

    Returns:
        list: ensemble des vecteurs des docs ou leur indice correspond a l'id du doc
    """
    ensemble = []
    lh = len(hachage)
    keys = hachage.keys()
    with open(path, 'r', encoding='utf-8') as f:
        obj = csv.reader(f)

        for ligne in obj:
            if ligne[0] == "":
                continue
            d = int(ligne[0])
            x_d = transformation(d, lh, keys, path)
            ensemble.append(x_d)
    return ensemble


def trouver_class_ppv(ppv, path):
    """trouve la classe pour un enseble de plus proche voisin donné

    Args:
        ppv (list): liste de couple (a, b) ou a est un vecteur et b le document correpsondant à ce dernier
        path (str): le document data qui relie les id des docs a leur class

    Returns:
        int: la classe pour ce vecteur
    """
    ensemble = []
    for elt in ppv:
        a, b = elt
        with open(path, 'r', encoding='utf-8') as f:
            obj = csv.reader(f)

            for ligne in obj:
                if ligne[0] == "":
                    continue
                elif int(ligne[0]) != b:
                    continue
                ensemble.append(int(ligne[1]))
    return max(ensemble, key=ensemble.count)


def pourcentage(classes, path, l):
    """renvoit a quel point on est précis avec notre algorithme
    pour les indices la classes en position i correspond au doc en position i

    Args:
        classes (list): liste des classes que l'on a estimer pour les documents dont on cherche la classe
        path (str): vers le document qui relie les doc id aux classes
        l (list): liste des id des docs pour lesquels on a deviner la classes

    Returns:
        float: precision comprise entre 0 et 1
    """
    list = []
    with open(path, 'r', encoding='utf-8') as f:
        obj = csv.reader(f)

        for ligne in obj:
            if ligne[0] in l:
                if ligne[1] == classes[l.index(ligne[0])]:
                    list.append(1)
                else:
                    list.append(0)
    return statistics.mean(list)


def obtenir_id(path):
    """renvoie les id d'un ensemble de document

    Args:
        path (str): lien vers le doc avec tout les docs

    Returns:
        lst: liste avec les id des docs qu'on regarde
    """
    ensemble = []
    with open(path, 'r', encoding='utf-8') as f:
        obj = csv.reader(f)

        for ligne in obj:
            if ligne[0] == "":
                continue
            d = int(ligne[0])
            ensemble.append(d)
    return ensemble


def return_stem(sentence):
    """ce qui sépare la phrase en petit mot

    Args:
        sentence (str): la phrase en question

    Returns:
        list: liste avec tout les mots coupés
    """
    doc = nlp(sentence)
    return [stemmer.stem(X.text) for X in doc]


def traitement(str):
    """renvoie une liste de mot représentant la phrase lématiser avec chaque mot séparé

    Args:
        str (str): phrase a lemmatiser

    Returns:
        list: la liste de mots sans conjugaisons, sans stop word etc....
    """
    clean_words = []
    for token in return_stem(str):
        if token not in stopWords:
            clean_words.append(token)
    i = 0
    while i < (len(clean_words)):
        if clean_words[i] == '.' or clean_words[i] == '...' or clean_words[i] == ':' or clean_words[i] == "!":
            del clean_words[i]
        else:
            i += 1
    return clean_words


def sans_html(str):
    """enlève les balises html pour un texte donné

    Args:
        str (str): un texte avec potentiellement des balises html

    Returns:
        str: le même texte sans les balises html
    """
    return re.sub(r'<[^>]*?>', '', str)


def euclidienne(a, b):
    """calcule la disatnce euclidienne entre deux vecteurs

    Args:
        a (list): vecteur a
        b (list): vecteur b

    Returns:
        float: la distance euclidienne entre a et b
    """
    return (abs(la.norm(a)-la.norm(b)))


def proche_voisin(metric, x, l, k):
    """prend en entrée un vecteur et retroune la liste des k plus proche voisins, on part du principe que
    le vecteur x est bien dans l'espace du vocabulaire car sinon on aurait un problème pour la représentation
    vectorielle, un mot par exemple qui n'est pas pris en compte dans le vocab

    Args:
        metric (fonction): qui prend deux vecteur et renvoi la metric
        x (list): le vecteur ou on veut les voisins
        l (list): liste de vecteurs dans l'espace
        k (int): nombre de plus proche voisin a renvoyer

    return :
        Liste des couples avec les plus proches voisins et leurs indices (correspond a quel doc)
    """
    if x not in l:
        raise "Problème de vocab qui peut exister"
    distance = {}
    ppv = []
    for i in range(len(l)):
        distance[metric(x, l[i])] = i
    distancetrie = sorted(distance.keys())
    for i in range(max(k + 1, len(distancetrie))):
        ppv.append((l[distance[distancetrie[i]]], distance[distancetrie[i]]))
    return ppv[1:]
