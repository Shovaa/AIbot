import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak (audio):
  engine.say(audio)
  engine.runAndWait()

def wishMe():
  hour =int(datetime.datetime.now().hour)
  if hour>= 0 and hour<12:
      speak("Good morning")

  elif hour>=12 and hour<18:
      speak("Good afternoon")

  else:
      speak("Good Evening")


  speak("I am Shova. How can I help you")             
  
def takeCommand():
                r= sr.Recognizer()
                with sr.Microphone() as source:
                        print("Listening...")
                        r.adjust_for_ambient_noise(source, duration=1) 
                        audio = r.listen(source) 
                        
                try:
                        print("Recognize..")
                        query= r.recognize_google(audio)
                        print(f"User said:{query}\n")

                except Exception as e:
                        print("Say that again please..")
                        return "None"    

                return query

def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('adhikarisumitra@gmail.com','pokhara1234')
    server.sendmail('adhikarisumitra18@gmail',to,content)
    server.close()




if __name__=="__main__":

    wishMe()
    #while True:
    if 1:
        query =takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open google' in query:
            webbrowser.open("google.com")    


        elif 'play music' in query:
            music_dir='D:\\NOn criical\\favourite song'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))   



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Madam, th time is{strTime}") 
            print(strTime)

        elif 'send emali to' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="shovakuikel1@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")

            except Exception as e:
                                    print(e)
                                    speak("sorry my frined")