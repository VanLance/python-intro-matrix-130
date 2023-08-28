# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints
    # Determine a Logical way to solve the problem
        # Write each step out english
        # Write each step out in Python-esse
    # Invoke and Test Your Function


# Given a string of letters, write a function to see if the word  is a palindrome (the same word spelled forward and backwards).

# The given string will contain only letters 

# Examples:
# is_palindrome("RaceCar") \\ => True
# is_palindrome("mom")  \\ => True
# is_palindrome("Shoha") \\ => False

""" 
input string of letters
output = boolean
constraints: inputs only letters, only one word
RaceCar

approach:
look at each of letter and check equality
if unequal then non palindrome
if equal look at next letters
next letters moving first letter one to right
last letter one to left
continue checking all letters for eqaulity until unequal or i've checked to the middle

sudo code:
if not lettter =
return false
else =
continue
 """

def check_palindrome(astring):
    left_point = 0
    right_point = len(astring) - 1
    while left_point < right_point:
        if astring[left_point].lower() != astring[right_point].lower():
            return False
        left_point += 1
        right_point -= 1
    return True

print(check_palindrome("RaceCar"), True)
print(check_palindrome("mom"), True)
print(check_palindrome("Shoha"), False)

def check_with_reverse(astring):
    return astring.lower() == astring.lower()[::-1]

print(check_with_reverse("RaceCar"), True)
print(check_with_reverse("mom"), True)
print(check_with_reverse("Shoha"), False)