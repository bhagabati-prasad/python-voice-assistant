import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



emails = {
    "admin": "bhagabatiprasada@gmail.com",
    "Ashish": "ashis3d@gmail.com",
    "Chintu": "northgtaworld@gmail.com"
}


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("Jarvis at your service, How can I help you?")

def takeCommand():
    # It takes micophone input from user and return string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e) # Comment this out. Only for debugging purpose
        speak("I did not get it sir, Please say again.")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sendmailfrom80@gmail.com", "popsot123")
    server.sendmail("sendmailfrom80@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # while False:
    while True:
        query = takeCommand().lower()
        # Executing tasks
        if 'wikipedia' in query:
            speak('Searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'search' in query:
            from selenium import webdriver
            speak("What do You want to search?")
            # Take input from user
            search_string = takeCommand()
            # converts string to URL format
            search_string = search_string.replace(' ', '+')
            # Select Chrome browserfor searching
            browser = webdriver.Chrome('chromedriver')
            speaking("Searching, hold on.")
            # Search query on google
            for i in range(1):
                matched_elements = browser.get("https://www.google.com/search?q="+search_string+"&start="+str(i))

        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\asus\\Desktop\\UCDownloads'
            songs = os.listdir(music_dir)
            speak("May I take rest?")
            musconf = takeCommand()
            if "ok" in musconf:
                speak("Thank you sir, playing music.")
                os.startfile(os.path.join(music_dir, songs[3]))
                quit()
            else:
                speak("Ok playing, Say what will I do.")
                os.startfile(os.path.join(music_dir, songs[0]))
                continue

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {time}")

        elif 'code editor' in query:
            editorPath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            speak("Opening sir.")
            os.startfile(editorPath)

        elif 'email' in query:
            try:
                speak("To whom?")
                name = takeCommand()
                to = emails[name]
                speak("What will I say?")
                content = takeCommand()
                # sendEmail(to, content)
                # speak("Email has been sent!")
                speak("Confirm, yes or no?")
                mailconf = takeCommand()
                flag = 0
                while flag != 1:
                    if "yes" in mailconf:
                        sendEmail(to, content)
                        speak("Email has been sent!")
                        flag = 1
                    elif "no" in mailconf:
                        speak("Cancelled sending email, say how may I help you.")
                        break
                    else:
                        speak("Unable to confirm, plese say again.")
                        break
            except Exception as e:
                # print(e)
                speak("Sorry, could not send message.")

        elif 'open command' in query:
            cmdPath ="%windir%\\system32\\cmd.exe" # Error in file path
            speak("Opening sir.")
            os.startfile(cmdPath)

        elif 'quit' in query:
            speak("Ok, quiting.")
            quit()
