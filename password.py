
from re import S
import string
import random
import types

if __name__ == "__main__":
    # letters = string.ascii_letters --> this gives set of all the alphabates including lowe and upper case
    s1 = string.ascii_lowercase  # gives all letters of lowercase
    # print(s1)

    s2 = string.ascii_uppercase  # gives all letters of uppercase
    # print(s2)

    s3 = string.digits
    # print(s3) # gives digits form 0 to 9

    s4 = string.punctuation
    # print(s4) # gives all the punctuation marks

    pass_len = int(input("Enter password length : "))

    s = []  # this an empty list
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    # adding all the above created numbers at the end of empty list
    s.extend(s4)

    # print(s)
    # this will do the same thing as we do with the cards, i.e. shuffles the list in random way
    random.shuffle(s)
    # print(s)

    print("Your password is : ", end="")
    # print("".join(s[8:pass_len+8])) # join method takes all elements of an iterable and converts it into a string, so here list is an iterable and we converting it into a single string..

    # an alternative way
    print("".join(random.sample(s, pass_len)))
