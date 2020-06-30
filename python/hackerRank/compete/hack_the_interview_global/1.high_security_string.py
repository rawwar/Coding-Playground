"""https://www.hackerrank.com/hack-the-interview-global"""

from string import ascii_lowercase
# print(ascii_lowercase)
password = input()
strength_a = int(input())

strength = 0
for each in password:
    strength += (ascii_lowercase.index(each) + strength_a)%26
print(strength)