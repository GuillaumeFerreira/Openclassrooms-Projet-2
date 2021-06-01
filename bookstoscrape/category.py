# coding: utf8
import requests
from bs4 import BeautifulSoup
from constants import URL


def recup_categorie():
    # On récupère le code de la page web pour ensuite le traite avec beautifulsoup
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, "html5lib")

    dico_categorie = {}

    # On parcourt tous les liens de la page
    for element in soup.find_all("a"):
        # Il faut au moins trouver un occurence 'catalogue/category/books' pour la définir une catégorie
        if element["href"].count("catalogue/category/books/") == 1:
            # On enregistre dans un dictionnaire les variables nom et url de la catégorie
            dico_categorie[element.text.replace(" ", "")] = element["href"]

    return dico_categorie


def recup_lien_livre(lien, nb):
    liste_lien_livre = []
    for i in range(1, nb + 1):

        if i == 1:
            req = requests.get(URL + "/" + lien)

        else:
            req = requests.get(
                URL + "/" + lien[0 : len(lien) - 10] + "page-" + str(i) + ".html"
            )

        soup = BeautifulSoup(req.content, "html5lib")

        for element in soup.find_all("h3"):
            lien_livre = element.a["href"][8 : len(element.a["href"])]
            liste_lien_livre.append(URL + "catalogue" + lien_livre)

    return liste_lien_livre


def nb_page(lien):
    # On récupère le code de la page web pour ensuite le traite avec beautifulsoup
    req = requests.get(URL + "/" + lien)
    nb = 1
    # Si on trouve la class current dans le code source alors plusieurs pages sinon 1 page
    if str(req.content).count("current") == 1:
        soup = BeautifulSoup(req.content, "html5lib")

        # On recherche le texte de la class current pour recuperer la derniere lettre qui sera le nombre de page
        for i in soup.find_all(class_="current"):
            texte = i.text.replace(" ", "").replace("\n", "")
            nb = int(texte[len(texte) - 1])

    return nb
