from words import get_random_word
from game import play_game
def main():
    word=get_random_word() 
    play_game(word)

if __name__ == "__main__":
    main()