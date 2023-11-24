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