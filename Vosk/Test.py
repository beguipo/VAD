import os
import time
import vosk
import csv

def transcribir_archivos_mp3(directorio_entrada):
    # Obtener la lista de archivos en el directorio
    archivos_wav = [archivo for archivo in os.listdir(directorio_entrada) if archivo.endswith(".wav")]

    # Iniciar el motor de Vosk
    modelo = vosk.Model("Vosk/vosk-model-es-0.42")
    reconocedor = vosk.KaldiRecognizer(modelo, 32000)

    # Lista para almacenar los resultados de transcripción
    resultados_transcripcion = []

    # Iterar sobre cada archivo .wav
    for archivo_wav in archivos_wav:
        # Componer la ruta completa del archivo
        ruta_completa = os.path.join(directorio_entrada, archivo_wav)

        # Leer el archivo de audio y convertirlo a bytes
        with open(ruta_completa, 'rb') as audio_file:
            audio_data = audio_file.read()

        # Procesar el audio
        inicio_transcripcion = time.time()
        reconocedor.AcceptWaveform(audio_data)
        resultado = reconocedor.FinalResult()
        fin_transcripcion = time.time()

        # Obtener la transcripción
        transcripcion = transcripcion.get("text", "") if isinstance(resultado, dict) else str(resultado)

        # Calcular el tiempo que ha tardado en transcribirlo
        tiempo_transcripcion = fin_transcripcion - inicio_transcripcion

        # Agregar resultados a la lista
        resultados_transcripcion.append({
            "nombre_archivo": archivo_wav,
            "tiempo_transcripcion": tiempo_transcripcion,
            "transcripcion": transcripcion
        })

        # Mostrar el tiempo y la transcripción en la consola
        print(f"Archivo: {archivo_wav}")
        print(f"Tiempo de transcripción: {tiempo_transcripcion} segundos")
        print("Transcripción:")
        print(transcripcion)
        print("=" * 50)

    return resultados_transcripcion

def guardar_resultados_csv(resultados, nombre_archivo_csv):
    # Encabezados del archivo CSV
    encabezados = ["Nombre del Archivo", "Tiempo de Transcripción", "Transcripción"]

    with open(nombre_archivo_csv, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        
        # Escribir encabezados
        escritor_csv.writerow(encabezados)

        # Escribir resultados
        for resultado in resultados:
            nombre_archivo = resultado["nombre_archivo"]
            tiempo_transcripcion = resultado["tiempo_transcripcion"]
            transcripcion = resultado["transcripcion"]

            escritor_csv.writerow([nombre_archivo, tiempo_transcripcion, transcripcion])

if __name__ == "__main__":
    directorio_entrada_audio = "/home/berri/Desktop/VAD/Muestras/Sin_Ruido/"  # Reemplaza con la ruta de tu directorio

    resultados_transcripcion = transcribir_archivos_mp3(directorio_entrada_audio)

    # Ruta donde se guardará el archivo CSV
    nombre_archivo_csv = "/home/berri/Desktop/VAD/Vosk/resultados.csv"

    # Guardar resultados en el archivo CSV
    guardar_resultados_csv(resultados_transcripcion, nombre_archivo_csv)
