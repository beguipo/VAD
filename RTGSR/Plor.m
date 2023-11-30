% Leer los archivos de audio
[recording, fs_recording] = audioread('recording.wav');
[jackhammer, fs_jackhammer] = audioread('jackhammer.wav');

% Asegurarse de que ambas señales tengan la misma frecuencia de muestreo
if fs_recording ~= fs_jackhammer
    error('Las frecuencias de muestreo de los archivos no coinciden.');
end

% Añadir el ruido al archivo de grabación
noisy_file = recording + jackhammer;

% Guardar el archivo resultante
audiowrite('noisy_file.wav', noisy_file, fs_recording);

% Graficar las señales originales y la resultante
time_recording = (0:length(recording)-1) / fs_recording;
time_jackhammer = (0:length(jackhammer)-1) / fs_jackhammer;
time_noisy = (0:length(noisy_file)-1) / fs_recording;

figure;

subplot(3,1,1);
plot(time_recording, recording);
title('Grabación Original');
xlabel('Tiempo (s)');
ylabel('Amplitud');

subplot(3,1,2);
plot(time_jackhammer, jackhammer);
title('Ruido (jackhammer)');
xlabel('Tiempo (s)');
ylabel('Amplitud');

subplot(3,1,3);
plot(time_noisy, noisy_file);
title('Grabación con Ruido');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Guardar la figura
saveas(gcf, 'audio_plots.png');
