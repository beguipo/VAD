import os
import time
from deepgram import Deepgram
from pydub import AudioSegment

def transcribir_archivos_mp3(directorio_entrada):
    # Obtener la lista de archivos en el directorio
    archivos_wav = [archivo for archivo in os.listdir(directorio_entrada) if archivo.endswith(".wav")]

    deepgram = Deepgram(DEEPGRAM_API_KEY)

    # Iterar sobre cada archivo .mp3
    for archivo_wav in archivos_wav:
        # Componer la ruta completa del archivo
        ruta_completa = os.path.join(directorio_entrada, archivo_wav)

        # Tomar muestra de tiempo
        

        # Transcribir el archivo con Whisper
        with open(ruta_completa, 'rb') as audio:
            source = {'buffer': audio, 'mimetype': 'audio/wav'}
            options = {'punctuate': True, 'language': 'es'}
            inicio_transcripcion = time.time()
            response = deepgram.transcription.sync_prerecorded(source, options)
            fin_transcripcion = time.time()
            transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
            #print(transcript)

        # Tomar muestra de tiempo
        

        # Calcular el tiempo que ha tardado en transcribirlo
        tiempo_transcripcion = fin_transcripcion - inicio_transcripcion

        # Mostrar el tiempo y la transcripción
        print(f"Archivo: {archivo_wav}")
        print(f"Tiempo de transcripción: {tiempo_transcripcion} segundos")
        print("Transcripción:")
        print(transcript)
        print("=" * 50)

if __name__ == "__main__":

    DEEPGRAM_API_KEY = '531290cdeab25255d63ec5f5cf04742ce092df5f'

    directorio_entrada_audio = "/home/berri/Desktop/VAD/Muestras/Sin_Ruido/"  # Reemplaza con la ruta de tu directorio
    transcribir_archivos_mp3(directorio_entrada_audio)
