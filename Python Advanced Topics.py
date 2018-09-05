#LIST COMPREHENSION & GENERATOR EXPRESSION

#Q.1- Write a python program to print the cube of each value of a list using list comprehension.

l=[2,5,7,9,10]
list1=[i*i*i for i in l]
print(list1)

#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.
a=int(input("enter the range till which u want to find prime no"))
k=0
list2=[i for i in range(1,a) if all(i%y!=0 for y in range(2,i))]
print(list2)

#Q.3- Write the main differences between List Comprehension and Generator Expression.

#A List Comprehension is like the plain range function, executes immediately and returns a list.
#A Generator Expression returns and object that can be iterated over.
#The comparision is not perfect because in an object returned by the generator expression we cannot access an element by index.
#The difference between the two kinds of expressions is that the List comprehension is enclosed in square brackets [] while the Generator expression is enclosed in plain parentheses ()



#LAMBDA & MAP

#Q.1- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.

Celsius = [39.2, 36.5, 37.3, 37.8]
d=list(map(lambda x:(x*1.8)+32,Celsius))
print(d)

#Q.2- Apply an anonymous function to square all the elements of a list using map and lambda.
list3=[3,7,11,13,15]
e=list(map(lambda c: c*c,list3))
print(e)

#FILTER & REDUCE

#Q.1- Filter out all the primes from a list.

def isprime(v):
        for i in range(2,v):
            if v%i==0:
                return False
            else:
                return True

list4 = [3,5,7,11,17,23,10,6]
h=list(filter(isprime,list4))
print(h)

#Q.2- Write a python program to multiply all the elements of a list using reduce.

list5 = [10,20,30,8,12]
from functools import *

n = reduce(lambda x,y:x*y,list5)
print(n)
    

       
