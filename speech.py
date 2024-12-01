#(please ensure the file name should "text_speech_converter.py" as per README.md file instruction)
#text to speech converter
import pyttsx3
engine = pyttsx3.init()
answer = input("what you want to convert into speech:")
engine.setProperty("rate", 150)
engine.say(answer)
engine.runAndWait()

#speech to text converter
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("speak anything")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("you said : {}".format(text))
    except:
        print("sorry could not recognize your voice")
    

