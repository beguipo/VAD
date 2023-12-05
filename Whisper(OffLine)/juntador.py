import os
from pydub import AudioSegment



def concatenar_archivos_en_directorio(directorio_salida, directorio_entrada):
    archivos = [archivo for archivo in os.listdir(directorio_entrada) if archivo.lower().endswith('.wav')]

    if not archivos:
        print("No hay archivos WAV en el directorio de entrada.")
        return

    archivos_ordenados = sorted(archivos, key=lambda x: int(x.split('output')[1].split('.')[0]))

    archivos_concatenados = AudioSegment.silent()

    for archivo in archivos_ordenados:
        ruta_completa = os.path.join(directorio_entrada, archivo)
        archivos_concatenados += AudioSegment.from_wav(ruta_completa)

    # Guardar el archivo concatenado con un nombre basado en el directorio de salida
    nombre_concatenado = os.path.join(directorio_salida, "concatenado.wav")
    archivos_concatenados.export(nombre_concatenado, format="wav")
    print(f"Archivos concatenados y guardados como: {nombre_concatenado}")


# Especificar directorios de entrada y salida
directorio_entrada_audio = "seq/"
directorio_salida_audio = "seq/Final/"

# Llamar a la función para concatenar archivos en el directorio de entrada y guardar el resultado en el directorio de salida
concatenar_archivos_en_directorio(directorio_salida_audio, directorio_entrada_audio)
