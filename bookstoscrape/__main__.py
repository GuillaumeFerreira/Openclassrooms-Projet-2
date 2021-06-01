# coding: utf8
from livre import lister_livre
from csv_write import ecriture_csv

import os



def run():
    dico_cat = lister_livre()

    for cat,liste_livre in dico_cat.items():
        cat="resultat/" + cat.replace(" ", "").replace("\n", "")
        if not os.path.exists(cat):
            os.makedirs(cat)

        ecriture_csv(liste_livre,cat)

if __name__ == "__main__":
    run()