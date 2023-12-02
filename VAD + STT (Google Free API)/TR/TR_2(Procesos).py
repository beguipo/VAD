import os
import time
import speech_recognition as sr
from multiprocessing import Process, Queue

def grabar_audio(queue):
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Escuchando...")
            r.adjust_for_ambient_noise(source)
            audio = r.record(source, duration=5)  # Grabar durante 5 segundos

            # Envía el audio al proceso de análisis
            queue.put(audio)

def analizar_audio(queue):
    r = sr.Recognizer()

    while True:
        # Obtiene el audio del proceso de grabación
        audio = queue.get()

        try:
            # Utiliza Google Web Speech API para la transcripción
            texto = r.recognize_google(audio, language="es-ES")
            print("Transcripción:", texto)

            # Almacena la transcripción en un archivo de texto
            with open("seq/transcripciones.txt", "a") as archivo:
                archivo.write(texto + "\n")

        except sr.UnknownValueError:
            print("No se pudo transcribir el audio")
        except sr.RequestError as e:
            print("Error en la solicitud al servicio de reconocimiento de voz:", str(e))

if __name__ == "__main__":
    # Crea la carpeta 'seq' si no existe
    if not os.path.exists("seq"):
        os.makedirs("seq")

    # Configura la cola para compartir datos entre procesos
    cola = Queue()

    # Crea los procesos
    proceso_grabacion = Process(target=grabar_audio, args=(cola,))
    proceso_analisis = Process(target=analizar_audio, args=(cola,))

    # Inicia los procesos
    proceso_grabacion.start()
    proceso_analisis.start()

    try:
        # Espera a que los procesos terminen (esto podría ser reemplazado por un manejo de señales más elegante)
        proceso_grabacion.join()
        proceso_analisis.join()

    except KeyboardInterrupt:
        # Manejo de la interrupción de teclado (Ctrl+C)
        print("Programa interrumpido. Terminando procesos.")
        proceso_grabacion.terminate()
        proceso_analisis.terminate()
        proceso_grabacion.join()
        proceso_analisis.join()
