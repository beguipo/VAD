import os
import time
import threading
import queue
import speech_recognition as sr

def grabar_audio(q):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        while True:
            print("Escuchando...")
            r.adjust_for_ambient_noise(source)
            audio = r.record(source, duration=5)  # Grabar durante 5 segundos
            q.put(audio)

def analizar_audio(q):
    r = sr.Recognizer()

    while True:
        audio = q.get()
        try:
            texto = r.recognize_google(audio, language="es-ES")
            print("Transcripción:", texto)
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

    # Configura la cola para compartir datos entre subprocesos
    cola = queue.Queue()

    # Crea los subprocesos
    hilo_grabacion = threading.Thread(target=grabar_audio, args=(cola,))
    hilo_analisis = threading.Thread(target=analizar_audio, args=(cola,))

    # Inicia los subprocesos
    hilo_grabacion.start()
    hilo_analisis.start()

    try:
        # Espera a que los subprocesos terminen
        hilo_grabacion.join()
        hilo_analisis.join()

    except KeyboardInterrupt:
        # Manejo de la interrupción de teclado (Ctrl+C)
        print("Programa interrumpido. Terminando subprocesos.")
        hilo_grabacion.join()
        hilo_analisis.join()
