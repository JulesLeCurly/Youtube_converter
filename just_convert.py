from moviepy.editor import AudioFileClip
from tqdm import tqdm
import os
import time 
# Convertir les fichiers audio en format MP3
for audio_file in tqdm(os.listdir("mp3"), desc="Conversion en cours", unit="fichier"):
    if audio_file.endswith(".mp4"):
        audio_path = os.path.join("mp3", audio_file)
        mp3_path = os.path.join("mp3", audio_file.replace(".mp4", ".mp3"))
        audio = AudioFileClip(audio_path)
        audio.write_audiofile(mp3_path)
        audio.close()  # Fermez explicitement le fichier audio pour le libérer
        time.sleep(0.2)
        os.remove(audio_path)
        #print(f"{mp3_path} converti")