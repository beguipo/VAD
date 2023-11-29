# VAD
Creacion de un VAD para la incorporación en un asistente de voz para un vehículo autónomo.

## PROGRAMAS (En timepo real):

### VAD_1.py
En este script se busca hacer un VAD básico de manera que através del microfono por defecto del sistema podamos mostrar por la terminal un 1 si se detcta voz y un 0 si no se detecta voz.



### VAD_2.py
Se observa que la sensibilidad es muy pequeña para hacer que se grabe solo cunado hay un 1, para ello haremos uso de un buffer (ventana deslizante).

buffer = collections.deque(maxlen=BUFFER_SIZE)

Con esta configuracion el buffer actua de manera que al llenarse se elimina el valor mas antiguo exixtente en este (como un head drop)


### VAD_3.py
Es este script integramos la grabacion cunado la media del buffer sea mayor que un threshold, se puede observar que proceso es lento y tedioso por lo que voy a tratar de hacerlo de manera que se hagan pequeñas grabaciones de 5s perodicamente, se analizen con un VAD y si hay voz en dos seguidas se unan. A ver si de esta manera obtenemos unos resultados mas rápidos.


## PROGRAMAS (Grabaciones cortas):

### VAD_s_1.py
Scrip que graba cada 5s y lo almacena en la carptea de audios

### VAD_s_2.py
Script extraido de github: https://github.com/wiseman/py-webrtcvad/blob/master/example.py
Se ejecuta pasandole el nivel de agressividad (1-3), siendo 3 el máximo y el path del archivo que quieres analizar. COn las pruebas que he hecho el 3 es el mejopr modo ya que coje exctamente donde hay voz. Otra cosa que hace es reducir la velocidad de la grabacion que nos devuelve de manera que nos escuchamos mas graves y lentos, aunque solo escuchamos la parte de voz, las demas partes las elimina.

Ya no se oye lento, era por una diferencia en la frecuencia de muestreo del microfono y en la de lectura.

## RTGSR
Pruebas con Google Cloud Speech Recogniton, usando su api básica

### Transcripción_basica.py
Es un script sencillo que toma un archivo de texto .wav y nos muestra la trasncripcion por terminal

### TR_1.py
Nos graba un fragmento de audio, lo trasncribe y ejecuta una funcion si se detecta cierta palabra en la transcripción. El objetivo es hacer tipo alexa de manera que si detecta cierta palabra (un nombre o algo) podemos ejecutar una funcion y sino descartar toda la trasncripción o almacenarla en un sition diferente.

### TR_2.py (porcesos o hilos)
Basandonos en el programa anterior programamos un hilo o proceso para que grabe segmentos de audio de manera recurrente y otro porceso o hilo se encarga de in haciendo las trasncripciones de los fragmentos de audio. (Mejor funcionamiento en hilos)

** POSIBLE MEJORA: 2 hilos de escucha sincronizados para que cuando uno acabe le otro empiece asi conseguimos solventar esas peridas de milisegundos entre grabaciones. **
