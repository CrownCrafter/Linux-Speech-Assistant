#!/usr/bin/env python3

from gtts import gTTS
import os
from playsound import playsound
import webbrowser
import requests
from googlesearch import search
import speech_recognition
import pyttsx3
import sys
import subprocess
import wikipedia
# TODO Get Distro Base name
op_sys = 'arch'
# Default Applications
def_terminal = 'alacritty'
def_folder = '~/Documents/Dovah/'
# Speech Recognizer
rec = speech_recognition.Recognizer()
rec.dynamic_energy_threshold = False
rec.energy_threshold = 400
# Definitions
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 200, 200)
    win.setWindowTitle("Dovah")
    win.show()
    sys.exit(app.exec())
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
if '--text' not in sys.argv:
    ttsbot("What would you like to search for")
while True:
    if '--text' not in sys.argv:
        try:
            with speech_recognition.Microphone() as mic:
                rec.adjust_for_ambient_noise(mic, duration=1)
                print("Listening")
                audio=rec.listen(mic, timeout= 3)
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
        if '--text' not in sys.argv:
            ttsbot(text)
        #print(wikipedia.summary(query))
        #s = ttsbot(wikipedia.summary(query))

    #elif query.lower().startswith('watch'):
    #    query = query.split()
    #    query = ''.join(query[1:])
    #    webbrowser.open('https://www.youtube.com/c/'+query)
    elif 'weather' in query.lower():
        # TODO IMPLEMENT
        ttsbot("Getting weather info")
    elif query.lower().startswith('open'):
        m = query.lower()
        if m.split()[1] == 'browser':
            webbrowser.open('https://www.google.com')
        elif m.split()[1] == 'terminal':
            subprocess.run(def_terminal)
        else:
            subprocess.run(['xdg-open', '/home/ayushm/Documents/Dovah/goals.docx'], shell=False)
            #subprocess.run([m.split()[1]], shell=False)
    elif 'run' in query.lower().split()[0]:
        m = query.lower()
        m = m.lstrip('run')
        m = m.lstrip()
        m = m.split()
        m = ''.join(m)
        if m == 'update':
            if op_sys == 'arch':
                subprocess.run('xterm -e sudo pacman -Syu')
            elif op_sys == 'debian' or op_sys == 'ubuntu':
                subprocess.run('xterm -e sudo apt update && sudo apt upgrade')


        subprocess.run([m], shell=True)
    elif query.lower().startswith('exit'):
        if '--text' not in sys.argv:
            ttsbot("Exiting")
        break
    else:
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            if j.startswith('https'):
                if '--text' not in sys.argv:
                    ttsbot("Opening Webpage") 
                webbrowser.open(j)
                break
