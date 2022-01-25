import re
import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
        return query

    except speech_recognition.UnknownValueError:
        return "Что ты там сказал????"

def greeting():
    """Greeting function"""


    return "Привет нищеброд!"

def create_task():
    """create todo list"""
    
    print("Что добавим в список?")
    
    query = listen_command()

    with open("todo-list", "a") as file:
        file.write(f"   {query}\n")

        return f"Задаяа {query} добавлена в todo-list!"

def main():
    query = listen_command()

    if query == "привет":
        print(greeting())
    elif query == "добавить задачу":
        print(create_task())
    else:
        print("Прожуй, потом говори!")

if __name__ == "__main__":
    main()
