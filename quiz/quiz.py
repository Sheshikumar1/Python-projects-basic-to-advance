print("welcome to game")

playing=input("Do you want to play? ")

if playing.lower() !="yes":
    quit()
print("Okay ! lets play :)")

score=0

answer=input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print('correct!')
    score+=1
else:
    print('incorrect!')

answer=input("What does GPU stands for? ").lower()

if answer == "graphic processing unit":
    print('correct!')
    score+=1
else:
    print('incorrect!')
answer=input("What does RAM stand for? ").lower()

if answer == "Random Acess Memory":
    print('correct!')
    score+=1
else:
    print('incorrect!')
answer=input("What does PSU stand for? ").lower()

if answer == "power supply unit":
    print('correct!')
    score+=1
else:
    print('incorrect!')
answer=input("What does MMU stand for? ").lower()

if answer == "central Memory Management unit":
    print('correct!')
    score+=1
else:
    print('incorrect!')


print("You got "+ str(score) +" Questions corret")
print("You got "+ str((score/5)*100)+"%.")
