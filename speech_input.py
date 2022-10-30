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
# Speech Recognizer
rec = speech_recognition.Recognizer()

# Definitions
def ttsbot(text):
    output = gTTS(text,slow=False)
    output.save("last_said.mp3")
    playsound('last_said.mp3') 
def wikiscrape(url):
    
    page = requests.get(url)
    soup = bs(page.content,'html.parser')
    text = soup.find_all('p')[0]
    text = str(text)
    text = text.split('. ')[0]
    text = re.sub(r'\[[0-9]*\]',' ',text)
    # Print string after removing tags
    return re.compile(r'<[^>]+>').sub('', text)
ttsbot("What would you like to search for")
while True:
    try:
        with speech_recognition.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic, duration=1)
            print("Listening")
            audio=rec.listen(mic)
            query=rec.recognize_google(audio)
            print(query)
            
    except speech_recognition.UnknownValueError():
        continue
    if query.startswith('search'):
        query = query.split()
        query = ' '.join(query[1:])
        print(query)
        s = wikiscrape('https://en.wikipedia.org/w/index.php?go=Go&search='+query)

        print(s)
        try:
            ttsbot(s)
        except:
            print("No text found")
        
    elif 'weather' in query.lower():
        # TODO IMPLEMENT
        ttsbot("Getting weather info")
    elif 'open' in query.lower():
        m = query.lower()
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
                ttsbot("Opening Webpage") 
                webbrowser.open(j)
                break        