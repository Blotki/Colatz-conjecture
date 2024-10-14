highscore = 0
high1 = 0
def ddit(nomd):
    steps = 0
    startnum= nomd
    num = nomd
    for count in range(1,1000):
        global highscore
        global high1
        if num == 1:
            print("number " + str(startnum) + " has " + str(steps) + " steps")
            if highscore<steps:
                highscore=steps
                high1 = (nomd)
            break
        elif (num % 2) ==0:
            num = num/2
            steps = steps + 1
        else:
            num = num*3 + 1
            steps = steps + 1
start = int(input(" starting at"))
end = int(input(" ending at"))
if end < start:
    hold = start
    start = end
    end = hold
for bob in range(start , end):
    ddit(bob)
print (str(high1) + " is the biggest number with " + str(highscore) + " steps")