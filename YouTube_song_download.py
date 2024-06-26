from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

while True:
    # Demander à l'utilisateur de fournir le lien de la vidéo YouTube
    video_url = input("Entrez le lien de la vidéo YouTube à télécharger : ")

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