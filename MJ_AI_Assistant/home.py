import webbrowser as br
import pyttsx3
import speech_recognition as sr
from AI_assistant import assistent as ai
new_ai=ai()

Recognizer = sr.Recognizer()


'''voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)'''
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
def commandprocessing(command2):
    if command2.lower()=="open google":
        br.open("https://www.google.com/")
    elif command2.lower()=="open youtube":
        br.open("https://www.youtube.com/")
    elif command2.lower()=="open chatgpt":
        br.open("https://chatgpt.com/")
    else :
         speak(new_ai.work(command2))

    

if __name__=="__main__":
   speak("starting RJ...")
   speak("hey, how may i help you sir")
   
   while True:
        with sr.Microphone() as source:
                print("Speak something...")
                audio = Recognizer.listen(source)

        try:
                command = Recognizer.recognize_google(audio)
                if ("rj" in command.lower()):
                    speak("i am listening")
                    with sr.Microphone() as source:
                        print("RJ activating...")
                        audio = Recognizer.listen(source)
                    try:
                        command2 = Recognizer.recognize_google(audio)
                        commandprocessing(command2)
                        break
                    except:
                        print("error")
                        speak("Sorry, I could not understand the commond")
                    

                    
                print("You said:", command)
        except:
                print("error")
                speak("Sorry, I could not understand")
                