% Nombre de los archivos .wav
archivo1 = 'Pequeñas Muestras/Audios/2023-11-24--19-29-07(1).wav';
archivo2 = 'chunk-01.wav';

% Leer los archivos .wav
[y1, fs1] = audioread(archivo1);
[y2, fs2] = audioread(archivo2);

% Crear un vector de tiempo para cada señal
t1 = (0:length(y1)-1) / fs1;
t2 = (0:length(y2)-1) / fs2;

% Crear una figura con dos subgráficos
figure;

% Subgráfico 1
subplot(2, 1, 1);
plot(t1, y1);
title('Señal de Audio 1');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Subgráfico 2
subplot(2, 1, 2);
plot(t2, y2);
title('Señal de Audio 2');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Ajustar el diseño de la figura
sgtitle('Dos Señales de Audio');

% Mostrar la figura
grid on;
