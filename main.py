import PyPDF2
import JarvisAI
import pywhatkit
import speech_recognition as sr
import pyttsx3
import wikipedia
import wikipedia
import random
import operator



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


try:
    with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print('Hi I am your Virtual Assistant Emma, How can i help you?')
            talk('Hi I am your Virtual Assistant Emma, How can i help you?')

            audio=listener.listen(source)
            print(':recognizing..')
            command=listener.recognize_google(audio)
            talk(command)
            print(command)
except:
        print('I am sorry, I could not understand the command')
        talk('I am sorry, I could not understand the command')




def run_emma():
    userinput = listener.recognize_google(audio)
    print('userinput')
    if 'who'  in userinput:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'yourself' in userinput:
        print('I am your virtual assistant Emma, I can be your friend')
        talk('I am your virtual assistant Emma, I can be your friend')
    elif 'name' in userinput:
        print('My name is emma, I am your friend and I am here to help you')
        talk('My name is emma, I am your friend and I am here to help you')
    elif 'play' in userinput:
        try:
            pywhatkit.playonyt(userinput)
            print('playing')
        except:
            print('network issue')
    elif 'read' in userinput:
        book = open('The_Adventures_of_Tom_Sawyer_-_Penguin_Readers-min.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        print(pages)
        for num in range(5, pages):
            page=pdfReader.getPage(5)
            text=page.extractText()
            print(text)
            talk(text)
    elif 'easy' in userinput:
        talk('Amazing!! Lets learn some maths in a fun way..')
        print('Amazing!! Lets learn some maths in a fun way..')
        talk("")
        talk('Lets learn addition ')
        print('Lets learn addition ')
        talk('There 10 green books and there are 5 blue books, how many books are there in all?')
        print('There 10 green books and there are 5 blue books, how many books are there in all?')
        talk('ahm..what do you think is the answer')
        print('..what do you think is the answer')
        print('we add 10 green books + 5 blue books, so start adding up to 5 numbers after 10...that is 11, 12, 13, 14, 15. ahaa so our answer is 15')
        talk('we add 10 green books + 5 blue books, so start adding up to 5 numbers after 10...that is 11, 12, 13, 14, 15. ahaa so our answer is 15')
        talk(' 10')
        print(' 10')
        talk('+  5')
        print('+ 5')
        print('________')
        print(' 15')
        talk(' 15')
        talk ('do you want to try an example?')
        print('do you want to try an example?')
    elif 'example' in userinput:

        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source, duration=1)



                voicecommand = listener.listen(source)
                print(':recognizing..')


        except:
            print('dint recognize')
            command1 = listener.recognize_google(voicecommand)
            talk(command1)
            print(command1)
            if 'yes' in command1:
                talk('okay.. thats great! Lets begin')
                print('There are 20 oranges in a basket and there 3 apples in another basket, how many fruits are there in all?')
                talk('There are 20 oranges in a basket and there 3 apples in another basket, how many fruits are there in all?')

    elif 'learn' in userinput:
        def random_problme():
            operators = {
                '+': operator.add,
                '-': operator.sub,
                '/': operator.truediv,
                '*': operator.mul,

            }

            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operation = random.choice(list(operators.keys()))
            answer = operators.get(operation)(num1, num2)
            print(f'What is {num1} {operation} {num2}?')
            if '/' in operation:
               expression = operation.replace('/','divided by')
               talk (f'What is {num1} {expression} {num2}?')
            elif '*' in operation:
                expression=operation.replace('*', 'multiplied by')
                talk(f'What is {num1} {expression} {num2}?')
            elif '-' in operation:
                expression = operation.replace('-', 'minus')
                talk(f'What is {num1} {expression} {num2}?')
            else:
                talk(f'What is {num1} {operation} {num2}?')

            return answer



        def ask_question():
            answer = random_problme()
            guess = float(input())
            return guess == answer

        def game():
            print('How well do u know math?')
            talk('How well do u know math?')
            talk('')
            talk('Lets play a math game')
            score = 0
            for i in range(5):
                if ask_question() == True:
                    score += 1
                    print('correct')
                    talk('correct')
                else:
                    print('oowww..that is a wrong answer')
                    talk('oowww..that is a wrong answer')

            print(f'Your score is {score} out of 5')
            talk(f'Your score is {score} out of 5')
            if score==3:
                print('Not bad dear, that is a fair score')
                talk('Not bad dear, that is a fair score')
            elif score==4:
                print('Amazing!! Well Played! you are an absolute math genius!!')
                talk('Amazing!! Well Played! you are an absolute math genius!!')
            elif score==5:
                print('Waaoooowwww !!! Mind blowing! you are absolute math genius!!')
                talk('Waaoooowwww !!! Mind blowing! you are absolute math genius!!')
            elif score==2:
                print('Not bad..better luck next time')
                talk('Not bad..better luck next time')
            elif score==1:
                print('Not bad..better luck next time')
                talk('Not bad..better luck next time')

        game()


run_emma()








