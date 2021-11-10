from random import randrange
n = randrange(10)
chances = 5
while chances !=0:
    v = int(input('Enter Number : '))
    if n ==v:
        print("Congratulations, You Win! the number was ",n)
        break
    if (n < v):
          chances-=1
          print("Smaller, you have "+str(chances)+" chances left")

    else :
        chances-=1
        print("Bigger, you have "+str(chances)+" chances left")
        

if (chances==0):
    print("You Lose!, the number is ", n)