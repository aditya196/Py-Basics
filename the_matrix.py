import random as r
import time
counter = 0
symbols = ["0","1"," "," "]
line =[]
for i in range(118):
    x=r.randint(0,3)
    line.append(symbols[x])
    counter+=1
for i in range(100000):
    if counter%5==0:
        r_symbols = [r.randint(0,117) for x in range(10)]
        for i in r_symbols:
            line[i] = symbols[r.randint(0,3)]
    print(*line)
    counter+=1
    time.sleep(0.03)
