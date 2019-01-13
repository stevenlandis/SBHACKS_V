import pip
import smtplib
import speech_recognition as sr
import ssl
Sender = 'gareyflee@gmail.com'
Recipient = 'gareyflee@gmail.com'
pw = "Dew61316131"
def Speech_To_Email():

    # for index, name in enumerate(sr.Microphone.list_microphone_names()):
    #     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    mic = sr.Microphone()
    r = sr.Recognizer()
    with mic as source:

        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio = r.listen(source)
        voiceHold = r.recognize_google(audio)
    print(voiceHold)

    server = smtplib.SMTP('smtp.gmail.com', 587) ## 25 465 587
    server.starttls()
    server.login(Sender, pw)

    msg = voiceHold + "\n\nSent from Hackathon"
    server.sendmail(Sender, Recipient, msg)
    server.quit()
