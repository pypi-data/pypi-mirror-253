def main():
    import speech_recognition as sr

    with open('fraud_patterns.txt','r') as f:
        for line in f:
            patterns = f.read().split('\n')
            patterns = [i.split(',') for i in patterns]

    with open('social_prestige.txt','r') as p:
        for line in p:
            keywords = p.read().split('\n')
            keywords = [j.split(',') for j in keywords]

    def recognize_speech():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Speak now ...")
            audio = r.listen(source,timeout=8,phrase_time_limit=8)

        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
        

    def check_sequence(lst, given_str):
        index = -1
        for elem in lst:
            index = given_str.lower().find(elem.lower(), index + 1)
            if index == -1:
                return False
        return True

    def checkPat(inp:str):
        for i in patterns:
            if check_sequence(i,inp):
                return True
        return False

    def checkKey(inp:str):
        for j in keywords:
            if check_sequence(j,inp):
                return True
        return False

    speech = recognize_speech()
    if not speech == None:
        print('Speech:',speech)
        if checkPat(speech):
            print('This may be a fraudulent speech!')
        elif checkKey(speech):
            print('This may be a hate speech!')
        else:
            print('No threat detected!')


if __name__ == '__main__':
    main()