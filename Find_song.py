from youtubesearchpython import VideosSearch
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os


def search_youtube(query):
    videosSearch = VideosSearch(query, limit = 1)
    result = videosSearch.result()
    if result['result']:
        video = result['result'][0]
        title = video['title']
        link = video['link']
        return title, link
    else:
        return None, None

query = "votre titre de musique ici"
title, link = search_youtube(query)

if title and link:
    print(f"Title: {title}")
    print(f"Link: {link}")
else:
    print("Aucune vidéo trouvée.")


while True:
    query = input("Entrez votre titre de musique à télécharger : ")
    title, link = search_youtube(query)

    if title and link:
        print(f"Title: {title}")
        print(f"Link: {link}")
        video_url = link
        # Créer un objet YouTube
        yt = YouTube(video_url)

        # Filtrer les flux pour n'inclure que l'audio
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Télécharger l'audio
        audio_file = audio_stream.download(output_path="mp3")
        print(f"{audio_file} téléchargé")

        # Convertir le fichier audio en format MP3
        if audio_file.endswith(".mp4"):
            audio_path = os.path.join("mp3", audio_file)
            mp3_path = os.path.join("mp3", audio_file.replace(".mp4", ".mp3"))
            audio = AudioFileClip(audio_path)
            audio.write_audiofile(mp3_path)
            audio.close()  # Fermez explicitement le fichier audio pour le libérer
            os.remove(audio_path)
            print(f"{mp3_path} converti")
    else:
        print("Aucune vidéo trouvée.")
    