import sys

try:
    from pytube import YouTube
    from pytube import Playlist
    from moviepy.editor import AudioFileClip
    from youtubesearchpython import VideosSearch
    import os
    from tqdm import tqdm
    import time
    import shutil
except:
    print("Please install the neded librairy with 'module_needed.bat' ")
    sys.exit()


class YoutubeConverter():
    def __init__(self):
        pass
    
    def Just_convert(self, time_wait = 0.2, path="", playlist = None):
        if path == "":
            # Chemin vers le dossier de l'utilisateur
            user_home = os.path.expanduser('~')
            
            # Chemin vers le dossier de téléchargements
            final_path_folder = os.path.join(user_home, 'Downloads')
        else:
            final_path_folder = path
        
        if playlist != None:
            final_path_folder = os.path.join(final_path_folder, playlist)
        
        # Convertir les fichiers audio en format MP3
        for audio_file in tqdm(os.listdir("temporary"), desc="Conversion en cours", unit="fichier"):
            if audio_file.endswith(".mp4"):
                audio_path = os.path.join("temporary", audio_file)
                mp3_path = os.path.join("temporary", audio_file.replace(".mp4", ".mp3"))
                audio = AudioFileClip(audio_path)
                audio.write_audiofile(mp3_path)
                audio.close()  # Fermez explicitement le fichier audio pour le libérer
                time.sleep(time_wait)
                os.remove(audio_path)
                self.deplacer_fichier_vers_dossier(mp3_path, final_path_folder)
                print(f"{mp3_path} converti")
    
    def Find_Song(self, query):
        videosSearch = VideosSearch(query, limit = 1)
        result = videosSearch.result()
        if result['result']:
            video = result['result'][0]
            title = video['title']
            link = video['link']
            return title, link
        else:
            return None, None
    
    def Song_Download(self, url = "", name = "", path = ""):
        if url == "":
            title, link = self.Find_Song(name)
            if title and link:
                print(f"Title: {title}")
                print(f"Link: {link}")
                video_url = link
        else:
            video_url = url

        # Créer un objet YouTube
        yt = YouTube(video_url)
    
        # Filtrer les flux pour n'inclure que l'audio
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        os.makedirs("/temporary", exist_ok=True)
        # Télécharger l'audio
        audio_file = audio_stream.download(output_path="temporary")
        print(f"{audio_file} téléchargé")
        
        self.Just_convert(path=path)
            
    
    def Playlist_Download(self, url, path = ""):
        # Créer un objet Playlist
        playlist = Playlist(url)
        
        # Télécharger l'audio de chaque vidéo dans la playlist
        for video in tqdm(playlist.videos, desc="Téléchargement en cours", unit="vidéo"):
            audio_stream = video.streams.filter(only_audio=True).first()
            audio_file = audio_stream.download(output_path="temporary")
            print(f"{audio_file} téléchargé")
        
        nom_playlist = playlist.title
        self.Just_convert(path=path, playlist = nom_playlist)
    
    def deplacer_fichier_vers_dossier(self, source, dossier_destination):
        try:
            # Vérifier si le fichier source existe
            if not os.path.isfile(source):
                print(f"Le fichier source {source} n'existe pas.")
                return
    
            # Vérifier si le dossier de destination existe, sinon le créer
            if not os.path.exists(dossier_destination):
                os.makedirs(dossier_destination, exist_ok=True)
                print(f"Le dossier de destination {dossier_destination} a été créé.")
    
            # Obtenir le nom de fichier à partir du chemin source
            nom_fichier = os.path.basename(source)
    
            # Construire le chemin complet du fichier de destination
            destination_complet = os.path.join(dossier_destination, nom_fichier)
    
            # Déplacer le fichier
            shutil.move(source, destination_complet)
            print(f"Fichier déplacé de {source} à {destination_complet}")
        
        except Exception as e:
            print(f"Erreur lors du déplacement du fichier: {e}")