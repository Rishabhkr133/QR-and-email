import speech_recognition as sr
import smtplib

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Clearing background noise")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("Waiting for your message")
    recordedAudio = recognizer.listen(source)
    print("Done recording")
    try:
        print("Printing the message")
        text = recognizer.recognize_google(recordedAudio,language='en-US')
        print(f"your message is :{text}")
    except Exception as e:
        print(e)

reciever = 'rishabhkr1991@gmail.com'
message = text
sender = 'rishabhkumar133@gmail.com'
subject = "Automated email testing"
password = 'kjdnsniojefioskeef'
server = smtplib.SMTP('smtp.gmail.com',587) 
server.starttls()
server.login(sender,password)
server.sendmail(sender,reciever,message)
