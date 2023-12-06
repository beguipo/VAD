import os
import time
import whisper
from pydub import AudioSegment

def transcribir_archivos_mp3(directorio_entrada):
    # Obtener la lista de archivos en el directorio
    archivos_mp3 = [archivo for archivo in os.listdir(directorio_entrada) if archivo.endswith(".mp3")]

    # Iniciar el motor de Whisper
    modelo_whisper = whisper.load_model("small")

    # Iterar sobre cada archivo .mp3
    for archivo_mp3 in archivos_mp3:
        # Componer la ruta completa del archivo
        ruta_completa = os.path.join(directorio_entrada, archivo_mp3)

        # Tomar muestra de tiempo
        inicio_transcripcion = time.time()

        # Transcribir el archivo con Whisper
        transcripcion = modelo_whisper.transcribe(ruta_completa)

        # Tomar muestra de tiempo
        fin_transcripcion = time.time()

        # Calcular el tiempo que ha tardado en transcribirlo
        tiempo_transcripcion = fin_transcripcion - inicio_transcripcion

        # Mostrar el tiempo y la transcripción
        print(f"Archivo: {archivo_mp3}")
        print(f"Tiempo de transcripción: {tiempo_transcripcion} segundos")
        print("Transcripción:")
        print(transcripcion)
        print("=" * 50)

if __name__ == "__main__":
    directorio_entrada_audio = "/home/berri/Desktop/VAD/Muestras/Con_Ruido/"  # Reemplaza con la ruta de tu directorio
    transcribir_archivos_mp3(directorio_entrada_audio)
