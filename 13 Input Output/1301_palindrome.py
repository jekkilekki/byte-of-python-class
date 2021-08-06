# 1301_palindrome.py

def reverse(text):
         return text[::-1]

def is_palindrome(text):
         return text.lower() == reverse(text.lower())

check = input('Enter text: ')
if is_palindrome(check):
         print('"{}" is a palindrome.'.format(check))
else:
         print('Not a palindrome.')
