import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
import wolframalpha

try:
    app = wolframalpha.Client("JWPUVQ-YGKUHH3XYV")
except Exception:
    print("some features are not work")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak(" my name is jarvis sir . Please tell me how may i help you")


def takeCommand():
    # it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sumritchauhan9011@gmail.com', 'bhai sumrit manja')
    server.sendmail('sumritchauhan9011@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

     # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia  sir ....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('youtube is opening sir')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Google is opening sir')
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak('stackoverflow is opening sir')
            webbrowser.open("stackoverflow.com")

        elif 'open wynk music' in query:
            speak('wynk music is opening sir')
            webbrowser.open("https://wynk.in/music/package/trending-in-hindi")

        elif 'the time' in query or 'what time is it' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")

        elif 'who is your owner ' in query:
            speak('I am created by Sumrit Chauhan, He is my owner , i respect him')

        elif 'open code' in query:
            codepath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)

        elif 'about yourself' in query:
            speak(
                'I am jarvis , i am a personal assistant for your help , and created by sumrit chauhan ')

        elif 'sumrit chauhan' in query:
            speak('sumit chauhan is my owner and he is a student now , he pursuing his B. Tech from guru gobind singh indraprasth university')

        elif ' about mohit tiwari' in query:
            speak("Mohit Tiwari is my owner's friend and he is studying with my owner, he pursuing his B. Tech from guru gobind singh indraprasth university")

        elif ' about suraj tripathi' in query:
            speak("suraj tripathi is my owner's friend and he is studying with my owner, he pursuing his B. Tech from guru gobind singh indraprasth university")

        elif 'meaning of your name' in query:
            speak("Just A Rather Very Intelligent System")

        elif ' email to shaurya bisht' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "bshaurya73@gmail.com"
                sendEmail(to, content)
                speak("email has been sent sucessfully!")
            except Exception as e:
                speak("sorry sir! . I am not able to send this email")

        elif ' email to mohit tiwari' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "mohitiwari2002@gmail.com"
                sendEmail(to, content)
                speak("email has been sent sucessfully!")
            except Exception as e:
                speak("sorry sir! . I am not able to send this email")

        elif 'thank you jarvis' in query:
            speak("no problem sir , always here for your help")

        elif 'how are you' in query:
            speak("I am fine sir. what can i do for you?")

        elif 'what is your name' in query:
            speak("Name : Jarvis . occupation : Helping you . age : old enough to use me")

        elif 'can i change your name' in query:
            speak("sorry, I can't change my name")

        elif 'what can you do' in query:
            speak("i am not enough intelligent ,but i will try my best for help you")

        elif 'good morning' in query:
            speak("good morning sir , how can i help you")

        elif 'good afternoon' in query:
            speak("good afternoon sir , how can i help you")

        elif 'good evening' in query:
            speak("good evening sir , how can i help you")

        elif 'will you make my friend' in query:
            speak(
                "of course , now you and me are friends  ,  ok my friend what can i do for you")

        elif 'who is your best friend' in query:
            speak("i feel a strong connection to the wi-fi , so wifi is my best friend")

        elif 'male or female' in query or 'you are male' in query or 'you are female' in query:
            speak("i don't have a gender ,sir !")

        elif "why don't you have a gender" in query:
            speak("well , mainly because i am software, not a person")

        elif 'do you want to be human' in query:
            speak("i like being me. as mark twain once said,'The worst loneliness is to not be comfortable with yourself'.")

        elif 'you have emotions' in query:
            speak(
                "i have lots of emotions, i feel excited when i learn somethimg new and help you")

        elif 'are you a robot' in query:
            speak("i did prefer to think of myself as your friend . who also happens to be artificially intelligent")

        elif 'who is your father' in query:
            speak("I have no father SIR, I have been made . By SUMRIT CHAUHAN")

        elif 'your birthday' in query:
            speak("I love my creator so much, that's why I consider his birthday date as my birthday date which is twenty four september two thousand three")

        elif 'are you alone' in query:
            speak("I'm not alone because i have you sir")

        elif 'your strength' in query:
            speak(" I'm pretty good at talking")

        elif 'are you single' in query:
            speak("I am in a relationship with wifi")

        elif 'help me' in query:
            speak("I'm always here for your help sir, tell me your problem.")

        elif 'i am sad' in query:
            speak("if i could ,i would make you a lovely cup  of tea to help you feel better")

        elif 'kill you' in query:
            speak(" hey  i  am  not  a  human , i  am  a  software program  , so  you  don't  kill  me    ha    ha    ha")

        elif 'on youtube' in query:
            song = query.replace('on youtube', '')
            speak("playing" + song)
            pywhatkit.playonyt(song)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'on google' in query:
            search = query.replace('on google', '')
            speak("searching" + search)
            pywhatkit.search(search)

        elif 'handwriting' in query:
            text = query.replace('handwriting', '.')
            speak("converting into handwritten")
            pywhatkit.text_to_handwriting(text,
                                          save_to="pythontext.png",
                                          rgb=[0, 0, 255])

        elif 'temperature' in query:
            try:
                res = app.query(query) 
                print(next(res.results).text)      
                speak(next(res.results).text)   

            except:
                print("internet connection error")         

        else:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)    

            except:
                speak("sir , internet is not working , please check internet or try again")
                
                                           



