## VAD + STT (Google Free API)
Uso de la api gratutita de google para detección y trasncripción de texto.

#### Transcripción_basica.py
Es un script sencillo que toma un archivo de texto .wav y nos muestra la trasncripcion por terminal

#### RT_1.ipynb (FUNCIONAL 100%)
Script de ronocimiento de voz de manera constante en timepo real que nos hace la trancripcion de manera automática. ACTUALMENTE EL QUE MEJOR FUNCIONA


### TR
Basandome en una primera grabacion de x segundos y luego llamar a la API

#### TR_1.py
Nos graba un fragmento de audio, lo trasncribe y ejecuta una funcion si se detecta cierta palabra en la transcripción. El objetivo es hacer tipo alexa de manera que si detecta cierta palabra (un nombre o algo) podemos ejecutar una funcion y sino descartar toda la trasncripción o almacenarla en un sition diferente.

#### TR_2.py (porcesos o hilos)
Basandonos en el programa anterior programamos un hilo o proceso para que grabe segmentos de audio de manera recurrente y otro porceso o hilo se encarga de in haciendo las trasncripciones de los fragmentos de audio. (Mejor funcionamiento en hilos)