from pytube import Playlist
from moviepy.editor import AudioFileClip
from tqdm import tqdm
import os

# Demander à l'utilisateur de fournir le lien de la playlist YouTube
playlist_url = input("Entrez le lien de la Playlist YouTube à télécharger : ")

# Créer un objet Playlist
playlist = Playlist(playlist_url)

# Télécharger l'audio de chaque vidéo dans la playlist
for video in tqdm(playlist.videos, desc="Téléchargement en cours", unit="vidéo"):
    audio_stream = video.streams.filter(only_audio=True).first()
    audio_file = audio_stream.download(output_path="mp3")
    #print(f"{audio_file} téléchargé")

# Convertir les fichiers audio en format MP3
for audio_file in tqdm(os.listdir("mp3"), desc="Conversion en cours", unit="fichier"):
    if audio_file.endswith(".mp4"):
        audio_path = os.path.join("mp3", audio_file)
        mp3_path = os.path.join("mp3", audio_file.replace(".mp4", ".mp3"))
        audio = AudioFileClip(audio_path)
        audio.write_audiofile(mp3_path)
        os.remove(audio_path)
        #print(f"{mp3_path} converti")
