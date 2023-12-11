# Voice activity detection (VAD)
import speech_recognition as sr

# Monitorizacion del directorio sin polling
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Directorios
import os

# Importamos el motor de Vosk
import vosk

# Hilos
import threading

# Tratamiento de .wav
import wave



#--------------------------------------------- Funciones --------------------------------------------------#

def eliminar_archivos_wav(directorio):
    archivos = [archivo for archivo in os.listdir(directorio) if archivo.lower().endswith('.wav')]

    for archivo in archivos:
        os.remove(os.path.join(directorio, archivo))


def main(semaphore):

    while True:
        semaphore.wait()
        with sr.Microphone() as source:
            print("Di algo...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            # Guardar el audio en un archivo .wav
            with wave.open(directorio_entrada_audio + "audio.wav", "wb") as file:
                file.setnchannels(1)
                file.setsampwidth(2)
                file.setframerate(44100)
                file.writeframes(audio.get_raw_data())
        semaphore.clear()
            

class MyHandler(FileSystemEventHandler):
    def __init__(self, file_created_event):
        self.file_created_event = file_created_event

    def on_created(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created':
            print(f"¡Se ha creado el archivo: {event.src_path}!")
            self.file_created_event.set()

def monitor_directory(directory_path, file_created_event):
    event_handler = MyHandler(file_created_event)
    observer = Observer()
    observer.schedule(event_handler, path=directory_path, recursive=False)
    observer.start()

    try:
        print(f"Monitoreando el directorio: {directory_path}")
        observer.join()
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


def Whisper_ngin(semaphore,rec_semaphore):

    modelo = vosk.Model("Vosk/vosk-model-es-0.42")
    reconocedor = vosk.KaldiRecognizer(modelo, 44100)
    #print("Modelo cargado")
    rec_semaphore.set()

    while True: 
        #print("while true whisper")
        semaphore.wait()

        #print('Entra a traducir')
        with open(directorio_salida_audio + "audio.wav", 'rb') as audio_file:
            audio_data = audio_file.read()

        #inicio_transcripcion = time.time()
        reconocedor.AcceptWaveform(audio_data)
        resultado = reconocedor.FinalResult()
        #fin_transcripcion = time.time()


        eliminar_archivos_wav(directorio_salida_audio)
        
        #print(trasncripcion)
        with open("transcripcion.txt", "a") as file:
            file.write(resultado + "\n")

        semaphore.clear()
        rec_semaphore.set()


if __name__ == "__main__":



    directorio_entrada_audio = "FINAL/tmp/"
    directorio_salida_audio = "FINAL/tmp/"
    recognizer = sr.Recognizer()

    # Semaforo generacion de archivos
    file_created_event = threading.Event()
    semaphore2 = threading.Event()

    # Crear e iniciar el hilo que verifica archivos
    verificador_thread = threading.Thread(target=monitor_directory,args=(directorio_salida_audio, file_created_event))
    verificador_thread.start()

    whisperThread = threading.Thread(target=Whisper_ngin, args=(file_created_event,semaphore2))
    whisperThread.start()

    main(semaphore2)
