# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tdc4cplihzJFywuApSV8giWld1aHg5Qv
"""

# Question No. 1
list = (1,2,3,4,5,6,7,8,9)
for num in list:
  if num % 2 != 0:
    print(num)

# Question No. 2a
numbers = [1,2,3,4,5,1,4,5]
Sum = sum(numbers)
print(Sum)
Sum = sum(numbers, 10)
print(Sum)

# Question No. 2b
numbers=[10,5,15,20]
total=sum(numbers)
print("The Total Sum Of List is", total)

# Question No. 3 (1st way)
values = [1,2,3,4,5,6,7,8,9]
values.reverse()
print(values)

# Question No. 3 (2nd way)
value = [1,3,5,7,9]
print(value[::-1])

# Question No. 4
num = [2,4,6,8,10,20]
max1 = max(num)
num.remove(max1)
max2=max(num)
print("The Top Two Maximum Numbers In a List is:", max1, "and", max2)

# Question No. 5
num = [2,4,6,8,10,20]
max1 = max(num)
num.remove(max1)
max2=max(num)
print("The Second Highest Number In a List is:", max2)

# Question No. 6
string = "Abdul Hadi Khan"
sorted_string = sorted(string,reverse=True)
print("The sorted string in decending order is:", sorted_string)

# Question No. 7
string = "SSUET SSUET"
l = string.split()
s = set(l)
print(''.join(s))

# Question No. 8   
alphabet = input("Enter a character:")
alphabet = alphabet.lower()
if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u":
 print(alphabet, "is a vowel.")
else:
  print(alphabet, " is a consonant.")

# Question No. 9
number = int(input("Enter a number:"))
factorial = 1
for i in range(1, number + 1):
  factorial *= i
print("The Factorial of", number, "is",factorial)

# Question No. 10
list1 = [10,20,30]
list2 = [40,50,60]
list1.extend(list2)
print("Merged List:", list1)

