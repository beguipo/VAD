import sounddevice as sd
import numpy as np
import datetime
import soundfile as sf



    
def grabar_audio():
    # Configurar la duración de la grabación en segundos
    duracion = 5

    # Grabar audio desde el micrófono
    audio = sd.rec(int(duracion * 44100), samplerate=44100, channels=1)

    # Esperar a que la grabación termine
    sd.wait()

    # Generar un nombre único para el archivo de grabación
    nombre_archivo = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S") +"(1)"+".wav"


    nombre_archivo = "Pequeñas Muestras/Audios/" + nombre_archivo
    # Guardar la grabación en un archivo WAV
    sf.write(nombre_archivo, audio, samplerate=32000)
    grabar_audio()



while True:
    grabar_audio()