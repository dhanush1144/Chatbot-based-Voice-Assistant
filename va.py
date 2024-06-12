import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import subprocess
import os
import pyautogui
from time import sleep

#Replace with your chrome path
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
voicespeed = 200
engine.setProperty('rate', voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("welcome back sir")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 2:
        speak("Good morning")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("how can i help u?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = new_func(r, source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio)
    except Exception as e:
        print(e)
        print("---")

        return "None"
    return query


def new_func(r, source):
    audio = new_func1(r, source)
    return audio


def new_func1(r, source):
    audio = r.listen(source)
    return audio


def open_chrome():
    url = "https://www.google.co.in/"
    webbrowser.get(chrome_path).open(url)


def open_yt():
    url = "https://www.youtube.com/"
    webbrowser.get(chrome_path).open(url)


# main
if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()

        elif "open chrome" in query:
            speak("opening the Chrome")
            open_chrome()
        elif "open youtube" in query:
            speak("opening the youtube")
            open_yt()
        elif "search" in query:
            speak("what should i search?")
            search = takeCommand().lower()
            webbrowser.get(chrome_path).open_new_tab(search)
        elif "offline" in query:
            speak("going offline")
            quit()
        elif "logout" in query:
            speak('logging out in 5 second')
            sleep(5)
            os.system("shutdown - l")

        elif "shutdown" in query:
            speak('shutting down in 5 second')
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak('restarting in 5 second')
            sleep(5)
            os.system("shutdown /r /t 1")


        else:
            print("invalid")

