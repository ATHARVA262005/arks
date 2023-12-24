import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import webbrowser




listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')


voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def talk(text):
        engine.say(text)
        engine.runAndWait()

talk('hello boss')

def take_command():
    try:
        with sr.Microphone() as source:
            print('lisening...')
            voice = listener.listen(source)
            command= listener.recognize_google(voice)
            command = command.lower()

            if 'arks' in command:
                command = command.replace('arks','')
                print(command)

    except:
        pass
    return command

def run_arks():
    command = take_command()
    print(command)
    
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+song)
        print('playing'+song)
        pywhatkit.playonyt(song)
    
    elif 'hello' in command:
           talk('Hello Sir how can i help you today')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ',time)

    elif 'who' in command:
        person = command.replace('who','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)

    elif 'i love you' in command:
           talk('sorry i am in relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
    elif 'search' in command:
         query=command.replace('search','')
         url=f"https://www.google.com/search?q={query}"
         webbrowser.open_new_tab(url)


    else:
        talk('Please say the command again.')


while True:
    run_arks()