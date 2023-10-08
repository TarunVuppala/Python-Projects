import random

word_list = [
    "Elephant", "Computer", "Chocolate", "Butterfly", "Telephone",
    "Universe", "Adventure", "Guitar", "Ecosystem", "Symphony",
    "Kangaroo", "Rainbow", "Mountain", "Enchantment", "Diamond",
    "Astronomy", "Flamenco", "Pineapple", "Treasure", "Paradox",
    "Serenade", "Octopus", "Cinnamon", "Nebula", "Serenity",
    "Exquisite", "Zephyr", "Serendipity", "Avalanche", "Moonlight",
    "Vibrant", "Alligator", "Wonderland", "Aquamarine", "Mesmerize",
    "Incandescent", "Labyrinth", "Phenomenon", "Firefly", "Intrigue",
    "Volcano", "Whimsical", "Zucchini", "Serotonin", "Jigsaw",
    "Marathon", "Quicksilver", "Luminous", "Chrysalis", "Whisper",
    "Apple", "Banana", "Chair", "Dog", "Elephant",
    "Fish", "Guitar", "House", "Ice", "Jump",
    "Kite", "Laptop", "Mountain", "Nest", "Orange",
    "Piano", "Quiet", "River", "Sun", "Tree",
    "Umbrella", "Violin", "Water", "Xylophone", "Yellow",
    "Zebra", "Bicycle", "Carrot", "Dance", "Eagle",
    "Flower", "Globe", "Horse", "Island", "Jacket",
    "Kangaroo", "Lion", "Monkey", "Ninja", "Ocean",
    "Pizza", "Queen", "Rain", "Star", "Train",
    "Unicorn", "Volcano", "Window", "X-ray", "Yoga",
    "Zoo"
]

def assign_word():
    random.shuffle(word_list)
    word = random.choice(word_list).lower()

    letter_list = []
    for letter in word:
        letter_list.append(letter)

    random.shuffle(letter_list)
    print(letter_list)
    return word


word = assign_word()
tries=6
user_guess = input(f"\nTries left {tries+1} Your Guess: ").lower()

while tries>0:
    if user_guess==word:
        print("You Guessed it right!\nAnother challenge coming up...\n")
        word = assign_word()
        tries=6
    else:
        tries-=1
        user_guess = input(f"Tries left {tries+1} Your Guess: ").lower()
else:
    print("Oops!! Tries over.")