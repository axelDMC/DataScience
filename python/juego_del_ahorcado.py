from gc import collect
import os
import random
import collections

def randomWord():
    with open("./archivos/data.txt", "r", encoding="utf-8") as file:     
        allText = file.read()   
        words = list(map(str,allText.split()))
        return random.choice(words)    

def compareList(l1, l2):
    if(collections.Counter(l1) == collections.Counter(l2)):
        return True
    else:
        return False

def clear():
    os.system('clear')

def run():
    word = randomWord()
    wordList = list(word)
    guessWord = ['_' for element in word]    
    letter = ""
    while(True):
        clear()              
        print('¡Adivina la palabra!')
        for index, c in enumerate(word):
            if(word[index] == letter):
                guessWord[index] = c
                #print("data is", word)
                print(letter, end = " ")
            elif guessWord[index] == int():
                print(guessWord[index], end=" ")
            else :
                print(guessWord[index], end=" ") 
        print('\n')
        if(compareList(wordList, guessWord) == True):
            break
        letter = input('Ingresa una letra: ')

    clear()
    print("¡Ganaste! La palabra era" , ''.join(wordList).upper())
    print('\n')

if __name__ == '__main__':
    run()
    