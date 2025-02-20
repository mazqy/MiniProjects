import os
import json
import random

hint = ""
word = ""
running = True
hint_arr = []
attemps = 5

with open(file="words.json", mode="r") as dic:
    data = json.load(dic)
    word = data["words"][random.randint(0, len(data["words"]) - 1)]
    hint_arr = ["_" for _ in range(len(word))]
    hint = " ".join(hint_arr)

def check_word(p_input):
    global running, hint_arr, word, hint, attemps
    
    if len(p_input) == len(word):
        
        if p_input == word:
            print("\nYou got the word right!")
            running = False
        else:
            
            if attemps <= 0:
                print("\nYou wasted all your attemps. You lost :(")
                input(f"\nAwnser: {word}")
                running = False
            else:
                attemps -= 1
                for i in range(len(word)):
                    if word[i] == p_input[i]:
                        hint_arr[i] = word[i]
                hint = " ".join(hint_arr)
    else:
        input(f"\nThe word has to be {len(word)} letters long...")


while running:
    os.system("cls")
    print(f"-GUESS THE WORD-\n")
    print(f"Attemps: {attemps} | Word Lenght: {len(word)}")
    print(f"\nHint: {hint}")
    p_input = input("\n> ")
    check_word(p_input)
