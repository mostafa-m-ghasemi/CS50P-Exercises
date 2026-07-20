WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5 , "GRAPHIC": 7}

def main():
    print("Welcome to spelling Bee!")
    print("Your letters are : A I P C R H G")
    points = 0
    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")
        if guess == "GRAPHIC":
            WORDS.clear()
            print("YOU WON!")
            # .items
            for word, points in WORDS.items():
                print(f"{word}: {points}")
        elif guess in WORDS.keys():
            points += WORDS.pop(guess)
            print(f"Good job! You scored {points}! points.")


    print("That's the game")
