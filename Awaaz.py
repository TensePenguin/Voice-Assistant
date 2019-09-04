from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
import pyaudio


def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en-ie')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')


def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am ready to talk")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said : " + command + "/n")

    except sr.UnknownValueError:
        assistant(myCommand())

    return command


def assistant(command):

    if 'open YouTube' in command:
        url = 'https://www.youtube.com'
        webbrowser.get(using=None).open_new_tab(url)

    if 'open email' in command:
        url = 'https://www.gmail.com'
        webbrowser.get(using=None).open_new_tab(url)

    if 'hello' in command:
        talkToMe('Hi, How are you Esh?')

    if 'your name' in command:
        talkToMe('My name is Awaaz')

    if 'stop' in command:
        talkToMe('Exiting Now')
        exit()


talkToMe('Do you need anything Esh?')

while True:
    assistant(myCommand())
