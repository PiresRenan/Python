#import os
#path = "C:\\Users\\TI\\PycharmProjects\\TestePasta"
#if os.path.exists(path):
    #print("That location exists!")
    #if os.path.isfile(path):
        #print("That is the file")
    #elif os.path.isdir(path):
        #print("That is a directory!")
#else:
    #print("That location doesn't exist!")

#try:
    #with open('C:\\Users\\TI\\PycharmProjects\\basicPython4\\test.txt') as file:
        #print(file.read())
#print(file.closed)
#except FileNotFoundError:
    #print("That file was not found ")

#text =  "Yoooooooo\nThis is some text\nHave a good one!\n"
#text =  "HAVE A GOOD DAY, SIR!"
#with open('test2.txt','w') as file:
    #file.write(text)
#with open('test2.txt','a') as file:
    #file.write(text)

#import shutil
#shutil.copyfile('test.txt','copy.txt') #source to destination#copies contents of a file
#shutil.copyfile('test.txt','C:\\Users\\TI\\Desktop\\copy2.txt')
#shutil.copy('test.txt','C:\\Users\\TI\\Desktop\\copy2.txt')#copyfile() + permission mode + destination can be a directory.
#shutil.copy2('test.txt','C:\\Users\\TI\\Desktop\\copy2.txt')#copy() + copies metadata(file's creation and modification times)

#import os
#source = "test3.txt"
#destination = "C:\\Users\\TI\\Desktop\\Testes"
#try:
    #if os.path.exists(destination):
        #print("There is already a file there")
    #else:
        #os.replace(source,destination)
        #print(source + " was moved")
#except FileNotFoundError:
    #print(source + " was not found")

#import os
#import shutil
#os.remove('test4.txt')#or by path:"C:\\Users\\TI\\PycharmProjects\\basicPython4\\test4.txt" or path way
#path = 'C:\\Users\\TI\\PycharmProjects\\basicPython4\\test4.txt'
#os.remove(path)
#path = 'Empty_folder'
#try:
    #os.remove(path)
    #os.rmdir('Empty_folder')
    #os.rmdir('Folder')
    #shutil.rmtree('Folder')
#except FileNotFoundError:
    #print("That file was not found!")
#except PermissionError:
    #print("You do not have permission to delete that!")#for that use os.rmdir(path)
#except OSError:
    #print("You cannot delete that using that function")#for that use shutil.rmtree(path)
#else:
    #print(path+" was deleted!")#just import os > os.remove(path)

#import TestPythonFile#Modular construction
#import TestPythonFile as msg
#msg.hello()
#msg.bye()
#from TestPythonFile import hello,bye #or '*' for all content in modular file
#hello()
#bye()
#help('modules')#for helpfull commands(can access docs.python.org/3/py-modindex.html for full modules)

#import random
#while True:
    #choices = ['rock', 'paper', 'scissors']
    #computer = random.choice(choices)
    #player = None
    #while player not in choices:
        #player = input("Rock, Paper or Scissors? ").lower()
    #if player == computer:
        #print("Computer: ", computer)
        #print("Player: ",player)
        #print("Tie!")
    #elif player == "rock":
        #if computer == "paper":
            #print("Computer: ", computer)
            #print("Player: ", player)
            #print("You lose!")
        #if computer == "scissors":
            #print("Computer: ", computer)
            #print("Player: ", player)
            #print("You win!")
    #elif player == "scissors":
        #if computer == "paper":
            #print("Computer: ", computer)
            #print("Player: ", player)
            #print("You lose!")
        #if computer == "rock":
            #print("Computer: ", computer)
            #print("Player: ", player)
            #print("You win!")
    #elif player == "paper":
        #if computer == "scissors":
            #print("Computer: ", computer)
            #print("Player: ", player)
            #print("You lose!")
        #if computer == "rock":
            #print("Computer: ", computer)
            #print("Player: ", player)
            #print("You win!")
    #play_again = input("Play again? (Yes/No) ").lower()
    #if play_again != "yes":
        #break
#print("Bye!")

#def new_game():
    #guesses = []
    #correct_guesses = 0
    #question_num = 1
    #for key in questions:
        #print("------------------------")
        #print(key)
        #for i in options[question_num - 1]:
            #print(i)
        #guess = input("Enter (A, B, C or D): ")
        #guess = guess.upper()
        #guesses.append(guess)
        #correct_guesses += check_answer(questions.get(key), guess)
        #question_num += 1
    #display_score(correct_guesses, guesses)
#def check_answer(answer, guess):
    #if answer == guess:
        #print("CORRECT!")
        #return 1
    #else:
        #print("WRONG!")
        #return 0
#def display_score(correct_guesses, guesses):
    #print("--------------------")
    #print("RESULTS")
    #print("--------------------")
    #print("Answers: ", end="")
    #for i in questions:
        #print(questions.get(i), end=" ")
    #print()
    #print("Guesses: ", end="")
    #for i in guesses:
        #print(i, end=" ")
    #print()
    #score = ((correct_guesses / len(questions))*100)
    #print("Your score is: "+str(score) + "%")
#def play_again():
    #response = input("Do you want play again?(Yes or No) ")
    #response = response.upper()
    #if response == "YES":
        #return True
    #else:
        #return False
#questions = {
    #"Who created Python? ": "A",
    #"What year was Python created? ": "B",
    #"Python is tributed to which comedy group? ": "C",
    #"Is the Earth round? ": "A"
#}
#options = [[
    #"A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    #["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    #["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    #["A. True", "B.False", "C. Sometimes", "D. What's Earth?"
#]]
#new_game()
#while play_again():
    #new_game()
#print("Byeeee!")
