# Deteccion exclusiva de voz, sin reduccion de ruido, hay que calibrarlo segun el micrófono

import sounddevice as sd
import numpy as np
from pydub import AudioSegment
import webrtcvad  

import collections #Para el buffer
import threading #Para el hilo de comprobacion del buffer
import time #Para dormir el hilo

import wave #Para guardar el audio
import datetime #Para el nombre del archivo

import os #Para manejar archivos y direcotrios

from deepgram import Deepgram #Para la API de Deepgram -> del github oficial de Deepgram
import json


# Directorios
directorio_entrada_audio = "seq/"
directorio_salida_audio = "seq/Final/"


#API DeepGram
DEEPGRAM_API_KEY = '531290cdeab25255d63ec5f5cf04742ce092df5f'




#Configuración del buffer 
BUFFER_SIZE = 5  # Número de resultados de detección de voz a tener en cuenta
VOICE_THRESHOLD =0.8   # Umbral de voz para comenzar a grabar

buffer = collections.deque(maxlen=BUFFER_SIZE)
buffer.extend([0]*BUFFER_SIZE)




# Configuración de sounddevice
fs = 32000  # Frecuencia de muestreo (Depende algo ams de las caracteristicas del micrófono)
duration = 0.1  # Duración de cada grabación en segundos (a mas pequeño, mayor sensibilidad)


THRESHOLD = 1000  #Umbral a partir del que se considera que hay voz

# Inicializar el objeto VAD
vad = webrtcvad.Vad()


global numero # Para la numeracion de los archivos
numero  = 0

def eliminar_archivos_wav(directorio):
    archivos = [archivo for archivo in os.listdir(directorio) if archivo.lower().endswith('.wav')]

    for archivo in archivos:
        os.remove(os.path.join(directorio, archivo))


def transcribir_DGM(idioma='es'):
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    archivo = directorio_salida_audio + "concatenado.wav"
    with open(archivo, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        options = {'punctuate': True, 'language': idioma}
        response = deepgram.transcription.sync_prerecorded(source, options)
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        print(transcript)
        #print(json.dumps(response, indent=4))

        #Eliminacion de los archivos de audio una vez usados
        eliminar_archivos_wav(directorio_entrada_audio)
        eliminar_archivos_wav(directorio_salida_audio)



def concatenar_archivos_en_directorio(directorio_salida, directorio_entrada):
    archivos = [archivo for archivo in os.listdir(directorio_entrada) if archivo.lower().endswith('.wav')]

    if not archivos:
        print("No hay archivos WAV en el directorio de entrada.")
        return

    archivos_ordenados = sorted(archivos, key=lambda x: int(x.split('output')[1].split('.')[0]))

    archivos_concatenados = AudioSegment.silent()

    for archivo in archivos_ordenados:
        ruta_completa = os.path.join(directorio_entrada, archivo)
        archivos_concatenados += AudioSegment.from_wav(ruta_completa)

    # Guardar el archivo concatenado con un nombre basado en el directorio de salida
    nombre_concatenado = os.path.join(directorio_salida, "concatenado.wav")
    archivos_concatenados.export(nombre_concatenado, format="wav")
    print(f"Archivos concatenados y guardados como: {nombre_concatenado}")




#Funcion para detectar voz
def is_voice(data):
 
    audio_segment = AudioSegment(
        data.tobytes(),
        frame_rate=fs,
        sample_width=data.dtype.itemsize,
        channels=1
    )
    volume = audio_segment.rms
    return volume > THRESHOLD


#Funcion main
def main():
    # Establecer el modo de VAD en el nivel más suave (comprobar)
    vad.set_mode(1)

    print("Escuchando...")

    global audio_data

    # Iniciar el hilo de comprobación del buffer
    threading.Thread(target=check_buffer, daemon=True).start()

    while True:
        # Grabar audio
        audio_data = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype=np.int16)
        sd.wait()

        # Verificar si hay voz
        if is_voice(audio_data):
            #print(1)
            buffer.append(1)
        else:
            #print(0)
            buffer.append(0)


#Hilo de comprobacion del buffer
def check_buffer():
    global numero

    while True:
        mean = sum(buffer) / len(buffer)
        if mean > VOICE_THRESHOLD:
            print("Grabando", end="", flush=True)  # Escribir "Grabando" sin salto de línea
            audio_data = sd.rec(int(fs * 2), samplerate=fs, channels=1, dtype=np.int16)
            sd.wait()

            # Guardar el audio en un archivo .wav
            
            nombre = directorio_entrada_audio + "output" + str(numero) + ".wav"
            numero = numero + 1

            with wave.open(nombre, 'w') as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(2)  # 2 bytes (16 bits) de ancho de muestra
                wav_file.setframerate(fs)
                wav_file.writeframes(audio_data.tobytes())
            print("Fin tramo", end="", flush=True)  # Escribir "Fin tramo" sin salto de línea
        else:
            time.sleep(0.2) #Esperar 0.4 segundos

            

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma de grabacion finalizado.")
        concatenar_archivos_en_directorio(directorio_salida_audio, directorio_entrada_audio)
        print("\nPrograma de concatenacion finalizado.")
        transcribir_DGM()