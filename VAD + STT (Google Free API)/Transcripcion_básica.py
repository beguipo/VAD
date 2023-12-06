import speech_recognition as sr
import os
import time

# Ruta del archivo de audio
directorio_entrada = "/home/berri/Desktop/VAD/Muestras/Con_Ruido/"  # Reemplaza con la ruta de tu directorio


# Crear un objeto de reconocimiento de voz
recognizer = sr.Recognizer()

# Abrir el archivo de audio

archivos_wav = [archivo for archivo in os.listdir(directorio_entrada) if archivo.endswith(".wav")]

for archivo_wav in archivos_wav:

    ruta_completa = os.path.join(directorio_entrada, archivo_wav)


    with sr.AudioFile(ruta_completa) as source:
    # Leer el audio del archivo
    
        audio = recognizer.record(source)        
        try:
            # Realizar el reconocimiento de voz en español
            text = recognizer.recognize_google(audio, language="es-ES")
        except sr.UnknownValueError:
            text = "No se pudo reconocer el audio"

    
    # Componer la ruta completa del archivo

    # Tomar muestra de tiempo
    inicio_transcripcion = time.time()
    try:
        # Realizar el reconocimiento de voz en español
        text = recognizer.recognize_google(audio, language="es-ES")
    except sr.UnknownValueError:
        text = "No se pudo reconocer el audio"

    # Tomar muestra de tiempo
    fin_transcripcion = time.time()
    # Calcular el tiempo que ha tardado en transcribirlo
    tiempo_transcripcion = fin_transcripcion - inicio_transcripcion
    # Mostrar el tiempo y la transcripción
    print(f"Archivo: {archivo_wav}")
    print(f"Tiempo de transcripción: {tiempo_transcripcion} segundos")
    print("Transcripción:")
    print(text)
    print("=" * 50)