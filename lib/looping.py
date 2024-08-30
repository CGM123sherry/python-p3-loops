#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    # countdown from 10 to 0
    for i in range(10,0,-1):
        print(i)

    # print happynew year.
    print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
   squared_list =[x ** 2 for x in int_list]
   return squared_list

def fizzbuzz():
    # Iterate over the numbers from 1 to 100
    for i in range(1, 101):
        # Check if the number is a multiple of both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # Check if the number is a multiple of 3
        elif i % 3 == 0:
            print("Fizz")
        # Check if the number is a multiple of 5
        elif i % 5 == 0:
            print("Buzz")
        # If the number is not a multiple of 3 or 5, print the number
        else:
            print(i)

# Call the function to see the output
fizzbuzz()

