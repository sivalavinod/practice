#PASSWORD VALIDATIONS RANGE BTWN 6-12,UPPER LOWER LETTER NUMBER SYMBOL
# pswd=input('enter password')
# spcl_symbl=['@','#','$']
# if len(pswd)>6 and len(pswd)<12:
#     if not any(ch.isupper() for ch in pswd):
#         print("password should have atleat one upper letter")
#     if not any(ch.islower() for ch in pswd):
#         print("password should have atleat one lower letter")
#     if not any(ch.isdigit() for ch in pswd):
#         print("password should have atleat one digit")
#     if not any(ch in spcl_symbl for ch in spcl_symbl):
#         print("password should have atlest one special symbol")
#     print("valid password")
# else:
#     print("invalid password")


#PASSWORD VALIDATIONS RANGE BTWN6-12,UPPER LOWER LETTER NUMBER SYMBOL
# import re
# pswd=input("enter password")
# pat = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&*])[A-Za-z\d@#$%&*]{6,12}$"
# com=re.compile(pat)
# se=re.search(com,pswd)
# if se:
#     print("valid password")
# else:
#     print("invalid password")


#GENERATOR EXAMPLE
import random
#l=['z','s','e','r','g']
# i=iter(l)
# print(random.next(i))
# print(random.next(i))
# print(random.next(i))
# print(next(i))
# print(next(i))



# SORTING BASED ON NAME or AGE or SALARY
# from operator import itemgetter
# l=[]
# for x in range(2):
#     l2=[]
#     def dis(name,age,sal):
#         l2.append(name)
#         l2.append(age)
#         l2.append(sal)
#         l3=tuple(l2)
#         l.append(l3)
#     name=input("enter name")
#     age=eval(input("enter age"))
#     sal=eval(input("enter sal"))0
#     dis(name,age,sal)
#     l.sort(key=itemgetter(0,1,2))
# print(l)
# O/P:::::::::::::::::::::::
# enter namevind
# enter age12
# enter sal32
# enter namevind
# enter age12
# enter sal1
# [('vind', 12, 1), ('vind', 12, 32)]


# a=[2,5,78,65,24,57,6,0]
# b=["a","s","d","g","r","h","w"]
# l1=[]
# l2=[]
# while b:
#     min=b[0]
#     for n in b:
#         if n < min:
#             min=n
#     l1.append(min)
#     b.remove(min)
# print(l1)

# data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
# new_list = []
#
# while data_list:
#     minimum = data_list[0]  # arbitrary number in list
#     for x in data_list:
#         if x < minimum:
#             minimum = x
#     new_list.append(minimum)
#     data_list.remove(minimum)
#
# print (new_list)


# l=[1,5,89,65,32]
# res=(list(map(lambda x:x*2,l)))
# print(res)
#
# resT=[x*2 for x in l]
# print(resT)
# O/P::::[2, 10, 178, 130, 64]
#        [2, 10, 178, 130, 64]


#FACTORIAL OF A NUMBER
# class math:
#     def fact(x):
#         resu = 1
#         for y in range(1,x+1):
#             resu=resu*y
#         print(resu)
# v=math()
# v.fact(5)

# from functools import *
# l1=[1,2,3,4,5]
# l2=[1,2,3,4,5]
# res=list(map(lambda x,y:x+y,l1,l2))
# print(reduce((lambda x,y:x+y),res))



# l1=[1,2,3,4,5]
# l2=[1,2,3,4,5]
# res=[x+y for x,y in zip(l1,l2)]
# print(res)

#PRINT LIKE {1:4,2:5,3:6}
# l1=[1,2,3]
# l2=[4,5,6]
# x=dict(zip(l1,l2))
# print(x)



# a=5
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print("")
# for k in range(a,1,-1):
#     for l in range(1,k):
#         print(l,end="")
#     print("")


# enter the range10
# [1, 1, 2, 2, 4, 2, 6, 3, 9, 3, 12, 4, 16, 4, 20, 5, 25, 5, 30, 6]
# list=[]
# n=int(input("enter the range"))
# def calc():
#     l1, l2 = 1, 1
#     for x in range(n):
#         list.append(l1)
#         list.append(l2)
#         l1=l1+l2
#         l2=l1//l2
#     print(list)
# calc()


# {'a': 2, 'b': 3, 'x': 1, 'y': 2, 'l': 2, 'c': 1}
# a = 2 ,b = 3 ,x = 1 ,y = 2 ,l = 2 ,c = 1 ,
# 2 +3 +1 +2 +2 +1 +=11
# str='abxylaclybb'
# d={y:sum([1 for x in str if x==y]) for y in str}
# print(d)
# l=[]
# for x in d:
#     print(x,'=',d[x],',', end='')
#     l.append(d[x])
# print()
# for x in l:
#     print(x,'+',end='')
# print('=',end='')
# print(sum(l))

                                                                
# l=int(input("enter length"))
# d=int(input("enter length"))


# def res():
#     n1=int(input("enter no"))
#     n2=int(input("enter no"))
#     if n1>n2:
#         print("big no is",n1)
#     else:
#         print("big no is ",n2)#     add=n1+n2
#     print(add)
# res()

# res=lambda x,y:x if x>y else y
# x=int(input("enter no"))
# y=int(input("enter no"))
# print(res(x,y))

# s=["abcd"]
# st=[]
# l=len(s)
# for i in s(l-1):
#     i.append(st)
#     l=l-1
# print(st)


# t=0
# s=input("enter string")
# for i in s:
#    t+=ord(i)
# print(t)
#OUTPUT::::::::::::::::::::::
# enter stringAB
# 131


# subjects=["I", "You"]
# verbs=["Play", "Love"]
# objects=["Hockey","Football"]
# for i in range(len(subjects)):
#     for j in range(len(verbs)):
#         for k in range(len(objects)):
#             sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
#             print (sentence)
#
# OUTPUT::::::::::
# I Play Hockey.
# I Play Football.
# I Love Hockey.
# I Love Football.
# You Play Hockey.
# You Play Football.
# You Love Hockey.
# You Love Football.


# subjects=["I", "You"]
# verbs=["Play", "Love"]
# objects=["Hockey","Football"]
# for i in subjects:
#     for j in verbs:
#         for k in objects:
#             print(i,j,k)

# OUTPUT::::::::::
# I Play Hockey.
# I Play Football.
# I Love Hockey.
# I Love Football.
# You Play Hockey.
# You Play Football.
# You Love Hockey.
# You Love Football.


#PALINDROME OR NOT
# n=int(input("enter no"))
# n1=n
# sum,rem=0,0
# while n>0:
#     rem=n%10
#     sum=sum*10+rem
#     n=n//10
# if sum==n1:
#     print("palindrome")
# else:
#     print("not")

# import datetime as dt
# res=dt.datetime.now()
# print(res)
# OUTPUT::::::::::::::;
# 2019-12-11 16:09:54.010735


l=[1,2,3,4,5]
res=list(map(lambda x: x**2, l))
res2=list(filter(lambda x:x%2==0,l))
re=[x**2 for x in l]
re2=[r for r in l if r%2==0  ]
print(list(re))
print(list(res))
print(list(res2))
print(list(re2))


#
# l=[1,2,3,4,5]
# r=list(lambda x:x%2==0 for x in l)
# re=tuple(r)
# print(r)
# print(re)

