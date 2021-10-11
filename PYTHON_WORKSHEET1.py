#!/usr/bin/env python
# coding: utf-8

# In[1]:


#find the factorial of a number

num = int(input("Enter a number:"))
factorial = 1 
if num<0:
    print("Factorial doesnotnot esist")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range (1,num+1):
        factorial = factorial*i
    print('the factorial of',num, 'is', factorial)


# In[2]:


#finding wether a number is prime or composite

num = int(input("Enter a number:"))
for i in range(2,num):
    if num%i == 0:
        print("COMPOSITE")
        break
else:
    print("PRIME")


# In[4]:


#CHEACK WHEATHER AGIVEN STRIN IS PALINDROME OR NOT

string = input("Please enter a string : ")

if (string==string[::-1]):
    print("This is a palindrome string")
else:
    print("This is not a palindrome string")


# In[5]:


#finding third side from two given sides.

def right_angle_tringle():
    a=int(input('the lenght of one side = '))
    b=int(input('the lenght of other side =  '))
    c=int((a**2+b**2)**0.5)
    print('the value of third side is = ',c)


# In[6]:


right_angle_tringle()


# In[7]:


#print the frequency of each character preesent in a string

def freq(str):
    str=str.split()
    str2 = []
    
    for i in str:
        if i not in str2:
            str2.append(i)
    
    for i in range(0,len(str2)):
        print('Frequency of', str2[i], 'is:', str.count(str2[i]))
        
def main():
    str = "apple mango apple apple apple mango banana apple guava"
    freq(str)
    
if __name__=="__main__":
    main()

