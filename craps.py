import random


##variables

##set list for naturals, craps, and point
natural=[7,11]
craps=[2,3,12]
point=[]
wins=0
losses=0
games=0
gameover=False



print("simulate craps to determine odds of winning in the long run")
print("could be done with a long markov chain but i wanna learn python")

##begin simulation
##come-out roll
for x in range(0,10000):
    dice1=random.randrange(1,6)
    dice2=random.randrange(1,6)
    roll=dice1+dice2

    if roll in natural:
        ##print("win")
        wins+=1
        gameover=True
    elif roll in craps:
        ##print("loss")
        losses+=1
        gameover=True
    else:
        point.append(roll)
        while gameover==False:
            dice1=random.randrange(1,6)
            dice2=random.randrange(1,6)
            roll=dice1+dice2
            if roll in point:
                ##print("win")
                wins+=1
                gameover=True
            elif roll==7:
                ##print("loss")
                losses+=1
                gameover=True
    x+=1
    point.clear
    gameover=False
winrate=wins/x
print(winrate)

roughodds=float(8/36)
for y in range (0,20):
    roughodds+=(2/3)*(1/9)*(26/36)**y
    print(roughodds)
