import random
import hangman_stages
word_list=['apple','banana','parrot','potato','pepper','samosa','tiger','tamarind',
           'mango','varshini','lecturer','career','curd','guava']
lives=6
chosen_word=random.choice(word_list)
display=[]
print("Welcome to Hangman Game🎊🎊🎊")
print("You have only 6 lives so try to guess the word in 6 attempts!Good Luck👍👍👍")
for i in range(len(chosen_word)):
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter:").lower()
    for pos in range(len(chosen_word)):
        letter=chosen_word[pos]
        if(letter==guessed_letter):
            print("You chosen a correct letter✅✅✅..")
            display[pos]=guessed_letter
    print(display)
    if(guessed_letter not in chosen_word):
        print("Ohh!!You chosen a wrong letter❎❎❎..")
        lives-=1
        if(lives==0):
            game_over=True
            print("Game over...You lose🤧🤧🤧")
    if '_' not in display:
        game_over=True
        print("Game over...You won🥳🥳🥳")
    print(hangman_stages.stages[lives])

