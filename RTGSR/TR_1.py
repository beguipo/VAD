import speech_recognition as sr

def ejecutar_funcion():
    print("¡Palabra detectada! Ejecutando función.")

def escuchar_microfono():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Di algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Utiliza Google Web Speech API para reconocimiento de voz
        texto = recognizer.recognize_google(audio, language="es-ES")
        print(f"Texto detectado: {texto}")

        # Verifica si la palabra clave está en el texto
        if "mundo" in texto.lower():
            ejecutar_funcion()
        else:
            print("Palabra clave no detectada.")

    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print(f"Error en la solicitud al servicio de reconocimiento de voz; {e}")

if __name__ == "__main__":
    escuchar_microfono()
