import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyowm
import requests
import json
import time
from PIL import Image
import PyPDF2





listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(speech):

    engine.say(speech)
    
    engine.runAndWait()

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!!')
  
  
# input time in seconds
#t = input("Enter the time in seconds: ")
  
## function call
#countdown(int(t))

def take_command():
    
    

    try: 
        with sr.Microphone() as source:
            print("I am listening to you...")
            audio = listener.listen(source)
            voice = listener.recognize_google(audio)
            voice = voice.lower()
            if 'mona' in voice:
               voice = voice.replace('mona', '')
               print(voice)
            
            elif 'set timer to ' in voice:
                t= voice.replace("set timer to", '')
                countdown(int(t))
                speak("timer is set")

            elif'who the heck' in voice:
                info = voice.replace('who the heck', '')
                output = wikipedia.summary( info ,1)
                print(output)
                speak(output)
            elif 'date' in voice:
                speak('sorry I am taken')
            elif 'love' in voice:
                speak('oh it is hard to answer for me')
            elif 'are you single' in voice:
                speak('i am in a relationship with coding')
            elif ' cute' in voice:
                speak("amm i think so")
            elif 'is bay  cute' in voice:
                speak("please don't ask this question again")
            elif 'joke' in voice:
                speak(pyjokes.get_joke())

            elif 'weather' in voice:
                owm = pyowm.OWM('7f92f39df655bcff2ade732c9615a1fc')
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place('yangon')
                weather = observation.weather
                print(weather.detailed_status)
                #print(weather.temp)
                #print(weather.rain)
                speak('today weather is'+ weather.detailed_status)
                '''speak('temperature is '+ weather.temp)
                speak('chance of rain is ' + weather.rain)'''
                
            elif 'show' in voice:
                im = Image.open(r'bay1.jpg')
                im.show()
                
            elif 'what is   stock today' in voice:
                word = voice.replace('what is  stock today', '')
                output = wikipedia.summary( word ,1)
                print(output)
                speak(output)

            elif ' pdf' in voice:
                pdf = open('java foundation.pdf','rb')
                reader = PyPDF2.PdfFileReader(pdf)
                pages = reader.numPages
                assistant = pyttsx3.init()
                page = reader.getPage(22)
                text = page.extractText()
                assistant.say(text)
                assistant.runAndWait()




        
    except:
        pass
    return voice



def run_bay():
    voice = take_command()
    print(voice)
    if 'play' in  voice:
        song =  voice.replace('play', '')
        speak("play"+ song)
        pywhatkit.playonyt(song)

run_bay()

'''elif 'time' in voice:
                time = datetime.datetime.now().strftime("%I:%M %p")
                print(time)
                speak("current time is " + time)'''


