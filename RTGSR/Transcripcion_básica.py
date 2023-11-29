import speech_recognition as sr

# Ruta del archivo de audio
audio_file = "chunk-01.wav"

# Crear un objeto de reconocimiento de voz
recognizer = sr.Recognizer()

# Abrir el archivo de audio
with sr.AudioFile(audio_file) as source:
    # Leer el audio del archivo
    audio = recognizer.record(source)

    try:
        # Realizar el reconocimiento de voz en español
        text = recognizer.recognize_google(audio, language="es-ES")
    except sr.UnknownValueError:
        text = "No se pudo reconocer el audio"

# Imprimir el texto reconocido
print(text)
