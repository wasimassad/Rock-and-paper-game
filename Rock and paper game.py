import random

rock=('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper=('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissors=('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
game_image=[rock,paper,scissors]
person_you=int(input("what do you want to choose?:put the 0 for a rock put 1 for a paper put 2 for a scissors"))
print(game_image[person_you])
computer=random.randint (0,2)
print("computer chose")
print(game_image[computer])


if computer==person_you:
    print("No one win!")
elif (person_you==2 >computer==1):
    print("you Win")
elif person_you==1 > computer==0:
    print("you win!")
elif (person_you==0 < computer==2):
    print("you Win")
else:
    print("computer Win")
