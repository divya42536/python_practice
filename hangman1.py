
import random

word_list = ["aardvark","baboon", "camel"]
computer_choice = random.choice(word_list)
print(computer_choice)

#this line represents the empty spaces for a word
word_length = len(computer_choice)

place_holder = " "
for position in range(word_length):
    place_holder += "_"
print(place_holder)

game_over = False
correct_letters = []
while not game_over:
    guess = input( "are you ready with your guess? enter the first letter of the word:\n" ).lower()
    display =" "


    for letter in computer_choice:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_"not in display:
        game_over = True
        print("you win")


