import numpy


num=int(input("いくつまで数えますか？"))
for i in range(1,num+1):
    if (i%3==0 and i%5==0):
        print("Fizz Buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("Buzz")
    else: print(i)