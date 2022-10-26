import csv


def classe_cat(path):
    """
    prend un fichier csv en entrée de data de sortie et retourne pour chaque catégorie les elements dedans
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
                res[b].append(a)
            else:
                res[b] = [a]
    return(res)
