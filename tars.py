import pyttsx3
import datetime
import speech_recognition
import wikipedia
import webbrowser
import os
import smtplib
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices)
# print(voices[0])
# print(voices[0].id)
# print(voices[1])
# print(voices[1].id)

engine.setProperty('voice', voices[0].id)

email_ids = {"person1" : "person1-email-id", "person2": "person2-email-id", "person3": "person3-email-id"}

def speak(audio):
    print(f"TARS: {audio}")
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I'm TARS. Please tell me how may I help you")
    
def takeCommand():
    # it takes microphone input from the user and returns string output
    r = speech_recognition.Recognizer();
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
    except Exception as e:
        # print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('your-email-id', 'your-password') 
    # server.login('xyz@gmail.com', 'xyz*123')
    # provide access to 'less secure apps' in your google account for successful login 
    # (which is unsecure. So for demo purpose you can create a dummy account.)
    server.sendmail('your-email-id', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        # Logic for executing tasks based on query
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            speak(results)

        elif 'who are you' in query:
            speak("I am TARS! Mr Cooper has sent me to assist you!")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'dir-path'
            songs = os.listdir(music_dir)
            # print(songs)
            no_of_songs = len(songs)
            random_song = random.randint(0, no_of_songs-1)
            os.startfile(os.path.join(music_dir, songs[random_song]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Hey Sabiha, The time is {strTime}")
            
        elif 'open codechef' in query:
            webbrowser.open("codechef.com")
            
        elif 'open codeforces' in query:
            webbrowser.open("codeforces.com")
            
        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")
            
        elif 'open github' in query:
            webbrowser.open("github.com")
        
        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\sabiha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand() 
                to = email_ids[query.split()[-1].lower()] 
                # query = "Send email to papa"
                # to = email_ids[papa]   
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sabiha. I'm not able to send this email")
                

        
    


