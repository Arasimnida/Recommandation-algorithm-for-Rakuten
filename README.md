Ce projet n'a pas pu être poussé aussi loin que souhaité. Nous avons manqué de temps pour améliorer l'éfficacité et effectuer des tests croisés.

## Nom
E-Commerce : classification multimodale des types de produits à grande échelle.

## Description
Ce projet vise à associer à chaque objet (description, image) une catégorie à l'aide de données mises à notre disposition : ensemble d'associations objet-catégorie. Puis, par analyse de similarités, nous tâcherons alors d'attribuer à chaque objet la catégorie qui correspond le mieux.

## Installation
Pour pouvoir parcourir les différents fichiers correctement, il faut installer certaines bibliothèques. Pour vous faciliter la tâche, vous pouvez directement écrire la commande suivante : "$ pip install -r requierements.txt" dans votre terminal. 
Sinon, vous pouvez les installer un par un avec la commande : "pip install" suivie du nom de votre module.

## Usage
Il faut télécharger les images qui sont disponible à l'adresse suivante : https://challengedata.ens.fr/participants/challenges/35/
Ensuite il faut lancer le fichier classification_image.py pour classfier les images.
Il faut lancer le fichier main.py avec la commande : "python main.py" dans le terminal. Celui-ci réalise le calcul des classes. Attention : il faut renseigner la variable path_y (voir commentaire correspondant).
Il faut aussi lancer le fichier calcul_efficacite.py : il donne l'efficacité de notre modèle. 
Dans le module création, on retrouve les fichiers qui permettent de créer différentes choses utiles.
Dans le dossier data, on retrouve toutes les données : celles fournies, les données filtrées (équilibrage) et les données test.
Dans le module traitement se trouve les deux fichiers qui permettent de traiter image et texte respectivment.
Enfin, le module travail regroupe différentes fonctions qui permettent de réaliser diverses choses dont nous avons besoin.
Le fichier "Output.py" présente l'index inversé.
Le fichier "requierements.txt" permet au nouvel utilisateur de télécharger toutes les bibliothèques nécessaires à l'éxecution des programmes de ce projet.
Finallement, ce README vise à renseigner le visiteur/utilisateur sur le porjet qu'il s'apprête à découvrir.

## Support
En cas de problème, vos êtes invités à contacter :
- vincent.nguyen@student-cs.fr
- samuel.cordon@student-cs.fr
- eliot.atlani@student-cs.fr
- blaise.depauw@student-cs.fr
- arthur.carsana@student-cs.fr

## Roadmap
Ce projet est encore bien loin de toucher à sa fin et il reste enormément de choses possibles à faire pour le compléter.
Par exemple :
- traitement d'autres objets différents (support vidéo par exemple)
- amélioration de l'éfficacité avec des modèles différents des deux utilisés dans ce projet (plus proches voisins et régression logistique)
- effectuer des tests croisés pour l'entraînement du modèle. 

## Contributing
Nous sommes ouverts à toute contribution extérieure.