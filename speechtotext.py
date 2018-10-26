import speech_recognition as sr 
import sys
r = sr.Recognizer()                                                                                   
filename=sys.argv[1]
alltext=""

with sr.AudioFile(filename) as source:                                                                       
    #print("Speak:")                                                                                   
    audio = r.listen(source)   

try:
    print("::" + r.recognize_google(audio))
    text=r.recognize_google(audio)
    alltext=alltext+text

#except sr.UnknownValueError:
#    print("Could not understand audio")
#except sr.RequestError as e:
#    print("Could not request results; {0}".format(e))
except Exception:
	print("something went wrong")
# run it like python filename.py audiofilename.wav
with open("himani.txt", "w") as f:
    f.write(alltext)