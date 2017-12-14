#Hangman

#Tatem P.


def splash_screen():
    print(" _   _    ")                                     
    print("| | | |   ")                                      
    print("| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  ") 
    print("|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ") 
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                    __/ |                      ")
    print("                   |___/ ")

def show_credits():
    print("This game was made by : ")
    print("_____   __   _____  ____  _       ")        
    print(" | |   / /\   | |  | |_  | |\/|  ")   
    print(" |_|  /_/--\  |_|  |_|__ |_|  |   ")
    print(" _   _   ___   _    __   ___   _  ____ ") 
    print("/ | / | |___| / |  / /  |___| / |  / / ")
    print("|_| |_|       |_| (_)_)       |_| /_/ ") 
    
def get_puzzle():
    return ("memes") 
  
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
       print("         ,--./,-. ") 
       print("        / #      \\" )
       print("       |          | ") 
       print("        \        /   ")  
       print("         `._,._,'  ")
       print("Protect your food from the ants!")
       strikes += 1
       
    elif strikes == 1:
        print("         \__ ") 
        print("         (o )     ___ ") 
        print("         <>(_)(_)(___)") 
        print("           < < > >    ") 
        print("           ' ' ` `     ")

    elif strikes == 2: 
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")

    elif strikes == 3:
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")

    elif strikes == 4:
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")

    elif strikes == 5:
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ")
       print("         \__ ") 
       print("         (o )     ___ ") 
       print("         <>(_)(_)(___)") 
       print("           < < > >    ") 
       print("           ' ' ` `     ") 

def show_result(solved, puzzle, strikes, limit): 
    if solved == puzzle:
        print("You win!")
    elif strikes >= limit:
           print("The ants got your food!")
           print("         ,--./,-. ") 
           print("        / #      \\" )
           print("       |          | ") 
           print("        \        /   ")  
           print("         `._,._,'  ") 
           print("         \__ ") 
           print("         (o )     ___ ") 
           print("         <>(_)(_)(___)") 
           print("           < < > >    ") 
           print("           ' ' ` `     ") 
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
    

