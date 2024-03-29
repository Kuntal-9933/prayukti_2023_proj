import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
import psutil
import pyautogui
from wikipedia.wikipedia import page
import openai
from langdetect import detect



openai.api_key='api-key'

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
    global r
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
    print(f"{text}")
    speak(f"{text}")

def filter_command(command):
    if "Jarvis" in command:
        command=command.replace("Jarvis","")
        return command
    else:
        return command

def tak_commands():
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
        command=filter_command(command_unf)
        print(f"User asked for  {command}")
        return command
    except Exception as e:
        speak("Say That Again Please..")
        command = tak_commands()
        return command
    
    
def read_pdf():
    # import pyPDF2
    '''book=open("E:\electronics notes\Mesh analysis .pdf",'rb')
    # pdfReader=pyPDF2.pdffileReader(book)
    #pdfReader=PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages
    speak(f"total number of pages in the pdf is {pages}")
    speak("please the enter the number,  of page you want to read")
    no=int(input("enter the page number here:"))
    page=pdfReader.getPage(no)
    text=page.extractText()
    speak(text)
    print(text)'''
    pass


def send_email(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo
    server.starttls
    server.login('''kuntalmukherjee702@gmail.com','password''')
    server.sendmail('kuntalmukherjee702@gmail.com',to,content)
    server.close()


if __name__=='__main__':
    wish()
    a = True
    while a:
        command=tak_commands()

        if "introduce"in command:
            speak("Sir , I am Jarvis 2.0 at your service, a intelligent python program programmed by Kuntal Mukherjee")
            speak(" how can I help you sir?")
        elif " volume up" in command:
            pyautogui.press("volumeup")
        elif "volume down" in command:
            pyautogui.press("volumedown")
        elif " volume mute" in command:
            pyautogui.press("volumemute")
           
        elif "battery percentage" in command:
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
        elif "sleep" in command:
            speak("Going to sleep sir")
            a = invoke()
        elif "time" in command:
            time_Now=datetime.datetime.now().strftime('%H hour:%M minute:%S second')
            speak(f"Sir ,  the time is {time_Now}")
                
        elif "weather report" in command:
            search="temparature in kolkata"
            url=f"https://www.google.com/search?q={search}"
            m=requests.get(url)
            data=BeautifulSoup(m.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            print(f'current {search} is {temp}')
            speak(f'current {search} is {temp}')

        elif 'send email' in command:
            try:
                speak("what I will tell?")
                content=tak_commands()
                to="kuntalmukherjee834@gmail.com"
                send_email(to,content)
                speak("Email has been sent")
            except Exception as e:
                speak("sorry , email has not been sent")
        elif 'wikipedia' in command:
            speak("searching Wikipedia, wait for a while sir")
            command=command.replace('wikipedia','')
            results=wikipedia.summary(command,sentences=1)
            speak("According to google")
            speak(results)
            print(results)
        elif "play intro" in command:
            music_dir="C:\\Users\\KUNTAL MUKHERJEE\\Music"
            songs=os.listdir(music_dir)
            print(songs)
            speak("playing favourite song of Tony stark")
            os.startfile(os.path.join(music_dir,songs[2]))
        elif "open code" in command:
            code_way="C:\\Users\\KUNTAL MUKHERJEE\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening visual studio code")
            os.startfile(code_way)
            # break
        elif "read pdf" in command:
            read_pdf()
            break
        elif "open youtube" in command:
            speak("opening youtube")
            webbrowser.open('youtube.com')
        elif "open google" in command:
            speak("opening google for you sir , in a minute")
            webbrowser.open('google.com')
        elif "open facebook" in command:
            speak("opening facebook")
            webbrowser.open('facebook.com')
        elif "open hackerrank" in command:
            speak("opening hackerrank")
            webbrowser.open('hackerrank.com')
        elif 'quit' in command:
            speak("Good Bye Sir, hope we will meet again soon!")
            print("program terminates")
            break
        else:
            speak("I don't know what that means asking GPT ")
            chatgpt_service(command)
