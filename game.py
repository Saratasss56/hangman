from hangman import hangman
from display import create_display

def play_game(word):
    guessed=[]
    wrong_guess=0
    max_attempts=5

    while max_attempts>wrong_guess:
        display=create_display(word,guessed)

        print(hangman[wrong_guess])
        print("Word: ",display)

        if "_" not in display:
                    print("congrats, you won")
                    print("Word was ",word)
                    break

        guess=input("Enter your guess: ").lower()

        if len(guess)!=1 or not guess.isalpha():
                    print("Please enter one letter only")
                    continue
        
        if guess in guessed:
                    print("You already guessed that letter")
                    continue

       
        

        if guess in word:
                    print("Correct guess!")
        else:
                    wrong_guess += 1
                    print("Wrong guess!")
        

       

        guessed.append(guess)

        
        
        
    else:
        print("You lost")
        print("Word was ",word)    







