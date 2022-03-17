import random
import operator

def random_problme():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '/': operator.truediv,
        '*': operator.mul,


    }

    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num1, num2)
    print(f'What is {num1} {operation} {num2}?')
    return answer

def ask_question():
    answer = random_problme()
    guess = float(input())
    return guess == answer

def game():
    print('How well do u know math?/n')
    score=0
    for i in range(5):
        if ask_question() == True:
            score +=1
            print('correct')
        else:
            print ('Incorrect')

    print(f'Your score is {score} out of 5')

game()