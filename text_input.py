import webbrowser
from bs4 import BeautifulSoup
import requests
try:
    from googlesearch import search
except ImportError:
    print("Install Google")
def find_weather(city_name):
   city_name = city_name.replace(" ", "+")
 
   try:
       res = requests.get(
           f'https://www.google.com/search?q={city_name}&oq={city_name}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
      
       print("Loading...")
 
       soup = BeautifulSoup(res.text, 'html.parser')
       location = soup.select('wob_loc')[0].getText().strip()
       time = soup.select('wob_dts')[0].getText().strip()
       info = soup.select('wob_dc')[0].getText().strip()
       temperature = soup.select('wob_tm')[0].getText().strip()
 
       print("Location: " + location)
       print("Temperature: " + temperature + "°C")
       print("Time: " + time)
       print("Weather Description: " + info)
   except:
       print("Please enter a valid city name")
 
# to search
query = input("What would you like to search for: ")
if query.startswith('wiki'):
    webbrowser.open('https://en.wikipedia.org/w/index.php?search='+query.lstrip('wiki'))
elif 'weather' in query.lower():
    city_name = input("Enter City: ")
    find_weather(city_name)
else:
    for j in search(query, tld="co.in", num=1, stop=1, pause=3):
        if j.startswith('https'):
            webbrowser.open(j)
            break
    