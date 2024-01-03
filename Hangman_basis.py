import random
from hangman_art import logo
from hangman_words import word_list

# user_name = input("Hi, what is your name?")
print(logo)
print("Guess my word!")

chosen_word = list(random.choice(word_list))  # losowy wybór słowa z listy z pliku hangman_words
# print(chosen_word)
# poniżej wyświetlanie postępu uzupełniania słowa
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display.append("_")

print("".join(display))


# funkcja rysowania wisielca
def draw_hangman(frame):
    frame_1 = "__|______"
    frame_2 = """

  |    
  |    
  |   
  |   
__|______   
    """
    frame_3 = """
  _____
  |    
  |    
  |   
  |   
__|______
"""
    frame_4 = """
  _____
  |    |
  |    
  |   
  |   
__|______    
    """
    frame_5 = r"""
  _____
  |    |
  |    O
  |   
  |   
__|______
"""
    frame_6 = r"""
  _____
  |    |
  |    O
  |   /
  |   
__|______
"""
    frame_7 = r"""
  _____
  |    |
  |    O
  |   /|
  |   
__|______
"""
    frame_8 = r"""
  _____
  |    |
  |    O
  |   /|\
  |   
__|______
"""
    frame_9 = r"""
  _____
  |    |
  |    O
  |   /|\
  |   / 
__|______
"""
    frame_10 = r"""
  _____
  |    |
  |    O
  |   /|\
  |   / \
__|______
"""
    frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9, frame_10]
    print(frames[frame])


# ilość dostępnych żyć warunkowana ilością frames
lives = 10

while True:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter  # aktualizacja wyswietlanego słowa o odgadnięta litere
    print("".join(display))  # wyświetlanie obecnego stanu słowa

    if guess not in chosen_word:
        draw_hangman(10 - lives)  # rysowanie własciwego FRAME wisielca na podstawie liczby straconych żyć
        lives -= 1  # zmniejszanie ilości zyć, jeśli odgadnięta litera nie istnieje w danym słowie

        if lives == 0:
            print("You loose! The correct word was:", "".join(chosen_word))
            break
    if "_" not in display:
        print("You win!")
        break
