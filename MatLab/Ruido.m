
% Leer el archivo de audio
[original_audio, fs] = audioread('/home/berri/Desktop/VAD/Muestras/Sin_Ruido/Velocidad.wav');

% Generar ruido
ruido = 0.1 * randn(size(original_audio)); % ajusta la amplitud del ruido según sea necesario

% Añadir ruido al archivo de audio original
audio_con_ruido = original_audio + ruido;

% Guardar el archivo con ruido
audiowrite('/home/berri/Desktop/VAD/Muestras/Con_Ruido/Velocidad.wav', audio_con_ruido, fs);

% Graficar ambas señales
tiempo_original = (0:length(original_audio)-1) / fs;
tiempo_ruido = (0:length(ruido)-1) / fs;
tiempo_con_ruido = (0:length(audio_con_ruido)-1) / fs;

figure;

subplot(3,1,1);
plot(tiempo_original, original_audio);
title('Archivo de Audio Original');
xlabel('Tiempo (s)');
ylabel('Amplitud');

subplot(3,1,2);
plot(tiempo_ruido, ruido);
title('Ruido Agregado');
xlabel('Tiempo (s)');
ylabel('Amplitud');

subplot(3,1,3);
plot(tiempo_con_ruido, audio_con_ruido);
title('Archivo de Audio con Ruido');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Guardar la figura
saveas(gcf, 'audio_con_ruido_plots.png');
