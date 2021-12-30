import sys
import random

ans = True

while ans :
    questions =int( input("Ask the magic 5 ball a question: (press enter to quit):"))
    answer = random.randint(1,5)
    if questions == "":
        break
    elif answer == 1 :
        print("Its certian")
    elif answer == 2:
        print("Outlook good")
    elif answer == 3 :
        print("You may rley on it")
    elif answer == 4 :
        print("Ask again later")
    elif answer == 5 :
        print("Reply hezy try agin")
        break
