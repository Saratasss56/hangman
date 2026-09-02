def create_display(word,guessed):
    display=""
    for letter in word:
        if letter in guessed:
            display+=letter+" "
        else:
            display+="_"
    return display