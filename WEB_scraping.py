import requests
from bs4 import BeautifulSoup
import re

def trouver_lien_video(url):
    # Faire la requête GET pour récupérer le contenu HTML de la page
    response = requests.get(url)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Utiliser BeautifulSoup pour analyser le HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Trouver les balises <video> et extraire le lien de la source vidéo
        videos = soup.find_all('video')
        if videos:
            for video in videos:
                src = video.get('src')
                if src:
                    return src
        
        # Si aucune balise <video> n'est trouvée, chercher directement les liens vidéo
        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']
            if re.match(r'^.*\.(mp4|avi|mkv|mov)$', href):
                return href

        # Si aucun lien vidéo n'est trouvé
        return None
    else:
        # Afficher un message d'erreur si la requête échoue
        print("La requête a échoué avec le code :", response.status_code)
        return None

def telecharger_video(url_video, nom_fichier):
    # Faire une requête GET pour récupérer le contenu de la vidéo
    response = requests.get(url_video, stream=True)
    
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Ouvrir un fichier en mode binaire pour écrire le contenu de la vidéo
        with open(nom_fichier, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print("La vidéo a été téléchargée avec succès sous le nom :", nom_fichier)
    else:
        # Afficher un message d'erreur si la requête échoue
        print("La requête a échoué avec le code :", response.status_code)

# Lien du site web
lien_site = input("Entrez le lien du site web : ")

# Trouver le lien de la vidéo
lien_video = trouver_lien_video(lien_site)

if lien_video:
    # Télécharger la vidéo
    nom_fichier = input("Entrez le nom du fichier de sortie : ")
    telecharger_video(lien_video, nom_fichier)
else:
    print("Aucune vidéo n'a été trouvée sur cette page.")
