import os
import vosk

def transcribir_wav(ruta_modelo, ruta_audio):
    # Inicializar el modelo Vosk
    modelo = vosk.Model(ruta_modelo)

    # Crear un reconocedor de voz
    reconocedor = vosk.KaldiRecognizer(modelo, 32000) #Poner bien el sample rate

    # Leer el archivo de audio y convertirlo a bytes
    with open(ruta_audio, 'rb') as audio_file:
        audio_data = audio_file.read()

    # Procesar el audio
    reconocedor.AcceptWaveform(audio_data)
    resultado = reconocedor.FinalResult()

    # Obtener la transcripción
    transcripcion = resultado
    return transcripcion

def transcribir_carpeta(ruta_modelo, carpeta_audio):
    # Obtener la lista de archivos .wav en la carpeta
    archivos_wav = [f for f in os.listdir(carpeta_audio) if f.endswith(".wav")]

    # Transcribir cada archivo
    for archivo in archivos_wav:
        ruta_audio = os.path.join(carpeta_audio, archivo)
        transcripcion = transcribir_wav(ruta_modelo, ruta_audio)

        # Imprimir la transcripción o guardarla en un archivo, según sea necesario
        print(f'Transcripción de {archivo}: {transcripcion}')

if __name__ == "__main__":
    # Ruta al modelo de Vosk
    ruta_modelo = "/home/berri/Desktop/VAD/Vosk/vosk-model-es-0.42"

    # Ruta a la carpeta que contiene los archivos .wav
    carpeta_audio = "Muestras/Sin_Ruido"

    # Transcribir los archivos en la carpeta
    transcribir_carpeta(ruta_modelo, carpeta_audio)
