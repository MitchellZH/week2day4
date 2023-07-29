# Write a function that will check if two given characters are the same case.
# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0
# EXAMPLES:
# same_case('C', 'B'), --> 1
# same_case('b', 'a') --> 1
# same_case('d', 'd'), 1)
# same_case('A', 's') --> 0
# same_case('\t', 'Z') --> -1
# same_case('H', ':') -->  -1


def checkCase(letter1, letter2):
    if letter1.isalpha() and letter2.isalpha():
      if letter1.isupper() and letter2.isupper():
          return 1
      if letter1.islower() and letter2.islower():
          return 1
      if letter1.islower() and letter2.isupper():
          return 0
      if letter1.isupper() and letter2.islower():
          return 0
    else:
        return -1
 
print(checkCase('H', ':'))
    

