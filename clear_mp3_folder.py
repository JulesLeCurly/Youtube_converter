import os
import glob

def supprimer_fichiers_mp3():
    """
    Supprime tous les fichiers dans le sous-dossier /mp3 du dossier courant.
    """
    chemin_mp3 = os.path.join(os.getcwd(), 'mp3')
    fichiers_mp3 = glob.glob(os.path.join(chemin_mp3, '*'))

    for fichier in fichiers_mp3:
        try:
            if os.path.isfile(fichier):
                os.remove(fichier)
                print(f'Supprimé: {fichier}')
        except Exception as e:
            print(f'Erreur lors de la suppression de {fichier}: {e}')

# Utilisation de la fonction
supprimer_fichiers_mp3()
