import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("hello, I am alexa. How can I help you Sir")
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace('alexa ', '')
                # print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play ', '')
        talk("playing" + song)
        print("Playing....")
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is" + time)
        print(time)
    elif 'tell me about' in command:
        search = command.replace('tell me about ', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    else:
        talk("Unable to understand. please say it again")
        print("Unable to understand. Please say it again....")


while True:
    run_alexa()
