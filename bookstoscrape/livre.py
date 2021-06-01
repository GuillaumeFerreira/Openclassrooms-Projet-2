# coding: utf8
import requests
from bs4 import BeautifulSoup
from category import *
from constants import URL


class Livre:
    def __init__(self,lien,cat):

        req = requests.get(lien)

        soup = BeautifulSoup(req.content, 'html5lib')
        elements = soup.find_all('td')
        titres = soup.find_all('h1')
        description = soup.find_all('p')
        img = soup.find_all('img')
        rating = soup.find_all(class_="col-sm-6 product_main")

        self.product_page_url = lien
        self.upc = elements[0].text
        self.title = titres[0].text
        self.price_including_tax = elements[2].text[1:len(elements[2].text)]
        self.price_excluding_tax = elements[3].text[1:len(elements[3].text)]
        self.number_available = int(elements[5].text[10:len(elements[5].text)-11])
        self.product_description = description[3].text
        self.category = cat
        self.review_rating = 0
        if str(rating[0].find_all('p')[2])[22:26] == 'One"':
            self.review_rating = 1
        elif str(rating[0].find_all('p')[2])[22:26] == 'Two"':
            self.review_rating = 2
        elif str(rating[0].find_all('p')[2])[22:26] == 'thre':
            self.review_rating = 3
        elif str(rating[0].find_all('p')[2])[22:26] == 'Four':
            self.review_rating = 4
        elif str(rating[0].find_all('p')[2])[22:26] == 'Five':
            self.review_rating = 5
        self.image_url = URL + img[0]["src"][6:]
        self.name_img = img[0]["src"][6:len(img[0]["src"])]
def lister_livre():

    dico_cat={}
    for nom_cat, lien in recup_categorie().items():
        liste_livre = []



        for lien_l in recup_lien_livre(lien,nb_page(lien)):
            livre = Livre(lien_l, nom_cat.replace(" ", "").replace("\n", ""))
            liste_livre.append(livre)
        dico_cat[nom_cat]= liste_livre

    return  dico_cat