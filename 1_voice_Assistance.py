import speech_recognition as sr
import datetime
import subprocess
import pyttsx3
import pywhatkit
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
recognizer=sr.Recognizer()
def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises..... Please wait!")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print("Ask me anything....")
        recordedAudio=recognizer.listen(source)

        try:
            command=recognizer.recognize_google(recordedAudio,language="en-US")
        except Exception as ex:
            print(ex)
        else:

            if "Chrome" in command:
                a="Opening Chrome... Please Wait!"
                engine.say(a)
                engine.runAndWait()
                # program="C:/Program Files/Google/Chrome/Application/chrome.exe"
                program="C:\Program Files\Google\Chrome\Application\chrome.exe"
                subprocess.Popen(program)
            
            elif "time" in command:
                time=datetime.datetime.now().strftime("%I:%M %p")
                print(time)
                engine.say(time)
                engine.runAndWait()
            elif "play" in command:
                b="Opening Youtube...Please Wait!"
                engine.say(b)
                engine.runAndWait()
                pywhatkit.playonyt(command)
        

                

cmd()