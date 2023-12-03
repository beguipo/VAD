from deepgram import Deepgram #Para la API de Deepgram -> del github oficial de Deepgram
import json


# Directorios
directorio_entrada_audio = "seq/"
directorio_salida_audio = "seq/Final/"


#API DeepGram
DEEPGRAM_API_KEY = '531290cdeab25255d63ec5f5cf04742ce092df5f'





def transcribir_DGM(idioma='es'):
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    archivo = directorio_salida_audio + "concatenado.wav"
    with open(archivo, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        options = {'punctuate': True, 'language': idioma}
        response = deepgram.transcription.sync_prerecorded(source, options)
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        print(transcript)
        #print(json.dumps(response, indent=4))


if __name__ == "__main__":
    transcribir_DGM()