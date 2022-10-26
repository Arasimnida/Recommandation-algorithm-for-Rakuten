This project could not be taken as far as desired. There was not enough time to improve efficiency and to carry out cross-testing.

## Name
E-Commerce: multimodal classification of product types on a large scale.

## Description
This project aims to associate each object (description, image) with a category using data made available to us: a set of object-category associations. Then, by similarity analysis, we will try to assign to each object the category that best corresponds.

## Installation
To be able to browse the different files correctly, you need to install some libraries. To make it easier for you, you can directly write the following command: "$ pip install -r requierements.txt" in your terminal. 
Otherwise, you can install them one by one with the command: "pip install" followed by the name of your module.
Some files are compressed, so make sure you unpack them all.

## Use
You need to download the images which are available at the following address: https://challengedata.ens.fr/participants/challenges/35/
Then you have to launch the file classification_image.py to classify the images.
You have to launch the file main.py with the command: "python main.py" in the terminal. This file calculates the classes. Attention: you must fill in the path_y variable (see corresponding comment).
You must also launch the file calcul_efficacite.py : it gives the efficiency of our model. 
In the creation module, you will find the files that allow you to create various useful things.
In the data folder, we find all the data: the supplied data, the filtered data (balancing) and the test data.
In the processing module, you will find the two files that allow you to process images and text respectively.
Finally, the work module groups together various functions that allow us to do various things we need.
The file "Output.py" presents the inverted index.
The file "requierements.txt" allows the new user to download all the libraries necessary to run the programs of this project.
Finally, this README aims at informing the visitor/user about the project he is about to discover.

## Support
In case of problems, you are invited to contact
- samuel.cordon@student-cs.fr
- eliot.atlani@student-cs.fr
- blaise.depauw@student-cs.fr
- arthur.carsana@student-cs.fr
- vincent.nguyen@student-cs.fr

## Roadmap
This project is still far from being finished and there is still a lot to do to complete it.
For example :
- processing of other different objects (e.g. video support)
- improving the efficiency with different models than the two used in this project (nearest neighbours and logistic regression)
- cross-testing the model for training. 

## Contributing
We are open to any external contribution.
