#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

    

def square_integers(int_list):
    int_squared = [int * int for int in int_list]
    return int_squared

def fizzbuzz():
    for i in range(101):
        if i == 0 :
            continue
        if i %3 == 0 and i %5 == 0:
            # i +=1
            print("FizzBuzz") 
        elif i %3 == 0:
            # i += 1
            print("Fizz") 
        elif i%5 == 0:
            # i += 1
            print("Buzz") 
        else :
            print(i) 