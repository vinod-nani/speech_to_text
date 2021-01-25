import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import smtplib
import webbrowser as wb
import psutil
import pyjokes
import pyjokescli
import json
import requests
from urllib.request import urlopen
import random

#import wolframalpha
#from urllib.request import urlopen
#from html.parser import HTMLParser

engine = pyttsx3.init()
wolframalpha_app_id = 'Y4G297-697GY3R287'
#engine.say("hello world!")
#engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%I:%H:%S")
    #speak("Good Morning Soumya")
    speak("the current time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Narasimha")
    speak("How are you?")
    speak("I hope you doing well!!")
    #speak("I tell you date and time")
    time_()
    date_() 
    
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Narasimha !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Narasimha!")
    elif hour<=18 and hour<24:
        speak("Good Evening Nani")
    else:
        speak("Good Night Nani ")
    
    speak("Iron Man at your service. How can i help you sir")

#wishme()


def Take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening................")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...............")
        query = r.recognize_google(audio,language='en-US')
        print(query)
        
    except Exception as e:
        print(e)
        print("say that again please...............,,,,")
        return "None"
    return query

#Take()

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startls()

    server.login('lakshminarasimha1999@gmail.com','SivaRama@789')
    server.sendmail('lakshminarasimha1999@gmail.com',to,content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)



if __name__ == "__main__":
    #wishme()
    while True:
        query = Take().lower()

        if 'time' in query:
            time_()

        elif 'date' in query:
            date_()

        elif 'wikipedia' in query:
            speak("Searching..........")
            query = query.replace('wikipedia',' ')
            result = wikipedia.summary(query,sentences=3)
            speak('According to wikipedia')
            print(result)
            speak(result)


        elif 'cpu' in query:
            cpu()
        
        elif 'search in chrome' in query:
            speak("What should i search?")
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application'

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')


        elif 'youtube' in query:
            speak('What shoul i search')
            search_Term = Take().lower()
            speak("opening youtube")
            wb.open("https://www.youtube.com/results?search_query="+search_Term)


        elif 'offline' in query:
            speak("Going Offline!@")
            quit()


        elif 'news' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=9c228962819b474b8eb3270b421eb744")
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=9c228962819b474b8eb3270b421eb744")
                data = json.load(jsonObj)
                i = 1

                speak("Here are some top headlines")
                print("++++++++++TOP HEADLINES+++++++++"+"\n")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))

        
        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        elif 'what' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('what')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The Answer is:'+answer)
            speak('The Answer is:'+answer)

        elif 'exit' or 'shutdown' or 'close' in query:
            speak("Going offline Sir!")
            quit()
            



            




        '''elif 'send' in query:
            try:
                speak("what should i say?")
                content = Take()

                speak("who is the receiver")
                receiver = input("enter receiver's Email id:")

                #receiver = 'lakshminarasimha1999@gmail.com'
                to = receiver
                sendEmail(to,content)
                speak(content)
                speak('email has been sent')

            except Exception as e:
                print(e)
                speak("not send")

        elif 'chrome' in query:
            speak('What should I Search Bro!!?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
'''
        
            
      


        





