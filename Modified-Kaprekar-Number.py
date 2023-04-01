'''
A modified Kaprekar number is a positive whole number n with d digits, such that when we split its square into two pieces - a right hand piece r with d digits and a left hand piece l that contains the remaining d or d−1 digits, the sum of the pieces is equal to the original number (i.e. l + r = n).
Note: r may have leading zeros.
Here's an explanation from Wikipedia about the ORIGINAL Kaprekar Number (spot the difference!): In mathematics, a Kaprekar number for a given base is a non-negative integer, the representation of whose square in that base can be split into two parts that add up to the original number again. For instance, 45 is a Kaprekar number, because 45² = 2025 and 20+25 = 45.
The Task
You are given the two positive integers p and q, where p is lower than q. Write a program to determine how many Kaprekar numbers are there in the range between p and q (both inclusive) and display them all.
'''


import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    li1=[]
    for i in range(p,q+1):
      square=str(i*i)
      first_half=square[len(square)//2:] 
      
      if square[:len(square)//2]=="":
         second_half='0' 
      else:
        second_half=square[:len(square)//2]
        
      if int(first_half)+int(second_half)==i:
        li1.append(i)
    if len(li1)==0:
        print("INVALID RANGE")
    print(" ".join(str(i) for i in li1))
    
    
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
