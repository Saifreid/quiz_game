def getScore(score, incorrectList):
    if score == 5:
        print("You got 5/5 nice going!")
    elif score == 4:
        print("You got 4/5 almost there!")
        print("Question you got wrong:", incorrectList[0])
    else:
        print("You got {}/5 better luck next time".format(score))
        print("Question you got wrong:", incorrectList)

print("Hello and welcome to my quiz game:")
print("In this game I will ask you 5 questions at the end \nI will tell you your score depending on your answers!")
score = 0
incorrect = []
print("Ready?")
print("Question 1:\nHow many full weeks are in 1 year?")
answer = input()
if(answer == "52"):
    score += 1
else:
    incorrect.append(1)
print("Question 2:\nWhat is the capital city of Djibouti?")
answer = input()
if("djibouti" in answer.lower()):
    score += 1
else:
    incorrect.append(2)
print("Question 3:\nWhat is the videogame from Nintendo that you play as the character Link?")
answer = input()
if("zelda" in answer.lower()):
    score += 1
else:
    incorrect.append(3)
print("Question 4:\nWhat timezone is the state Pennsylvania in?")
answer = input()
if("eastern" in answer.lower() or answer.lower() == "est"):
    score += 1
else:
    incorrect.append(4)
print("Last Question!")
print("Question 5:\nWhat color does red and blue make when put together?")
answer = input()
if(answer.lower() == "purple"):
    score += 1
else:
    incorrect.append(5)
getScore(score, incorrect)