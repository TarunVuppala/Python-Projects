import random

options = ["r", "p", "s"]

print('''
      

      -----INSTRUCTIONS-----
      Rock --> r
      Paper --> p
      Scissors --> s


      ''')

user_score = 0
computer_score = 0

while True:
    if user_score < 5 and computer_score < 5:
        user_option = input("Player (r / p / s): ")
        computer_option = random.choice(options)

        if user_option=="p" and computer_option=="s":
            computer_score+=1
        elif user_option=="s" and computer_option=="r":
            computer_score+=1
        elif user_option=="r" and computer_option=="p":
            computer_score+=1
        elif user_option=="s" and computer_option=="p":
            user_score+=1
        elif user_option=="r" and computer_option=="s":
            user_score+=1
        elif user_option=="p" and computer_option=="r":
            user_score+=1
        else:
            pass

        print(f"\nPlayer: {user_option} ({user_score}/5)\nA.I: {computer_option} ({computer_score}/5)")
    else:
        if user_score>computer_score:
            print("\nYou Won!!!")
            break
        elif computer_score>user_score:
            print("\nOops! A.I won.")
            break
        break