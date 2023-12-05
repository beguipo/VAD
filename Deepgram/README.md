## Deepgram
Pruebas usando la API de deepgram (Deep Learn aplicado a la transccripcion de audio)

#### Deepgram.py
Script completo, incorpora un VAD que graba segmentos de 2s como los que se pueden ver en la carpeta 'Manualmente (Solo VAD)', funciones que concatenan las segmentos de audio si entran en una determinada ventana de tiempo, pasan el audio a la API de DeepGram con las pociones especificas para que detecte el idioma español y final mente nos devuelve la trasncripción y limpia los archivos de audio generados.

#### Fixed_VAD.py
VAD usado en el script DeepGram.py

#### juntador.py
Concatena archivos de audio de forma ordenada

#### Transcription.py 
Uso de la API de DeepGram