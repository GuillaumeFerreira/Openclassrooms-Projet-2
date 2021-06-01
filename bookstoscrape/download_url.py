# coding: utf8
import requests


def download_url_img(url_img, nom, rep):
    response = requests.get(url_img)
    # On isole le nom et l extention du fichier
    nom = nom.split("/")
    nom = nom[4]

    file = open(rep + "/" + nom, "wb")
    file.write(response.content)
    file.close()
