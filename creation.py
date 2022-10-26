import csv


def createurcsv(id, cat)
  data = [('productid', 'prdtypecode')]
   for i in range(0, len(id)):
        data.append((id[i], cat[i]))

    fichier = open('Y_prediction.csv', 'w', newline="")
    obj = csv.writer(fichier)
    for element in data:
        obj.writerow(element)
    fichier.close()
