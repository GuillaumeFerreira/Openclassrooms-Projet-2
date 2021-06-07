import requests

#Fonction qui telecharge l'image d'un livre
def download_url_img(url_img, nom, rep):
    response = requests.get(url_img)
    # On isole le nom et l extention du fichier
    nom = nom.split("/")[4]

    file = open(rep + "/" + nom, "wb")
    file.write(response.content)
    file.close()
