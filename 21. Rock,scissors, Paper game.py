import random

def getRandomNumber():
    randomNumber=random.randint(1,3)
    return randomNumber

def getCompChoice(randomNumber):

    if randomNumber==1:
        compChoice='rock'
    elif randomNumber==2:
        compChoice='paper'
    else:
        compChoice='scissors'
    return compChoice




def getUserChoice():
    userChoice=input('Enter your choice: ')
    return userChoice

def compare(compChoice,userChoice):


    rockmsg='rock smashes scissors'
    scissorsmsg='scissors cut paper'
    papermsg='paper wraps rock'
    winner='no winner'
    message=''

    if compChoice=='rock' and userChoice=='scissors':
        winner='the Computer won'
        message=rockmsg

    elif compChoice=='scissors' and userChoice=='rock':
        winner='You won'
        message=rockmsg

    if compChoice=='scissors' and userChoice=='paper':
        winner='the Computer won'
        message=scissorsmsg

    elif compChoice=='paper' and userChoice=='scissors':
        winner='You won'
        message=scissorsmsg

    if compChoice=='paper' and userChoice=='rock':
        winner='the Computer won'
        message=papermsg


    elif compChoice=='rock' and userChoice=='paper':
        winner='You won'
        message=papermsg

    return winner, message



def main():


    winner='no winner'

    while winner=='no winner':
        random_number=getRandomNumber()
        comp_choice=getCompChoice(random_number)
        user_choice=getUserChoice()
        print('The choice of the computer is',comp_choice)
        winner,message=compare(comp_choice,user_choice)


        if winner=='no winner':

            print(winner)
            print('You both chose the same thing. the game will start again..')


        if winner!='no winner':
            print(winner,',',message,sep='')


main()