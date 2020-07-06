#!/usr/bin/env python
# coding: utf-8

# In[12]:


'''1)  Create a variable, paragraph, that has the following content: 
"Python is a great language!", said Fred. "I don't ever remember having this much fun before." 
 '''
paragraph= '"Python is a great language!", said Fred. "I don\'t ever remember having this much fun before." '
print(paragraph)


# In[4]:


'''2. Write an if statement to determine whether a variable holding a year 
is a leap year.
'''
year=int(input("Enter the year"))
if year%4 is 0:
    print("{0}  is leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


# In[13]:


'''3. Write code that will print out the anagrams (words that use the same 
letters) from a paragraph of text. '''

word_list = ["percussion", "supersonic", "car", "tree", "boy", "girl", "arc"]


anagram_list = []
for word_1 in word_list: 
    for word_2 in word_list: 
        if word_1 != word_2 and (sorted(word_1)==sorted(word_2)):
            anagram_list.append(word_1)
print(anagram_list)
            


# In[2]:


''' 4. Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the list. What is the first item on the list? What is the second item on the list? 
'''


community_list=[]
name=input("Enter the name of the family members or colleagues or friends to append in the list")
community_list.append(name)
print(community_list)


# In[12]:


'''5) Create a tuple with your first name, last name, and age. Create a list, 
people, and append your tuple to it. Make more tuples with the corresponding information from your friends and append them to the list. Sort the list. When you learn about sort method, you can use the key parameter to sort by any field in the tuple, first name, last name, or age. 
'''



def sort_field(l):
   # keyword=int(input("enter the index through which you want to sort"))
    return l[m]
def sorting_list(l):
    return sorted(l,key=sort_field)

people_info=[('Rojina','Maharjan',21),('Kajol','Lama',22),('Babita','Ramtel',21)]
m=2
print(sorting_list(people_info))


    
    


# In[4]:


'''6)Create a list with the names of friends and colleagues. Search for the 
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it. 
'''

created_list=['raj','laxman','hari']
for name in created_list:
    if name is 'john':
        found=1
    else:
        found=0
if found is 0:
    print("Not Found")


# In[12]:


'''7) Create a list of tuples of first name, last name, and age for your friends and colleagues. If you don't know the age, put in None. Calculate the average age, skipping over any None values. Print out each name, followed by old or young if they are above or below the average age. 
'''

community_info=[('Rojina','Maharjan',21),('Kajol','Lama',25),('Babita','Ramtel',30),('Dbes','Rijal',None)]
average=0
sum=0
for item in community_info:
    j = item[2]
    if j is not None:
        sum=sum+j
        average=sum/(len(community_info))
        if j>average:
            print(item[0],'old')
        else:
            print(item[0],'young')
#print(average)


# In[8]:


'''8)Write a function, is_prime, that takes an integer and returns True if 
the number is prime and False if the number is not prime.
'''

input_number=int(input("Enter a number"))
def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if num %i is 0:
                print(" False {0} is not a prime number".format(num))
        else:
              print(" True {0} is a prime number".format(num))
   
    else:
        print(False)
is_prime(input_number)


# In[8]:


'''9) Write a binary search function. It should take a sorted sequence and the item it is looking for. It should return the index of the item if found. It should return -1 if the item is not found. ''' 


def binary_function(list,n):
    for i in list:
        if  i is n:
            print(list.index(i))
            
        else:
            return -1
            
binary_function([4,5,6,7,8,9],77)


# In[19]:


'''10) Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case (i.e. this_is_camel_cased). Modify the function by adding an argument, separator, so it will also convert to the kebab case (i.e.this-is-camel-case) as well. 
'''
def change_snakecase(str): 
    i = [str[0].lower()] 
    for c in str[1:]: 
        if c.isupper():
            i.append('_') 
            i.append(c.lower()) 
        else: 
            i.append(c) 
      
    return ''.join(i)

change_snakecase('ThisIsCamelCased')

def change_kebabcase(str): 
    i = [str[0].lower()] 
    for c in str[1:]: 
        if c.isupper():
            i.append('-') 
            i.append(c.lower()) 
        else: 
            i.append(c) 
      
    return ''.join(i) 

change_kebabcase('RojinaMaharjanLalitpur')


# In[36]:


'''11)Create a variable, filename. Assuming that it has a three-letter extension, and using slice operations, find the extension. For README.txt, the extension should be txt. Write code using slice operations that will give the name without the extension. Does your code work on filenames of arbitrary length? 
'''

filename='HelloIamwithoutextension.txt'
extension= filename[-3:]
print(extension)
filename_without_extension=filename[:-4]
print(filename_without_extension)


# In[17]:


'''12) Create a function, is_palindrome, to determine if a supplied word is 
the same if the letters are reversed. 
'''

def is_palindrome(word):

    letters = list(word)
    palindrome = True

    for letter in letters:
        if letter == letters[-1]:
            letters.pop(-1)
        else:
            palindrome = False
            break

    return palindrome
is_palindrome('madam')


# In[33]:


'''13) Write a function to write a comma-separated value (CSV) file. It should accept a filename and a list of tuples as parameters. The tuples should have a name, address, and age. The file should create a header row followed by a row for each tuple. '''
import csv
import os
from csv import DictWriter
filename='rojinamaharjan.csv'


def write_to_csv(list_of_tuple, filename):
    if os.path.exists(filename):
        with open(filename, write_mode) as csvfile:
            writer = DictWriter(csvfile, fieldnames=["name", "address", "age"])
            writer.writeheader()
            for each in list_of_tuple:
                writer.writerow(each)
                print(each)
                
tuple_param=[('Roji','lubho',21)]
print(write_to_csv(tuple_param,'rojinamaharjan.csv'))



# In[8]:


'''14)  Write a function that reads a CSV file. It should return a list of dictionaries, using the first row as key names, and each subsequent row as values for those keys.'''
import csv
import os
from csv import DictReader, DictWriter
filename='rojina.csv'
phonebook=[]

            
def add_item(phonebook, *, name, number, email, added_date):
    bookitem = {"fullname": "", "number": "", "email": "", "added_date": ""}
    bookitem["fullname"] = name
    bookitem["number"] = number
    bookitem["email"] = email
    bookitem["added_date"] = added_date
    phonebook.append(bookitem)           
def write_to_csv(phonebook, filename, write_mode = "w"):
    with open(filename, write_mode) as csvfile:
        writer = DictWriter(csvfile, fieldnames=["fullname", "number", "email","added_date"])
        writer.writeheader()
        for each in phonebook:
            writer.writerow(each)
def add_action():
    items = []
    while True:
        fullname = input("Enter Name: ")
        if not fullname.strip():
            print("Fullname cannot be empty. Please continue")
            continue
        ph_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        added_date = input("Date: ")
        items.append((fullname, ph_number, email, added_date))
        char = input("Do you want to continue? [y/yes]: ")
        if not (char.lower() == "y" or char.lower() == "yes"):
            break
    return items
def list_items(phonebook):
    print("FullName\t PhoneNumber\t Email\n==========", end="\n")
    action = input('sort by (D)ate or (N)ame:')
    if action.upper() == 'N':
        sorted_name = sorted(phonebook, key=lambda k: k['fullname'])
        for item in sorted_name:
            print("{}\t {}\t {}".format(
                item["fullname"], item["number"], item["email"], ['added_date']
            ))
        print("=" * 10)
        
        
def cli():
    global filename
    phonebook = []
    if os.path.exists(filename):
        with open(filename, "r") as csvfile:
            reader = DictReader(csvfile, fieldnames=["fullname", "number", "email", "added_date"])
            next(reader)
            phonebook.extend(reader)
    while True:
        print("""
        A: Add
        L: List
        E: Exit
        """)
        action = input("Please select a action: ")
        if action.upper() == "A":
            collected_items = add_action()
            for name, number, email, added_date in collected_items:
                add_item(phonebook, name=name, email=email, number=number, added_date=added_date)
        elif action.upper() == "L":
            # list action
            list_items(phonebook)
        elif action.upper() == "E":
            write_to_csv(phonebook, filename)
            break
        else:
            print("invalid action selected")
# print(__name__)
if __name__ == "__main__":
    cli()


# In[1]:


'''15) Imagine you are designing a banking application. What would a customer look like? What attributes would she have? What methods would she have? 

'''

class bankingapplication:
    def __init__(self):
        self.balance=0
        print("Welcome to Banking Application. You can withdraw and deposit balance")
        
  
    
    def deposit_balance(self):
        amount=int(input("Enter the amount you want to deposit:"))
        self.balance+=amount
        
    def withdraw_balance(self):
        amount=int(input("Enter the amount you want to withdraw:"))
        if amount>=self.balance:
            print("Balance not sufficient")
        else:
            self.balance=self.balance-amount
         
                 
    def display_information(self):
        print("the balance that you have is {0}".format(self.balance))
        
    
b=bankingapplication()
b.deposit_balance()
b.withdraw_balance()
b.display_information()

    


# In[ ]:


'''16) Imagine you are creating a Super Mario game. You need to define a class to represent Mario. What would it look like? If you aren't familiar with SuperMario, use your own favorite video or board game to model a player. 
'''

class super_mario:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def printinfo(self):
        print(self.name, self.age,self.height)
      
class mario(super_mario):
    
    
    


# In[5]:


'''17)Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator. Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors. '''



def add_numbers(a,b):
    sum=0
    sum=a+b
    return sum

def sub_numbers(a,b):
    diff=0
    diff=a-b
    return diff
def mul_numbers(a,b):
    mul=1
    mul=a*b
    return mul
def div_numbers(a,b):
    quotient=1
    try:
        quotient=a/b
        return quotient
    except:
        print("Zero Error")
try:
    num1 = int(input("enter the 1st number"))
    num2 = int(input("Enter the second number"))
    operator = input("Enter the operator")
except:
    print(" Please enter the number values")
while operator is not None:
    if operator=='+':
        result=add_numbers(num1,num2)
        print("the sum of {0} and {1} is {2}".format(num1,num2,result))
    elif operator=='-':
        sub_numbers(num1,num2)
    elif operator=='*':
        mul_numbers(num1,num2)
    elif operator=='/':
        div_numbers(num1,num2)
    else:
        print("Operator not defined")
    break



        
        


# In[10]:


'''18)Find a package in the Python standard library for dealing with JSON. Import the library module and inspect the attributes of the module. Use the help function to learn more about how to use the module. Serialize a dictionary mapping 'name' to your name and 'age' to your age, to a JSON string. Deserialize the JSON back into Python. 
'''

import json
self_info={
    'name':'rojina',
    'age' : 21
}

b=json.dumps(self_info)
print(b)


# In[12]:


'''19) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
 '''
open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
# Function to check parentheses 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "invalid"
    if len(stack) == 0: 
        return "Valid"
    else: 
        return "Invalid"
  
  
# Driver code 
string = "{[]{()}}"
print(string,"-", check(string)) 
  
string = "[{}{})(]"
print(string,"-", check(string)) 
  


# In[6]:


'''20)  Write a Python class to find the three elements that sum to zero 
from a list of n real numbers
'''
class sumtozero:
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < (len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(sumtozero().threeSum([9,4,5,-4,5,6,-7,-9,-8,6,-3]))


# In[ ]:




