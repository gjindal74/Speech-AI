import subprocess
import os
import pyttsx3
from getanswer import Fetcher
hi = pyttsx3.init()




class Commander:
    def __init__(self):
        self.confirm = ["Yes", "Affirm", "Sure", "Do it", "Yeah"]
        self.cancel = ["no", "dont", "not", "cancel", "nah"]

    def discover(self, text):
        if "my name" in text:
            self.respond("You haven't told me your name yet")
        elif "what" in text and "your name" in text:
            self.respond("My name is Speech AI. How are you?")
        elif "open" in text:
            app = text.split(" ", 1)[-1]
            self.respond("opening" + app)
            subprocess.Popen(app, shell=True)

        else:
            f = Fetcher("https://www.google.com/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)
    def respond(self, response):
        print(response)
        hi.say(response)
        hi.runAndWait()
