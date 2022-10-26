import csv
import os
import os.path


def trouver_cat_product(product_id, path, path2):
    """
    path = x train genre
    path 2 avec les cat

    product_id = id du product

    """
    id = 0
    cat = -1
    with open(path, 'r', encoding='utf-8') as f:
        obj = csv.reader(f)
        for i in obj:
            if i[3] == str(product_id):
                id = i[0]
                with open(path2, 'r', encoding='utf-8') as f:
                    obj = csv.reader(f)
                    for j in obj:
                        if j[0] == id:
                            cat = j[1]
    return cat


files = os.listdir('images/image_train')
for f in files:
    s = f.split("_")[3]
    s = s[:len(s)-4]
    print(int(s), trouver_cat_product(
        int(s), 'data/X_train_update.csv', 'data/Y_train_CVw08PX.csv'))
