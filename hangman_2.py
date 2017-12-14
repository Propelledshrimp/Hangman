#Hangman

#Tatem P.

import os
import random 

def splash_screen():
    with open('art/splash_screen.txt', 'r') as f:
            lines = f.read()

    print(lines)
 
def show_credits():
    print("This game was made by : ")

    with open('art/credits.txt', 'r') as f:
            lines = f.read()

    print(lines)
    
def get_puzzle():
    path = 'puzzles'
    file_names = os.listdir(path)
    for i, f in enumerate(file_names):
        with open(path + '/' +file_names[i], 'r') as f:
            catagory = f.read().splitlines()
        print(str(i + 1) + ")" + str(catagory[0]))
 

    choice = input("pick one ")
    choice = int(choice) - 1

    file = path + "/" +file_names[choice]

    with open(file, 'r') as f:
        lines = f.read().splitlines()

    catagory_name = lines[0]
    puzzle = random.choice(lines[1:])
    puzzle = puzzle.lower()
    puzzle = puzzle.strip() 
    print(catagory_name)

    return (puzzle) 
  
def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved
    
def get_guess():
    while True:
        letter = input("Guess a letter: ")
        letter = letter.lower() 
        if letter.isalpha():
           return letter
        else:
            print("Please guess a letter")
            

def display_board(solved, strikes): 
    print(solved)
    if strikes == -1:
        with open('art/apple.txt', 'r') as f:
            lines = f.read()

        print(lines)
      
        print("Protect your food from the ants!")
        strikes += 1
       
    elif strikes == 1:
        with open('art/strike_1.txt', 'r') as f:
            lines = f.read()

        print(lines)
    

    elif strikes == 2:
        with open('art/strike_2.txt', 'r') as f:
            lines = f.read()

        print(lines)


    elif strikes == 3:
        with open('art/strike_3.txt', 'r') as f:
            lines = f.read()

        print(lines)


    elif strikes == 4:
        with open('art/strike_4.txt', 'r') as f:
            lines = f.read()

        print(lines)


    elif strikes == 5:
        with open('art/strike_5.txt', 'r') as f:
            lines = f.read()

        print(lines)
        

def show_result(solved, puzzle, strikes, limit): 
    if solved == puzzle:
        print("You win!")
    elif strikes >= limit:
           print("The ants got your food!")
           
           with open('art/apple_thief.txt', 'r') as f:
            lines = f.read()

            print(lines)
        
            print("Too bad, it was good food!")
           
           
   
def play():
    puzzle = get_puzzle()
    guesses = ""
    strikes = -1
    limit = 6
    solved = get_solved(puzzle, guesses)
    display_board(solved,strikes)

    print(solved) 

    while solved != puzzle and strikes < limit:
        letter = get_guess()

        if letter not in puzzle:
            strikes += 1


        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved,strikes)
        show_result(solved, puzzle, strikes, limit)
        
        
def play_again():
    while True: 
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()
        decision = decision.strip() 
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
    


splash_screen()

playing = True

while playing:
    play() 
    playing = play_again()


show_credits() 
    

