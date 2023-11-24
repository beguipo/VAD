# Deteccion exclusiva de voz, sin reduccion de ruido, hay que calibrarlo segun el micrófono

import sounddevice as sd
import numpy as np
from pydub import AudioSegment
import webrtcvad  

# Configuración de sounddevice
fs = 32000  # Frecuencia de muestreo (Depende algo ams de las caracteristicas del micrófono)
duration = 0.1  # Duración de cada grabación en segundos (a mas pequeño, mayor sensibilidad)


THRESHOLD = 1000  #Umbral a partir del que se considera que hay voz

# Inicializar el objeto VAD
vad = webrtcvad.Vad()

def is_voice(data):
 
    audio_segment = AudioSegment(
        data.tobytes(),
        frame_rate=fs,
        sample_width=data.dtype.itemsize,
        channels=1
    )
    volume = audio_segment.rms
    return volume > THRESHOLD

def main():
    # Establecer el modo de VAD en el nivel más agresivo
    vad.set_mode(1)

    print("Escuchando...")

    while True:
        # Grabar audio
        audio_data = sd.rec(int(fs * duration), samplerate=fs, channels=1, dtype=np.int16)
        sd.wait()

        # Verificar si hay voz
        if is_voice(audio_data):
            print("1", end="", flush=True)  # Escribir "1" sin salto de línea
        else:
            print("0", end="", flush=True)  # Escribir "0" sin salto de línea

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")

        