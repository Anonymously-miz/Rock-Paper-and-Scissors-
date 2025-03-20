import random

#num = random.randint(1, 100)
#print("num")
#
#district_of_Sierra_Leone = ['Port Loko', "Koinadugu", "Bombali", "Tonkolili", "Kambia", "Karene", "Western Area Urban", "Western Area Rural", "Kono", "Kenema", "Kailahun", "Bo", "Moyamba", "Bonthe", "Pujehun"]
#print(district_of_Sierra_Leone[-7])
#district_of_Sierra_Leone.append("Abass Town")
#district_of_Sierra_Leone.extend(["Kabala", "Makeni", "Magburaka", "Lunsar", "Masiaka", "Koidu Town", "Koindu", "Segbwema", "Pendembu", "Yengema", "Zimmi", "Goderich"])
#
#district_of_Sierra_Leone.insert(7, "Freetown")
#
#print(district_of_Sierra_Leone)

#friends = ["Abass", "Yusuf", "Michael", "Mitchel", "Glennard"]
#print("Who will pay the Bill")
#pay = random.randint(0, 4)
#if pay == 0:
#    print(friends[0])
#elif pay == 1:
#    print(friends[1])
#elif pay ==2:
#    print(friends[2])
#elif pay == 3:
#    print(friends[3])
#else:
#    print(friends[4])
#
#print(random.choice(friends))
#print(friends[pay])

make_choice = ['ROCK', 'PAPER', 'SCISSORS']
computer_choice = random.randint(0,2)
arts0 = '''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
arts1 = ''''\
'---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
arts2 = '''' \
'---'   ____)____
          ______)
       __________)
      (____)
---.__(___)' \
'''
yourChoice =int (input("Make your choice: type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if yourChoice == 0:
    if yourChoice == 0 and computer_choice == 1:
            print("you choose Rock:\n" ,arts0)
            print("Computer choose Paper:\n", arts1)
            print("you lose")
    elif yourChoice == 0 and computer_choice == 2:
            print("you choose Rock:\n", arts0)
            print("Computer choose Scissors:\n", arts2)
            print("you win")
    else:
            print("you choose Rock:\n", arts0)
            print("Computer choose Rock:\n", arts0)
            print("It's a draw")
elif yourChoice == 1:
    if yourChoice == 1 and computer_choice == 0:
            print("you choose Paper:\n", arts1)
            print("Computer choose Rock:\n", arts0)
            print("you win")
    elif yourChoice == 1 and computer_choice == 2:
            print("you choose Paper:\n", arts1)
            print("Computer choose Scissors:\n", arts2)
            print("you lose")
    else:
            print("you choose Paper:\n", arts1)
            print("Computer choose Paper:\n", arts1)
            print("It's a draw")
else:
    if yourChoice == 2 and computer_choice == 0:
            print("you choose Scissors:\n", arts2)
            print("Computer choose Rock:\n", arts0)
            print("you lose")       
    elif yourChoice == 2 and computer_choice == 1:
            print("you choose Scissors:\n", arts2)
            print("Computer choose Paper:\n", arts1)
            print("you win")
    else:
            print("you choose Scissors:\n", arts2)
            print("Computer choose Scissors:\n", arts2)
            print("It's a draw")

    