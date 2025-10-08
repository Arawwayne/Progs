import speech_recognition as sr
from googletrans import Translator
import datetime

# Настройки
recognizer = sr.Recognizer()
translator = Translator()
output_file = "translation_log.txt"

# Захват звука с микрофона или виртуального устройства (например, VB-Cable)
with sr.Microphone() as source:
    print("Слушаю корейскую речь...")
    while True:
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="ko-KR")  # Распознавание корейского
            translation = translator.translate(text, src="ko", dest="en")  # Перевод на английский
            
            # Запись в файл
            with open(output_file, "a", encoding="utf-8") as f:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] KO: {text}\n")
                f.write(f"[{timestamp}] EN: {translation.text}\n\n")
            
            print(f"Перевод: {translation.text}")
            
        except sr.UnknownValueError:
            print("Речь не распознана")
        except Exception as e:
            print(f"Ошибка: {e}")