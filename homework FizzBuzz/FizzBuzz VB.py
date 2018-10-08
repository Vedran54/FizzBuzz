#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = int(raw_input("Please enter a number between 1 and 101: "))

# try-except statement: if the code inside try fails, the program automatically goes to the except part.

try:

    for numb in range (1, x+1):
        if numb % 3 == 0 and x % 5 == 0:
            print "fizzBuzz"
        elif numb % 3 == 0:
            print "fizz"
        elif numb % 5 == 0:
            print "buzz"
        else:
            print numb

except Exception as BLJAK:
    print "Please enter the whole number(integer)"