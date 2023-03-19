import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import sys
import os
import requests
from google_trans_new import google_translator
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
# from gui import Ui_MainWindow


# weather_api_key = os.environ.get('weather_api_key')
# api_link = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={command}&appid={weather_api_key}')
# api_data = api_link.json()
# print (api_data)
# print(weather_api_key)
trans = google_translator()
pardon = None
jarvis=1
friday=4
lang = 'en'
gender=jarvis
rate = 190
listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[gender].id)

def calculate(command):
    command = command.replace('calculate', '')
    command = command.replace('multiply by', '*')
    command = command.replace('multiply', '*')
    command = command.replace('into', '*')
    command = command.replace('divided by', '/')
    command = command.replace('divide', '/')
    command = command.replace('x', '*')
    command = command.replace(' ', '')
    print (command)
    result = eval(command)
    return result

def speak(text):
    global lang, pardon
    engine.setProperty('rate', rate)   
    engine.setProperty('voice', voices[gender].id)
    if lang=='hi':
        text = trans.translate(text, lang_tgt=lang)
    if type(text)=='string':
        text = text.replace('शुक्रवार', 'फ्राइडे')
    # jarvisgui.change()
    engine.say(text)
    print(text)
    pardon = text
    engine.runAndWait()



class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        
    def run1(self):
        self.run()


    # region                                                                                Defining Dependent Functions

    def tk_command(self):
        global lang
        with sr.Microphone() as source:
            print("listening...")
            # listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source=source, timeout=None, phrase_time_limit=5)
            try:
                print('Recognizing...')
                self.command = listener.recognize_google(voice, language=lang)
                print("Step 1")
                self.command = trans.translate(self.command, lang_tgt="en")
                print("Step 3")
                return self.command
                print("Step 4")
            except Exception as e:
                self.command = self.tk_command()
                return self.command

    def hotword(self):
        global gender, jarvis, friday
        self.command = self.tk_command()
        self.command = self.command.lower()
        if 'jarvis' in self.command:
            if 'shut down' in self.command or 'turn off' in self.command or 'shutdown' in self.command:
                gender=jarvis
                speak('Shutting down... I hope you will call me again soon')
                sys.exit()
            else:
                gender=friday
                speak("Jarves, hey buddy. You're up.")
                gender=jarvis
                speak('Well, I am here to assist')
                print (self.command)
                self.run()
        elif 'friday' in self.command:
            if 'shut down' in self.command or 'turn off' in self.command or 'shutdown' in self.command:
                gender=friday
                speak('Shutting down... I hope you will call me again soon')
                sys.exit()
            else:
                gender=jarvis
                speak("Hey Friday, it's your call")
                gender=friday
                speak('Ok, how can I assist')
                print (self.command)
                self.run()
        else:
            print (self.command)

    # endregion

    def run(self):
        global rate, gender, jarvis, friday, lang, pardon
        while True:
            # region                                                                        Taking command input
            self.command = self.tk_command()
            self.command = self.command.lower()
            if 'talk' not in self.command:
                if 'jarvis' in self.command:
                    self.command = self.command.replace('jarvis', '')
                    gender = jarvis
                elif 'friday' in self.command:
                    self.command = self.command.replace('friday', '')
                    gender = friday
            # endregion

            ''' Functioning of various commands are described below
                as multiple elif statements '''

            # region                                                                                Task_Execution

            if (('play' in self.command or 'search' in self.command) and 'youtube' in self.command) and 'google' not in self.command:         # Play or search on youtube
                song = self.command.replace('play', '')
                song = song.replace('youtube', '')
                song = song.replace('on', '')
                song = song.replace('for', '')
                speak('Playing.'+ song)
                pywhatkit.playonyt(song)
            
            elif ('send' in self.command or 'message' in self.command) and 'whatsapp' in self.command:                                   # Sending a Whatsapp message
                if 'to' not in self.command:                 # Check if phone number is input
                    speak('''Please say the command with a phone number or a contact name.
                        To save a new contact say, Save... your phone number... 
                            as... name of the recepient.''')
                else:                                   # Else Send the message
                    self.command = self.command.replace('send', '')
                    self.command = self.command.replace('whatsapp', '')
                    self.command = self.command.replace('message', '')
                    self.command = self.command.replace('to', '')
                    self.command = self.command.replace('on', '')
                    try:
                        number = int(self.command.replace(' ',''))
                        speak("Sure, what's the message.")
                        message = self.tk_command()
                        pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)
                    except Exception as e:
                        speak('Invalid number or contact, please try again.')
                        print (self.command)
                        self.run()
            
            elif 'time' in self.command:                                                                                       # Asking what time is it
                time = datetime.datetime.now().strftime('%I:%M:%S %p')
                speak('Right now, its, '+ time)
            
            elif ('search google for' in self.command) or (('search' in self.command) and ('on google' in self.command)):                # Searches anything on google
                print('Google Search')
                self.command=self.command.replace('search google for', '')
                self.command=self.command.replace('search', '')
                self.command=self.command.replace('on google', '')
                self.command=self.command.replace(' ', '+')
                pywhatkit.search(self.command)
                
            elif (('who' in self.command or 'what' in self.command) and ('is' in self.command)) or ('wikipedia' in self.command):             # Searches wikipedia for anything or anyone
                print(self.command)
                print('Wikipedia Search')
                lines = 1
                if 'explain' in self.command:
                    lines = 3
                    self.command = self.command.replace('explain', '')
                self.command = self.command.replace('who', '')
                self.command = self.command.replace('what', '')
                self.command = self.command.replace('is', '')
                self.command = self.command.replace('wikipedia', '')
                try:
                    info = wikipedia.summary(self.command, lines)
                    rate -= 20
                    speak(info)
                    rate += 20
                except Exception as e:
                    speak(f'No results for {self.command} on wikipedia')

            elif 'open' in self.command or 'turn on' in self.command:                                                               # Opens any application or settings
                self.command = self.command.replace('open', '')
                # self.command = self.command.replace(' ', '')
                try:
                    os.system('C:\\Program Files\Google\Chrome\Application\Chrome.exe')
                except Exception as e:
                    speak(Exception)

            elif ('shut' in self.command and 'down' in self.command) or 'turn off' in self.command:                                      # Shutdowns the program
                speak('Shutting down... I hope you will call me again soon')
                sys.exit()

            elif ('sleep' in self.command) or ('rest' in self.command):                                                             # Program goes to sleep
                speak('Entering sleep mode. Just say my name if you need anything, I\'ll be right here')
                print (self.command)
                break

            elif ('talk' in self.command and 'jarvis' in self.command) or self.command == 'jarvis':                                      # Activate male voice
                gender = jarvis
                speak('How can I be of service...')

            elif ('talk' in self.command and 'friday' in self.command) or self.command == 'friday':                                      # Activate female voice
                gender = friday
                speak('How can I be of service...')

            elif 'calculate' in self.command:                                                                                  # Calculates mathematical expressions
                try:
                    result = calculate(self.command)
                except Exception as e:
                    speak('Ok, what is the expression')
                    self.command = self.tk_command()
                    result = calculate(self.command)
                speak(int(result))

            elif 'change' in self.command and 'language' in self.command:                                                           # Changes language to Hindi or English
                if 'hindi' in self.command:
                    lang = 'hi'
                    engine.setProperty('language', lang)
                    jarvis = 2
                    friday = 3
                    if (gender == 1 and 'friday' not in self.command) or 'jarvis' in self.command:
                        gender = jarvis
                        speak('Good then, now I will talk to you in your native language')
                    elif (gender == 4 and 'jarvis' not in self.command) or 'friday' in self.command:
                        gender = friday
                        speak('Good then, now I will talk to you in your native language')
                elif 'english' in self.command:
                    lang = 'en'
                    engine.setProperty('language', lang)
                    jarvis = 1
                    friday = 4
                    if (gender == 2 and 'friday' not in self.command) or 'jarvis' in self.command:
                        gender = jarvis
                        speak('Your language is changed to english now')
                    elif (gender == 3 and 'jarvis' not in self.command) or 'friday' in self.command:
                        gender = friday
                        speak('Your language is changed to english now')

            elif 'pardon' in self.command or 'what did you say' in self.command or 'repeat' in self.command:                             # Pardons the last command
                speak(pardon)

            else:
                print (self.command)
                speak('I didn\'t recognize this command')
            
            # endregion

startexec = MainThread()

# class Main(QMainWindow):
#     change = 0
#     def __init__(self):
#         super().__init__()
#         self.ui = QMainWindow()
#         self.ui.setupUi(self)
#         self.ui.Run.clicked.connect(self.startTask)
#         self.ui.Terminate.clicked.connect(self.close)
        
#     def startTask(self):
#         self.ui.movie = QMovie("../gui_images/slow.gif")
#         self.ui.bgimg.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.movie = QMovie("../gui_images/LVum.gif")
#         self.ui.loadingimg.setMovie(self.ui.movie)
#         self.ui.movie.start()
#         self.ui.Run.setText("Sleep")
#         running = 1
#         startexec.start()
        
#     def change(self):
#         self.ui.movie = QMovie("../gui_images/fast.gif")
#         self.ui.bgimg.setMovie(self.ui.movie)
#         self.ui.movie.start()
        
# app = QApplication(sys.argv)
# jarvisgui = Main()
# jarvisgui.show()
# exit(app.exec_())

# if __name__ == '__main__':
#     while True:
#         hotword()
