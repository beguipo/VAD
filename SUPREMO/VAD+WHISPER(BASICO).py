import speech_recognition as sr
import wave
import whisper

recognizer = sr.Recognizer()

model = whisper.load_model("large-v3")

with sr.Microphone() as source:
    print("Di algo...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

    # Guardar el audio en un archivo .wav
    with wave.open("audio.wav", "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(44100)
        file.writeframes(audio.get_raw_data())

trasncripcion = model.transcribe("audio.wav")

print(f"Texto detectado: {trasncripcion['text']}")