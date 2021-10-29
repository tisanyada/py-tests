#inport the packages
import pyttsx3
engine = pyttsx3.init()
#ask for the text
engine.say(input('> Enter the text you want in speech here: '))
engine.runAndWait()
