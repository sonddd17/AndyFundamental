#####FizzBuzz

def FizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

######## Reverse A String
def ReverseText(text):
    reversedText = ""
    for n in range (len(text)-1,-1,-1):
        reversedText += text[n]

    return reversedText
###print("Hello"[::-1]) is a short cut for the loop
        
### min max

def MaxNum(num):
    m = num[0]
    for n in num:
        if n == m or n < m:
            continue
        elif n > m:
            m = n
        
    return m
def MinNum(num):
    m = num[0]
    for n in num:
        if n == m or n > m:
            continue
        elif n < m:
            m = n
    return m

####### Check if palindrome

def is_palindrpome(text):
    texts = text.lower().replace(" ","")
    ReverseText = texts[::-1]
    return texts == ReverseText
Words = "A man a plan a canal Panama"

#print(is_palindrpome(Words))

#######remove_duplicates(items)

def remove_duplicates(items):
    results = []

    for item in items:
        if item not in results:
            results.append(item)
    return results

items = [1, 2, 2, 3, 1, 4,4,6,5,7,7,8]

'''print(remove_duplicates(items))

print(list(set(items)))
print(list(dict.fromkeys(items)))

print(list(set([3, 1, 4, 1, 5, 9, 2, 6])))
print(list(set(["banana", "apple", "cherry", "apple"])))
print(list(set([-5, 10, -3, 100])))'''


#dictionary

def wordcount(n):

    texts = n.lower().split()
    counts = {}
    for text in texts:
        if text not in counts:
            counts[text] = 1

        else:
            counts[text] += 1
    
    return counts
texts = "the cat sat on the mat the cat ran"


##### try - except

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot Divide by zero"
    else:
        return "Invalid operator"



def get_even(numbers):
    return [ x for x in numbers if x%2 == 0]

def squares_odds(numbers):
    return [ x*x for x in numbers if x % 2 != 0  ]

numbers = [1,2,3,4,5,6,7,8,9,10]

###### Temperature converter

def convert_temp(degree, type):
    if type == 'C' or type == 'c':
        return degree*9/5 +32 
    elif type == 'F' or type == 'f':
        return (degree -32)*(5/9)
    else:
        return "invalid Operator"

print(convert_temp(0, 'Cl'))

def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total
user_input = input("Enter Numbers: ")
number_strings = user_input.split()
numbers = [int(n) for n in number_strings]
result = add_all(*numbers)
print(result)


def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

isDone = True
user_infos = {}
while isDone :
    kinput = input("Enter Key: ") 
    
    if kinput != "":
        vinput = input("Etner Value: ")
        if vinput != "":
            user_infos[kinput.strip()] = vinput.strip()
        else:
            print("Please re enter")
    else:
        isDone = False
        print("This is the user infomation:")

show_info(**user_infos)     