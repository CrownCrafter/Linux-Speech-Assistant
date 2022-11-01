from gtts import gTTS
import os
from playsound import playsound
import webbrowser
from bs4 import BeautifulSoup as bs
import requests
from googlesearch import search
import speech_recognition
import pyttsx3
import re
import subprocess
import wikipedia
# Default Applications
def_terminal = 'alacritty'
# Speech Recognizer
rec = speech_recognition.Recognizer()

# Definitions
def ttsbot(text):
    output = gTTS(text,slow=False)
    output.save("last_said.mp3")
    playsound('last_said.mp3') 
def wikiscrape(query):
    try:
        text = wikipedia.search(query)[0]
        text = wikipedia.summary(text)
        text = text.split('. ')[0]
    except:
        text = wikipedia.suggest(query)
        text = wikipedia.summary(text)
        text = text.split('. ')[0]
    return text

t = input("Text or Speech")
if t == 'speech':
    ttsbot("What would you like to search for")
while True:
    if t == 'speech':
        try:
            with speech_recognition.Microphone() as mic:
                rec.adjust_for_ambient_noise(mic, duration=1)
                print("Listening")
                audio=rec.listen(mic)
                query=rec.recognize_google(audio)
                print(query)
            
        except speech_recognition.UnknownValueError():
            continue
    else:
        query = input("Enter query: ")
    if query.lower().startswith('search'):
        query = query.split()
        query = ' '.join(query[1:])
        text = wikiscrape(query)
        print(text)
        if t == 'speech':
            ttsbot(text)
        #print(wikipedia.summary(query))
        #s = ttsbot(wikipedia.summary(query))

        
    elif 'weather' in query.lower():
        # TODO IMPLEMENT
        ttsbot("Getting weather info")
    elif 'open' in query.lower():
        m = query.lower()
        if m.split()[1] == 'browser':
            webbrowser.open('https://www.google.com')
        elif m.split()[1] == 'terminal':
            subprocess.run(def_terminal)
        else:
            subprocess.run([m.split()[1]], shell=False)
    elif 'run' in query.lower().split()[0]:
        m = query.lower()
        m = m.lstrip('run')
        m = m.lstrip()
        m = m.split()
        m = ''.join(m)
        subprocess.run([m], shell=True)
    else:
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            if j.startswith('https'):
                if t == 'speech':
                    ttsbot("Opening Webpage") 
                webbrowser.open(j)
                break        