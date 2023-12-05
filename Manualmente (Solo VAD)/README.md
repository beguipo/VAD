## Manualmente (Solo VAD):

Se busca crear un VAD de manera manual que detecte cuando se este emitiendo voz y grabe esas secuencias (Lento)

### Tiempo real
Para el caso en el que siempres e este escuchando audio y se ejecute cierta funcion cuando se diga una palabra en especial.

#### VAD_1.py
En este script se busca hacer un VAD básico de manera que através del microfono por defecto del sistema podamos mostrar por la terminal un 1 si se detcta voz y un 0 si no se detecta voz.


#### VAD_2.py
Se observa que la sensibilidad es muy pequeña para hacer que se grabe solo cunado hay un 1, para ello haremos uso de un buffer (ventana deslizante).

buffer = collections.deque(maxlen=BUFFER_SIZE)

Con esta configuracion el buffer actua de manera que al llenarse se elimina el valor mas antiguo exixtente en este (como un head drop)


#### VAD_3.py
Es este script integramos la grabacion cunado la media del buffer sea mayor que un threshold, se puede observar que proceso es lento y tedioso por lo que voy a tratar de hacerlo de manera que se hagan pequeñas grabaciones de 5s perodicamente, se analizen con un VAD y si hay voz en dos seguidas se unan. A ver si de esta manera obtenemos unos resultados mas rápidos.


### Muestras de tiempo:
Para el caso en el que al presinar un boton se escuche audio durante una determinada longitud de tiempo

#### VAD_s_1.py
Scrip que graba cada 5s y lo almacena en la carptea de audios

#### VAD_s_2.py
Script extraido de github: https://github.com/wiseman/py-webrtcvad/blob/master/example.py
Se ejecuta pasandole el nivel de agressividad (1-3), siendo 3 el máximo y el path del archivo que quieres analizar. COn las pruebas que he hecho el 3 es el mejopr modo ya que coje exctamente donde hay voz. Otra cosa que hace es reducir la velocidad de la grabacion que nos devuelve de manera que nos escuchamos mas graves y lentos, aunque solo escuchamos la parte de voz, las demas partes las elimina.

Ya no se oye lento, era por una diferencia en la frecuencia de muestreo del microfono y en la de lectura.
