import pyttsx3 #pip install pyttsx3 (For Speak)
import datetime 
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui (For Screenshot)
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import random
import operator
import json
import wolframalpha#pip install wolframalpha
import time
from urllib.request import urlopen
import requests
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisui import Ui_MainWindow

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
range =engine.setProperty('rate',170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M %p") 
    speak("the current time is")
    speak(Time)
    print(Time)
    
def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
    
def wishme():
    speak("HELLO RISHABH SIR! Welcome back !")
    print("HELLO RISHABH SIR Welcome back!")
    time_()
    
    
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour <24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("Jarvis at your service. Please tell me how can I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login('', '')
    server.sendmail('', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("screen.jpeg")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is'+ usage+'persent')
    #battery = str(psutil.sensors_battery())
    #speak("Battery level is")
    #speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def Introduction():
    speak("I am JARVIS upgraded version 2 point O , Personal AI assistant of Rishabh sir , "
    "I am created by Aayush sir , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also find definitions for you from wikipedia , "
    "and a lot more")

def Creator():
    speak("Aayush sir is an extra-ordinary person ,"
    "he has created me"
    "He has a passion for Robotics, Artificial Intelligence and Machine Learning ,"
    "He is very co-operative ,")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def TakeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.8
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(query)
            
        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        query = query.lower()
        return query
        

    def TaskExecution(self):
        wishme()    
        while True:
            self.query = self.TakeCommand()
            
            if 'time' in self.query:
                time_()
            elif 'date' in self.query:
                date()
            elif 'how are you' in self.query:
                speak("I am fine,Thanks for asking")

                speak("what about you sir")
                about = self.TakeCommand()
                if 'fine' in about or "good" in about or "nice" in about or "great" in about or "perfect" in about or"ok" in about:
                    speak("It's good to know that your fine")
                else:
                    speak("I hope you get well soon.")

            elif "change window" in self.query or "switch window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "switch to third window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "switch to previous window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("shift")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")                

            elif "change window" in self.query or "switch to next window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")


            elif 'wikipedia' in self.query:
                speak("Searching...")
                self.query = self.query.replace("wikipedia","")
                result = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            
            elif 'open youtube' in self.query:
                speak("sir! What should I search?")
                Search_term = self.TakeCommand()
                speak("Here we go to Youtube\n")
                wb.open("https://www.youtube.com/results?search_query="+Search_term)
                time.sleep(5)

            elif 'search edge' in self.query or 'search in edge' in self.query or 'search in microsoft edge' in self.query or 'search microsoft edge'in self.query or 'search in google' in self.query:
                speak("What should I search?")
                Search_term = self.TakeCommand()
                wb.open('https://www.bing.com/search?q='+Search_term)
                time.sleep(5)



            
            elif "who am i" in self.query or "who i am " in self.query:
                speak("If you can talk, then definitely you are a human")
            elif "why you came to this world" in self.query:
                speak("Thanks to aayush. further it is a secret")
                
            elif 'word' in self.query:
                speak("opening MS Word")
                word = r'Word path'
                os.startfile(word)

            elif 'what is love' and 'tell me about love' in self.query:
                speak("It is 7th sense that destroy all other senses , "
                "And I think it is just a mere illusion , "
                "It is waste of time")


            elif 'send email' in self.query:
                try:
                    speak("What should I say?")
                    content = self.TakeCommand()
                    speak("Who is the Reciever?")
                    reciept = input("Enter recieptant's name: ")
                    to = (reciept)
                    sendEmail(to,content)
                    speak(content)
                    speak("Email has been sent.")
                except Exception as e:
                    print(e)
                    speak("Unable to send the email.")
            elif 'open microsoft edge' in self.query:
                edgepath = 'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe'
                os.startfile(edgepath)


            elif 'log out' in self.query:
                os.system("shutdown -l")
            elif 'restart' in self.query:
                os.system("shutdown /r /t 1")
            elif 'shutdown' in self.query:
                os.system("shutdown /s /t 1")
            
            
            
            elif 'play songs' in self.query or 'play song' in self.query:                
                
                music_dir = 'C:\\Users\\Aayush\\Music\\songs'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            elif"play any other song" in self.query or "play second song" in self.query or "play another song" in self.query:
                music_dir = 'C:\\Users\\Aayush\\Music\\songs'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[1]))
                  
            elif "notepad" in self.query:
                speak("opening notepad")
                notepath = "D:\\notepad.exe"
                os.startfile(notepath)

            elif "close notepad" in self.query:
                os.system("TASKKILL /F /IM notepad.exe")
                time.sleep(2)    




            elif 'remember that' in self.query:
                speak("What should I remember ?")
                memory = self.TakeCommand()
                speak("You asked me to remember that"+memory)
                remember = open('memory.txt','w')
                remember.write(memory)
                remember.close()

            elif 'do you remember anything' in self.query:
                remember =open('memory.txt', 'r')
                speak("You asked me to remeber that"+remember.read())
            
            
            elif "write a note" in self.query:
                speak("What should i write, sir")
                note = self.TakeCommand()
                file = open('note.txt', 'w')
                speak("Sir, Should i include date and time")
                dt = self.TakeCommand()
                if 'yes' in dt or 'sure' in dt:
                    strTime = datetime.datetime.now().strftime("%I:%M %p")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                    speak('done')
                else:
                    file.write(note)
                    
            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("note.txt", "r")
                print(file.read())
                speak(file.read()) 

            elif "weather" in self.query: 
                
                api_key = "open weather api"
                base_url = "http://api.openweathermap.org/data /2.5/weather?q="
                speak(" City name ")
                print("City name : ")
                city_name = self.TakeCommand()
                complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                response = requests.get(complete_url)
                x = response.json()
                
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                    
                else:
                    speak(" City Not Found ") 
            
            elif "hello jarvis" in self.query or "hi jarvis" in self.query:
                speak("hello sir! how can i help you?")
                print("hello sir! how can i help you?")


                            
            elif 'take screenshot' in self.query:
                screenshot()
                speak("Done!")    
            elif 'cpu' in self.query:
                cpu()
            elif 'joke' in self.query:
                jokes()
            elif 'tell me about yourself'in self.query or 'who are you' in self.query:
                Introduction()
            elif 'tell me about Aayush'in self.query or 'creator' in self.query:
                Creator()
            
            #show location on map
            elif "jarvis where is" in self.query:
                self.query = self.query.replace("jarvis where is", "")
                location = self.query
                speak("User asked to Locate")
                speak(location)
                wb.open("https://www.google.com/maps/place/" + location + "")
                time.sleep(5)

            # most asked question from google Assistant
            elif "will you be my gf" in self.query or "will you be my bf" in self.query:
                speak("I'm not sure about, may be you should give me some time")
                
            elif "i love you" in self.query:
                speak("It's hard to understand, I am still trying to figure this out.")
            



            #sleep-time
            elif "don't listen" in self.query or "stop listening" in self.query:
                speak("for how much seconds you want me to stop listening commands")
                a = int(self.TakeCommand())
                time.sleep(a)
                print(a)

            #quit
            elif 'offline' in self.query:
                speak("going Offline")
                quit()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie =QtGui.QMovie("New folder/bg.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie =QtGui.QMovie("../JARVIS GUI/New folder/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        currunt_time = QTime.currentTime()
        currunt_date = QDate.currentDate()
        label_time = currunt_time.toString('hh:mm:ss')
        label_date = currunt_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)  


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

