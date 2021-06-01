# coding: utf8
from download_url import download_url_img
import csv
import os


def ecriture_csv(liste_livre, repertoire):

    # On créé le dossier 'images' pour la catégorie
    if not os.path.exists(repertoire + "/images"):
        os.makedirs(repertoire + "/images")

    with open(
        repertoire + "/bookstoscrape.csv", "w", newline="", encoding="utf-8-sig"
    ) as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=";")
        spamwriter.writerow(
            [
                "product_page_url",
                "universal_ product_code (upc)",
                "title",
                "price_including_tax",
                "price_excluding_tax",
                "number_available",
                "product_description",
                "category",
                "review_rating",
                "image_url",
            ]
        )
        for livre in liste_livre:
            spamwriter.writerow(
                [
                    livre.product_page_url,
                    livre.upc,
                    livre.title,
                    livre.price_including_tax,
                    livre.price_excluding_tax,
                    livre.number_available,
                    livre.product_description,
                    livre.category,
                    livre.review_rating,
                    livre.image_url,
                ]
            )

            # On profite de la boucle pour telecharger l image
            download_url_img(livre.image_url, livre.name_img, repertoire + "/images")
