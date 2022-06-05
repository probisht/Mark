import socket
import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import os
import random
from selenium import webdriver
from pygame import mixer
from bs4 import BeautifulSoup
import requests, json
import pyautogui
import psutil


engine=pyttsx3.init()
mixer.init()

def speak(message) :

    engine.say(f'{message}')
    engine.runAndWait()



def wish() :

    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12 :
        speak("Good Morning! Sir! I am Mark")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon! Sir! I am Mark")
    else :
        speak("Good Evening! Sir! I am Mark")



def voice_input() :

    #Takes voice as input using microphone

    r=sr.Recognizer()
    audio=''

    chunk_size=2048

    with sr.Microphone(chunk_size=chunk_size) as source :
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source,phrase_time_limit=5)

    try :
        print("Recognizing...")
        text=r.recognize_google(audio,language="en-in")
        print(f"User said : {text}\n")
        return text

    except Exception as e :
        print("Unable to Recognize, say that again please...")
        speak("Sorry Sir! I didn't get you. Say that again please..")
        time.sleep(2)
        return 0



def is_internet():
    try:
        socket.create_connection(('Google.com',80))
        return True
    except Exception as e:
        print(e)
        return False



def online():
    
    speak('completing initial checks,')
    speak('checking all files and drivers,')
    speak('establishing connections')
    speak('please wait a moment sir')
       
    
    time.sleep(5)
    speak('all systems have been started')
    speak('now i am online sir')


def curr_time():
    strTime = time.strftime("%I:%M %p")
    speak(f"Time is {strTime}")
    print(strTime)

def curr_date():
    dat = datetime.datetime.now().date()
    day=time.strftime("%A")
    speak(f"Today's is {day} {dat}")
    print(dat)



def curr_loc():
    response = requests.get('https://ipinfo.io/')
    if response.status_code == 200:
        data = response.json()
        city = data['city']
        return city
    else:
        print("Error in the HTTP request")


def curr_temprature():   
    #city="temprature of delhi"
    city=f"temprature of {curr_loc()}"
    url=f"https://www.google.com/search?q={city}"

    r=requests.get(url)

    d=BeautifulSoup(r.text,"html.parser")
    temp = d.find("div",class_="BNeawe").text
    print(f"Temperature: {temp} Celcius")
    speak(f'Current Temperature is {temp}')


def go_offline():
    speak('Bye Sir ! See You soon. ')
    time.sleep(1)
    speak('closing all systems')
    speak('disconnecting to servers')
    speak('going offline')
    #mixer.music.load('off.mp3')
    #mixer.music.play()
    #quit()


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)


greet=['hello','hi','whatsup']

def text_processing(query):


    if query in greet:
        speak(" At your service Sir")
        return


    elif "who are you" in query or "introduce yourself" in query:
        speak("Sir, I am Mark, Your Personal Assistant,"
                " I am here to make your tasks easier. I can help you out by carrying out your various tasks,"
                "such as opening applications,web surfing and many more ")
        return


    elif "who made you" in query or "who created you" in query:
        speak("I developed under the project work of Kailash Bisht")
        return


    elif 'how are you' in query:
        speak("I am fine Sir!")
        return


    elif 'thank you' in query or 'thankyou' in query:
        speak('You are Welcome Sir!')
        return


    elif 'what is time' in query :
        speak("Alright, Wait for a moment!")
        curr_time()
        return


    elif 'date today' in query:
        curr_date()
        return


    elif 'day today' in query:
        day=time.strftime("%A")
        speak(f"Today is {day}")
        return


    elif 'weather today' in query or 'current temperature' in query or 'how is the day' in query :
        speak('Weather Report of city Sir!')
        curr_temprature()
        return


    elif 'screenshot' in query or 'snapshot' in query:
        speak('Wait a moment Sir!')
        pic = pyautogui.screenshot()
        pic.save('C:/Users/Kailash/Desktop/Screenshot1.png')
        speak("Ok Sir Done. Check your Desktop")
        return


    elif 'charge remaining' in query or 'battery remaining' in query :
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = int(battery.percent)
        time_left = secs2hours(battery.secsleft)
        print(percent)
        if plugged:
            print("don't worry, sir charger is connected, i am charging")
        else:
            if percent < 20:
                print('sir, please connect charger because i can survive only ' + time_left)
            else:
                print('sir, i can survive ' + time_left)


    elif "youtube" in query:
        speak("Alright, Opening YouTube Wait a moment!")
        driver = webdriver.Chrome()
        driver.get("https://www.youtube.com/?gl=IN")
        time.sleep(10)
        return


    elif 'wikipedia' in query:
        speak('Searching wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=1)
        speak("According to wikipedia")
        print(results)
        speak(results)
        #driver = webdriver.Chrome()
        #driver.get(f"https://www.google.com/?#q={query}")
        return


    elif "google" in query:
        speak("Alright, Opening Google in a moment!")
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        time.sleep(10)
        return


    elif 'github' in query:
        speak('Taking you there Sir!')
        driver = webdriver.Chrome()
        driver.get("https://github.com/")
        time.sleep(10)
        return

    elif 'facebook' in query:
        speak('Alright! Opening Facebook in a moment.')
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/login/")
        time.sleep(10)
        return

    elif 'gmail'in query:
        speak("Alright! Opening Gmail ")
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/gmail/")
        time.sleep(10)
        return


    elif 'go offline' in query:
        go_offline()
        quit()


    else:
        try:
            speak("OK! I got it")
            driver=webdriver.Chrome()
            #driver.get(f"https://www.google.com/?#q={query}")
            driver.get('https://www.google.com')
            inputElem=driver.find_element_by_name("q")
            inputElem.send_keys(query)
            time.sleep(2)
            button=driver.find_element_by_name("btnK")
            button.click()
            time.sleep(10)
            speak("Hope you are satisfied with results")
            return
        except Exception as e:
            print('Failed! to Load! Incomplete Session ')



def open_application(query):

    if "adobe reader" in query:
        speak("Alright! Opening Adobe Reader, wait a moment")
        os.startfile("C:\\Program Files (x86)\\Adobe\Acrobat Reader DC\\Reader\\AcroRd32.exe")
        return


    elif "chrome" in query:
        speak("Alright, Opening Google Chrome Wait for a moment!")
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        return


    elif "mozilla" in query or "firefox" in query:
        speak("Alright, Opening Mozilla Firefox Wait for a moment!")
        os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        return


    elif "ms word" in query:
        speak("Alright, Opening Microsoft Word Wait for a moment!")
        os.startfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
        return


    elif 'play music' in query:
        speak("Alright, Playing music in a while !")
        music_dir = "H:\\P\\Songs\\Arijit Singh"
        song = os.listdir(music_dir)
        res = random.choice(song)
        os.startfile(os.path.join(music_dir, res))
        print(f"Playing \n {res}")
        return


    elif 'vs code' in query:
        speak("Alright, opening VS Code in a while")
        path = "C:\\Users\\Kailash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)
        return


    elif "my pc" in query:
        speak("Alright, Opening This PC")
        os.startfile("C:\\Users\\Kailash\\Desktop\\My PC.lnk")
        return

    elif 'control panel' in query:
        speak("Alright! Opening Control Panel")
        os.startfile("C:\\Users\\Kailash\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk")
        return

    elif 'open run' in query:
        speak("Alright! Wait a moment")
        os.startfile("C:\\Users\\Kailash\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run.lnk")
        return


    elif 'open notepad' in query or 'editor' in query:
        speak("Alright, Opening Editor")
        os.startfile("C:\\Program Files (x86)\\Notepad++\\notepad++.exe")
        return


    elif 'cmd' in query or "terminal" in query:
        speak("Alright, opening command line in a while")
        linepath = "C:\\WINDOWS\\system32\\cmd.exe"
        os.startfile(linepath)
        return


    elif 'open settings' in query:
        speak("Alright! Opening Settings ")
        os.system('start ms-settings:')
        return


    elif 'open task manager' in query:
        speak("Alright! Opening Task Manager")
        os.system("start taskmgr")
        return


    elif 'windows media player' in query:
        speak("Alright! Opening Windows Media Player")
        os.system('start wmplayer')
        return


    elif 'open paint' in query:
        speak("Alright! Opening MS Paint")
        os.system('start mspaint')
        return


    elif 'environment variables' in query:
        speak('Alright! Opening System Environment Variables Editor')
        os.system('start rundll32.exe sysdm.cpl, EditEnvironmentVariables')
        return


    elif 'device manager' in query:
        speak('Alright! Opening Device Manager')
        os.system('start devmgmt.msc')
        return


    elif 'open store' in query:
        speak('Alright! Opening Windows Store')
        os.system('start ms-windows-store:')
        return


    elif 'pycharm' in query:
        speak("Alright! Opening Pycharm")
        os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1\\bin\\pycharm64.exe")
        return


    elif 'calculator' in query:
        speak("Alright! Opening Calculator")
        os.startfile("C:\\Windows\\System32\\calc.exe")
        return


    elif 'python' in query:
        speak("Alright! Opening Python Editor")
        os.startfile("C:\\Users\\Kailash\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib\\idle.pyw")
        return


    else:
        try:
            speak("Here I found something for you!")
            driver=webdriver.Chrome()
            driver.get(f"https://www.google.com/?#q={query}")
            speak("Hope you are satisfied with results")
            return
        except Exception as e:
            print('Failed! to Load! Incomplete Session ')




if __name__=='__main__' :

    
    if is_internet():
        online()
        time.sleep(1)
        wish()
        time.sleep(2)
        curr_time()
        time.sleep(2)
        curr_date()
        time.sleep(2)
        curr_temprature()
        while True:
            time.sleep(1)
            speak("What's next Sir!")
            text = voice_input()

            if text == 0:
                continue

            text=text.lower()


            if 'bye' in str(text) or "exit" in str(text):
                go_offline()
                time.sleep(2)
                mixer.music.load('mus2.mp3')
                mixer.music.play()
                time.sleep(6)
                speak("Have a good day sir!!")
                break

            elif 'open' in str(text) or 'launch' in str(text):
                open_application(text)

            else:
                text_processing(text)

    else:
        speak('Sorry about that, can\'t connect at the moment')
        time.sleep(2)
        speak('Try again after establishing internet connection')
        