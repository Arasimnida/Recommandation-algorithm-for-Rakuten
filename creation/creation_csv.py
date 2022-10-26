import csv
import numpy as np

x_filtre_open = open('data/X_filtre.csv','r',encoding='utf-8')
y_filtre_open = open('data/Y_filtre.csv','r',encoding='utf-8')
x_eval_writer = open('data/X_eval.csv','w',newline='', encoding='utf-8')
x_eval_open = open('data/X_eval.csv','r', encoding='utf-8')
y_eval_writer = open('data/Y_eval.csv','w',newline='', encoding='utf-8')
x_filtre_final =open('data/X_filtre_final.csv','w',newline='',encoding='utf-8')
y_filtre_final =open('data/Y_filtre_final.csv','w',newline='',encoding='utf-8')
x_filtre_final_open = open('data/X_filtre_final.csv','r',encoding='utf-8')

def separation_csv(doc,fileto10,fileto90):
    """Permet de séparer un fichier csv en 10%/90% où les 10% vont dans le fichier fileto1O et le restant dans fileto90"""
    count = 0
    liste = []
    with doc as f, fileto90 as out:
        write = csv.writer(out)
        reader = csv.reader(f) 
        for obj in reader:
            if count <4600:
                """ 4600 représente 10% de X_filtre"""
                liste.append(obj)
                count += 1
            else:
                write.writerow(obj)
    with fileto10 as w:
        writer = csv.writer(w)
        for obj in liste:
            writer.writerow(obj)

            
separation_csv(x_filtre_open,x_eval_writer,x_filtre_final)


def lien_doc(doc_x,doc_y,doc_z):
    """Renvoie la liste des lignes de doc_x correspondant à l'ID dans doc_y"""
    liste =  []
    liste_2 =[]
    content_x = []
    content_y = []
    with doc_x as x:
        obj = csv.reader(x)
        for i in obj:
            liste.append(i[0])    
    with doc_y as y:
        obj_y = csv.reader(y)
        for i in obj_y:
            liste_2.append(i[0]) 
    with doc_z as z:
        obj_z = csv.reader(z)
        for i in obj_z:
            for j in liste:
                if i[0] == j:
                    content_x.append(i)
            for j in liste_2:
                if i[0] == j:
                    content_y.append(i)
    return content_x,content_y


x_evaluation,y_evalution = lien_doc(x_eval_open,x_filtre_final_open,y_filtre_open)



def importation_csv_X(file,content):
    """ Ecris dans file les informations contenues dans content"""
    with file:
        writer = csv.writer(file)
        for obj in content:
            writer.writerow(obj)

importation_csv_X(y_eval_writer,x_evaluation)
importation_csv_X(y_filtre_final,y_evalution)


            