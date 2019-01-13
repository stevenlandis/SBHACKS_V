import pip
import smtplib
def Speech_Recognition():

    if hasattr(pip, 'main'):
        pip.main(['install', 'SpeechRecognition'])
    else:
        pip._internal.main(['install', 'SpeechRecognition'])


    import speech_recognition as sr

    for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))



    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


        # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        voiceHold = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + voiceHold
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))



    from email.mime.text import MIMEText
    with open(textfile) as fp:
        msg = MIMEText(fp.read())
    msg['Subject'] = "Amazing Demonstration"
    msg['From'] = gareyflee@gamil.com
    msg['To'] = knguyen104@ucsb.edu

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
