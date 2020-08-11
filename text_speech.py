import pyttsx3
while True:
    sentence = input("Sentence : ")
    engine = pyttsx3.init()
    print("this program has been coded by EMİRKAN EŞME")
    engine.runAndWait()
    engine.say(sentence)
    engine.runAndWait()