%%Lectura de Tablas
dataW = readtable('Tiempos.xlsx','Sheet','Whisper');
dataG = readtable('Tiempos.xlsx','Sheet','Google (Free API)');
dataD = readtable('Tiempos.xlsx','Sheet','Deepgram (Free Test)');
dataV = readtable('Tiempos.xlsx','Sheet','Vosk');

%%Adquisicion de datos de Whisper
Whisper_L_T = dataW(1:7,3);
Whisper_L_B = dataW(1:7,4); %Contiene un NaN
Whisper_L_S = dataW(1:7,5);

Whisper_D_T = dataW(31:37,3);
Whisper_D_B = dataW(31:37,4);
Whisper_D_S = dataW(31:37,5);
Whisper_D_M = dataW(38:44,6);
Whisper_D_L3 = dataW(38:44,7);
Whisper_D_L3 = table(str2double(Whisper_D_L3.Var7),'VariableNames',{'Var1'}) %Adquiria los datos de manera diferente a los demas

%Adquisicion Datos Vosk
VoskD_D = dataV([11:17],3)
VoskD_L = dataV([28:34],3)

%%Adquisicion datos Speech Recognition (Google Free API)
GFA = dataG([1:7],2)

%%Adquisicion datos de DeepGramm (Free Test - 3 cent)
DFT = dataD([1:7],2)

%%Diagrama de cajas
lbls = {'MX330 Whiper Tiny','MX330 Whiper Base','MX330 Whiper Small','RTX4070 Whiper Tiny','RTX4070 Whiper Base','RTX4070 Whiper Small','RTX4070 Whiper Medium','RTX4070 Whiper Large-v3', 'Speech Recongition (Google)', 'Deepgram', 'Ryzen 5 5800X3D Vosk', 'i7-10510U Vosk'}
data = [Whisper_L_T.Tiempos,Whisper_L_B.Var4,Whisper_L_S.Var5,Whisper_D_T.Tiempos,Whisper_D_B.Var4,Whisper_D_S.Var5,Whisper_D_M.Trancripci_n,Whisper_D_L3.Var1,GFA.Tiempo,DFT.Tiempo,VoskD_D.Tiempo,VoskD_L.Tiempo]

h = boxplot(data, 'Labels',lbls)
yticks(0:0.2:3.4);



% Agregar líneas transparentes para guiar
hold on;
for y_val = 0:0.5:3.4
    plot([0.5, length(h)+0.5], [y_val, y_val], '--', 'Color', [0, 0, 0, 0.3], 'LineWidth', 0.5);
end
hold off;

xlabel('Modelos');
ylabel('Tiempo (s)');