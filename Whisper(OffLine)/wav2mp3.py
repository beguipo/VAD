from pydub import AudioSegment
import os

def convertir_wav_a_mp3(directorio_entrada, directorio_salida):
    # Obtener la lista de archivos .wav en el directorio de entrada
    archivos_wav = [archivo for archivo in os.listdir(directorio_entrada) if archivo.endswith(".wav")]

    # Crear el directorio de salida si no existe
    os.makedirs(directorio_salida, exist_ok=True)

    # Iterar sobre cada archivo .wav y convertirlo a .mp3
    for archivo_wav in archivos_wav:
        ruta_completa_wav = os.path.join(directorio_entrada, archivo_wav)

        # Cargar el archivo WAV
        audio = AudioSegment.from_wav(ruta_completa_wav)

        # Generar el nombre del archivo MP3 en el directorio de salida
        nombre_archivo_mp3 = os.path.splitext(archivo_wav)[0] + ".mp3"
        ruta_completa_mp3 = os.path.join(directorio_salida, nombre_archivo_mp3)

        # Exportar el archivo MP3
        audio.export(ruta_completa_mp3, format="mp3")
        print(f"Conversión completada: {nombre_archivo_mp3}")

if __name__ == "__main__":
    # Directorio de entrada (contiene archivos .wav)
    directorio_entrada_audio = "/home/berri/Desktop/VAD/Muestras/Con_Ruido"

    # Directorio de salida (donde se guardarán los archivos .mp3)
    directorio_salida_audio = "/home/berri/Desktop/VAD/Muestras/Con_Ruido"

    convertir_wav_a_mp3(directorio_entrada_audio, directorio_salida_audio)
