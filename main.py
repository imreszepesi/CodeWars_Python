""""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""
import math


def array_diff(a, b):
    list_difference = []
    for item in a:
        if item not in b:
            list_difference.append(item)

    return list_difference
""""
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive 
alphabetic characters and numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphabets 
(both uppercase and lowercase) and numeric digits.
"""
def duplicate_count(text):
    lowerText = text.lower()
    found = []
    for char in lowerText:
        if (not (char in found) and lowerText.count(char) > 1):
            found.append(char)

    return len(found)

"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(sentence):
    vowels = ["a","e","i","o","u"]
    count = 0
    for i in sentence:
        for j in vowels:
            if i == j:
                count = count + 1

    return count


"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
"""

def create_phone_number(n):
    ujstring = ""
    ujstring = "(" + str(n[0]) + str(n[1]) + str(n[2]) + ") " + str(n[3]) + str(n[4]) + str(n[5])+ "-" + str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
    print(ujstring)





"""
Write a function that takes in a string of one or more words, 
and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
"""
def spin_words(sentence):
    def remove_end_spaces(string):
        return "".join(string.rstrip())
    words = sentence.split()
    sentence = ""
    for i in words:
        if len(i) >= 5:
            sentence += i[::-1] + " "
        else:
            sentence += i + " "

    return remove_end_spaces(sentence)



"""
A square of squares
You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
"""
def is_square(n):
    if n >= 0:
        return n == math.isqrt(n) ** 2
    else:
        return False


"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

"""
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""


