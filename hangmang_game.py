import random

words = ["PYTHON","JAVA","PHP"]

images = ['''
   +---+
   |   |
       |
       |
       |
       |
  =========''',

'''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', 

'''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''',

'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', 

'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', 

'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', 

'''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  ========='''
  
]


#def difficulty():  
       

def run():
    #int(input("En que nivel quieres jugar?: "))
    print("En que dificultad quieres jugar?: ")
    print("Si quieres jugar en fácil ingresa 1")
    print("Si quieres jugar en intermedio ingresa 2")
    print("Si quieres jugar en dificil ingresa 3")
    ask_difficulty = int(input("Ingresa un número para elegir la dificultad: "))
    if ask_difficulty == 1:
        attemps = 12
    elif ask_difficulty == 2:
        attemps = 6
    elif ask_difficulty == 3:
        attemps = 3
    
    chosen_word = random.choice(words)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
    
    while True:
        print("Adivina la palabra!")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        else:
            
            attemps -= 1
        
        if "_" not in chosen_word_list_underscores:
            print("Ganaste la palabra era ", chosen_word)
            break


        if attemps == 0:
            print("Perdiste, la palabra era ", chosen_word)
            break



if __name__ == '__main__':
    print("COMIENZA EL JUEGO!!!")
    run()