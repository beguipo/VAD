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
            
            nombre = "seq/output" + str(numero) + ".wav"
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
        print("\nPrograma finalizado.")