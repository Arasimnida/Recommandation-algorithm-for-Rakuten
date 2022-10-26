import csv
import statistics


def createur_dico(path):
    dict = {}
    with open(path, 'r', encoding='utf-8') as f:
        obj = csv.reader(f)
        for ligne in obj:
            if ligne[1] == 'prdtypecode':
                continue
            if ligne[1] in dict:
                dict[ligne[1]].append(ligne[0])
            else:
                dict[ligne[1]] = [ligne[0]]
    return dict


def f1_cat(cat, beta):
    pred = set(dict_pred[cat])
    test = set(dict_test[cat])
    n1 = len(test)
    n2 = len(pred)
    n3 = len(test & pred)
    r = n3/n1
    p = n3/n2
    return (1 + beta*beta) * p * r / (beta * beta * p + r)


ypred = "data\Y_prediction.csv"
ytest = "data\Y_test.csv"
f1_parcat = []
beta = 1
dict_pred = createur_dico(ypred)
dict_test = createur_dico(ytest)

for cat in dict_test.keys():
    f1_parcat.append(f1_cat(cat, beta))


print("la métrique f1_beta donne : " + str(statistics.mean(f1_parcat)))

k = 0
dict = {}
with open(ypred, 'r', encoding='utf-8') as f:
    obj = csv.reader(f)
    for ligne in obj:
        dict[ligne[0]] = ligne[1]

with open(ytest, 'r', encoding='utf-8') as d:
    obj = csv.reader(d)
    for ligne in obj:
        if dict[ligne[0]] == ligne[1]:
            k += 1


print("la métrique M donne : " + str(k / len(dict.keys())))
