import pyglet
import speech_recognition as sr
import pyttsx3
from commands import Commander

engine = pyttsx3.init()

running = True
def say(text1):
    engine.say(text1)
    engine.runAndWait()



r = sr.Recognizer()
def initSpeech():
    cmd = Commander()
    print("Listening...")
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

        command = ""

        try:
            command = r.recognize_google(audio)
        except:
            print("Couldn't understand")
            command = "quit"

        print("Your Command")
        print(command)
        if command in ["quit", "exit", "bye", "goodbye", "terminate"]:
            global running
            running = False

        else:
            cmd.discover(command)
        #say('you said' + command)


while running == True:
    initSpeech()


