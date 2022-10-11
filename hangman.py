import random

win_count = 0
loss_count = 0
print("H A N G M A N")


def menu():
    menu_sel = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit')
    if menu_sel == "play":
        main()
    elif menu_sel == "results":
        print(f"You won: {win_count} times.")
        print(f"You lost: {loss_count} times.")
        menu()
    elif menu_sel == "exit":
        exit(0)
    else:
        pass


def main():
    global win_count
    global loss_count
    words = ['python', 'java', 'swift', 'javascript']
    word = random.choice(words)
    counter = 8
    display = '-' * len(word)
    temp = list(display)
    already_guessed = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(str(display))
    while counter > 0:
        guess = input("Input a letter:  ")
        if guess in already_guessed:
            print("You've already guessed this letter.")
            already_guessed.append(guess)
            counter -= 1
            print(display)
            print()
            continue
        elif len(guess) > 1 or guess == "":
            print("Please, input a single letter.")
            print(display)
            print()
            continue
        elif guess not in alphabet:
            print("Please, enter a lowercase letter from the English alphabet.")
            print(display)
            print()
            continue
        elif guess not in word:
            print("That letter doesn't appear in the word.")
            already_guessed.append(guess)
            print(display)
            counter -= 1
            print()
            continue
        for i in range(len(word)):
            if guess == word[i]:
                temp[i] = guess
                already_guessed.append(guess)
                display = ''.join(temp)
        print(display)
        print()
        if display == word:
            print(f"You guessed the word {word}!\nYou survived!")
            win_count += 1
            menu()
    if counter == 0:
        print("You lost!")
        loss_count += 1
        menu()


menu()
