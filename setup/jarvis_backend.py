import pyttsx3
import speech_recognition as sr
import pyautogui
import openai
import webbrowser
import datetime
import os
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtCore import QThread
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvis_fronted import Ui_MainWindow

openai.api_key='api_key'

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

r=sr.Recognizer()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hours=int(datetime.datetime.now().hour)
    if hours >=0 and hours<12:
        speak(f"Good Morning  Sir ")
    elif hours>=12 and hours <18:
        speak(f"Good Afternoon Sir")
    elif hours>=18 and hours<24 :
        speak(f"Good Evening Sir")

def invoke():
    print("Start")
    command = ""
    while "jarvis" or "wake up" or "wake" not in command:
        with sr.Microphone() as Source:
            print("Listening...")
            audio=r.listen(source = Source, timeout= None, phrase_time_limit= 5)
        try:
            print("Recognizing...")
            command=r.recognize_google(audio,language='en-in')
            print(f"{command}")
            if "jarvis" or "wake up" or "wake" in command.lower():
                speak("At your service sir !!")
                return True
        except Exception as e:
            print("Face exception ")
            command = invoke()
            return command
            
def chatgpt_service(message):
    chat= openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": message}
    ]
    )
    reply = chat.choices[0].message.content
    lst=reply.split()
    if len(lst)>=50:
        text=" ".join(lst[:len(lst)//2])
    else:
        text=" ".join(lst)
    return text

cmds=Ui_MainWindow()


class jarvis_backend(QThread):
    def __init__(self):
        super(jarvis_backend,self).__init__()

    def run(self):
        self.task_execution()

    def filter_command(self,command):
        if "Jarvis" in command:
            command=command.replace("Jarvis","")
            return command
        else:
            return command
    
    def tak_commands(self):
        global r
        with sr.Microphone() as Source:
            speak("please tell your query sir?")
            print("Listening...")
            r.pause_threshold=1
            audio=r.listen(source = Source, timeout= None, phrase_time_limit= 5)
        try:
            speak("Recognising...")
            print("Recognising...")
            command_unf=r.recognize_google(audio,language='en-in')
            print(f"User asked for  {command_unf}")
            command=self.filter_command(command_unf)
            print(f"User asked for  {command}")
            # cmds.change_text1(command)
            return command
        except Exception as e:
            speak("Say That Again Please..")
            command = self.tak_commands()
            return command
        
    def task_execution(self):
        wish()
        a = True
        while a:
            self.command=self.tak_commands()

            if "introduce"in self.command:
                speak("Sir , I am Jarvis 2.0 at your service, a intelligent python program programmed by Kuntal Mukherjee")
                speak(" how can I help you sir?")
            elif " volume up" in self.command:
                pyautogui.press("volumeup")
            elif "volume down" in self.command:
                pyautogui.press("volumedown")
            elif " volume mute" in self.command:
                pyautogui.press("volumemute")
            
            elif "battery percentage" in self.command:
                import psutil
                battery= psutil.sensors_battery()
                percentage=battery.percent
                speak(f"sir we are left with {percentage} percentage of battery")
                print(percentage)
                if percentage >=75 :
                    speak(" sir , we have enough battery support to continue")
                elif percentage< 75 and percentage>=30:
                    speak("sir , system may need cahrging in a few minutes")
                elif percentage <30:
                    speak("sir, system needs immediate charging ")
            elif "sleep" in self.command:
                speak("Going to sleep sir")
                a = invoke()
            elif "time" in self.command:
                time_Now=datetime.datetime.now().strftime('%H hour:%M minute:%S second')
                speak(f"Sir ,  the time is {time_Now}")

            elif "play intro" in self.command:
                music_dir="C:\\Users\\KUNTAL MUKHERJEE\\Music"
                songs=os.listdir(music_dir)
                print(songs)
                speak("playing favourite song of Tony stark")
                os.startfile(os.path.join(music_dir,songs[2]))
            elif "open code" in self.command:
                code_way="C:\\Users\\KUNTAL MUKHERJEE\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                speak("opening visual studio code")
                os.startfile(code_way)
                # break
            elif "open youtube" in self.command:
                speak("opening youtube")
                webbrowser.open('youtube.com')
            elif "open google" in self.command:
                speak("opening google for you sir , in a minute")
                webbrowser.open('google.com')
            elif "open facebook" in self.command:
                speak("opening facebook")
                webbrowser.open('facebook.com')
            elif "open hackerrank" in self.command:
                speak("opening hackerrank")
                webbrowser.open('hackerrank.com')
            else:
                speak("I don't know what that means asking GPT ")
                text=chatgpt_service(self.command)
                # cmds.change_text2(text)
                print(text)
                speak(text)

execution= jarvis_backend()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.text_1.setText(execution.tak_commands())
        self.ui.text_2.setText(chatgpt_service(execution.tak_commands()))
        execution.start()

    def start_exec(self):
        execution.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvis=Main()
    jarvis.show()
    sys.exit(app.exec_())

