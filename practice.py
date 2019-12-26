# s="vinod"
# count=0
# for x in s:
#     print(x)
#     count+=1
# print(count)
#
# for x in range(1,11):
#     for y in range(1,11):
#         print(x,"*",y,"=",x*y)
#
#
# fb1=0
# fb2=1
# for x in range(100):
#     fb=fb1+fb2
#     fb2=fb
#     fb1=fb2
#     if fb>49 and fb<501:
#         print(fb)
#
#s="deepu"
# s2=s.capitalize()
# print(s)
# print(s2)
#
#s1="hello students this is python"
# s2=s1.count("s")
# print(s2)
#
# s1="ABCD1024@%"
# s2=s1.encode()
# print(s2)
# print(type(s2))
# print(s1)
#
#def fun1(x):
#     print(x)
#
# fun1(10,)
# fun1(10,20,30)
# fun1(10,"sathya",False,10.25)"""
#


# s1={101:{"name":"vinod","marks":[75,85,95]},
#     102:{"name":"kumar","marks":[85,95,99]}
#     }
# print(s1)
# print(s1.keys())
# print(s1[101].keys())
# print(s1[101].values())
# print(s1[101].items())


# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
# d=[]
# d.append(a)
# d.append(b)
# d.append(c)
# for i in range(0,3):
#     for j in range(0,3):
#         for k in range(0,3):
#             if(i!=j&j!=k&k!=i):
#                 print(d[i],d[j],d[k])

# lower=int(input("Enter the lower limit for the range:"))   #15
# upper=int(input("Enter the upper limit for the range:"))    #17
# for i in range(lower,upper+1):
#     if(i%2!=0):
#         print(i)     # 15,17,19,21,23,25

# a=int(input("Enter value of first variable: "))  #12
# b=int(input("Enter value of second variable: "))   #15
# a=a+b
# b=a-b
# a=a-b
# print("a is:",a," b is:",b)   #a is: 15  b is: 12


# a,b=5,10
# a,b=b,a
# print(a,b)  #10,5


# a=[4,5,87,65,98,2,312]  #largest number without using built in functions
# ma=a[0]
# for x in a:
#     if ma<x:
#         ma=x
# print(ma)  #312


# a=[4,5,87,65,98,2,312]
# c=0
# for x in a:
#     c+=1
# a.insert(c,100)
# print(a)   #[4, 5, 87, 65, 98, 2, 312, 100]

# we con't modify the length of the tuple but we can modify the size of the tuple
# l=[1,2,3,4]
# t=(8,9,[12,13])
# print(l)
# print(t)
# t[2][1]=150000000
# print(t)

#reverse string
# s="vinod"[::-1]
# print(s)    #doniv


#remove duplicate words in a list
# l=["asdf","sasff","asdf","qwrr"]
# l2=list(dict.fromkeys(l))    # dictionary doesn't contains duplicates   dict.fromkeys  it helps to remove duplicates
# print(l2)

#
# l=[1,2,3,4,5,2,4]
# l2=
# print(l)

# import functools as fun
# s="azzxzxxxy"
# s2=[s]
# s3=[]


# s=["sun","mon","tue","wed","thu","fri","sat"]
# d=input("enter the day")
# n=int(input("enter the number"))
# if d in s:
#     r=s.index(d)
#     res=r+n+1
#     if res > 6:
#         p=res%7
#     else:p=res
# print(s[p])


# one i/p is number and another i/p is char and o/p is in number like 2*four=8
# from word2number import w2n
# def dis():
#     n=eval(input("enter number"))
#     c=input("ener number in characters")
#     a=w2n.word_to_num(c)
#     res=n*a
#     print(res)
# dis()


# I/P IN NUMBER O/P IN BINARY FORMAT
# a=6
# b=bin(a)
# print(b)


#input in numbers format and o/p in character
# import inflect
# n = int(input("enter number:::"))
# c = int(input("ener number in characters:::"))
# res=n*c
# r=inflect.engine()
# ans=r.number_to_words(res)
# print(ans)


import os
# f=open("index.txt",'w')
# text=input("enter text")
# f.write(text)
# f.close()
# t=open("index.txt")
# te=t.read()
# print(te)



#threading example
# from threading import*
# import time
# def dis(z,a):
#     sum=z+a
#     print(sum)
#     for x in range(1,10):
#         print(x)
# t=Thread(target=dis,args=(10,100))
# t.start()
#
# for y in range(20,40):
#     print(y)


#TO PRINT DATE WHAT WE GAVE
# from datetime import datetime
# a=input("enter date")
# print(type(a))
# b=datetime.strptime(a,'%m-%d-%Y')
# print(b)



# from datetime import datetime
# print("1.add customer   2.deleting   3.list of customer    4.exit  ")
# c=int(input("enter your choice"))
# if c==1:
#     cus_id=input("enter cus id")
#     if len(cus_id) >= 3:
#         cus_name=input("enter cus name")
#         if len(cus_name) > 2:
#             cus_address=input("enter customer address")
#             dob=input("enter date of birth in format of mm-dd-yyyy")
#             age=datetime.strptime(dob,'%m-%d-%Y')
#             if age.year < 2000:
#                 cus_mobile=input("enter cus mobile no")
#                 with open("index.txt",'a')as v:
#                     v.write(cus_id+","+cus_name+","+cus_address+","+dob+","+cus_mobile +'\n')
#                     print("inserted successfully")
# elif c==2:
#     #check_id=input("enter customer id")
#     with open("index.txt",'r')as f:
#         ff=f.read()
#         print(ff)
#
# elif c==3:
#     pass



# a="hai hello how are you"
# b=a.split()
# c=b[0]
# d=b[len(b)-1]
# c,d=d,c
# j=''.join(b)
# print(j)


#
# import datetime as dt
# import os
# class Pro():
#     def __init__(self, choice):
#
#         if choice == 1:
#             self.addCust()
#         elif choice == 2:
#             self.delCust()
#         elif choice == 3:
#             self.display()
#
#     def addCust(self):
#         Cust_id = (input("Enter the customer id"))
#         if len(Cust_id) >= 3 and Cust_id.isdigit():
#             Cust_name = input("Enter the customer name")
#             if len(Cust_name) >= 2 and Cust_name.isalpha():
#                 Cust_address = input("Enter the customer address")
#                 Date_of_birth = input("Enter the cust dob in dd/mm/yyyy")
#                 dob = Date_of_birth.split('/')
#                 day = (dob[0])
#                 month = (dob[1])
#                 year = (dob[2])
#                 if len(day) < 2 or len(month) < 2 or len(year) < 4:
#                     print("Please enter the date in dd/mm/yyyy")
#                 else:
#                     day = int(dob[0])
#                     month = int(dob[1])
#                     year = int(dob[2])
#                     age = dt.datetime.now() - dt.datetime(day=day, month=month, year=year)
#                     ageyear = age.days / 365
#                     if (round(ageyear) >= 15):
#                         Mobile_number = input("Enter the customer mobile number")
#                         with open("add.txt", 'a+') as file:
#                             file.write(
#                                 Cust_id + ',' + Cust_name + ',' + Cust_address + ',' + Date_of_birth + ',' + Mobile_number + "\n")
#                             print("Succesfully written")
#                     else:
#                         print("Sorry your are not lisensed")
#
#     def delCust(self):
#         Cust_id = input("Enter the cust id")
#         if len(Cust_id) <= 2:
#             pass
#         else:
#             deletevar = input("enter id to delete=")
#             with open('add.txt', 'r') as f:
#                 lines = f.readlines()
#                 orignalcountv = len(lines)
#             with open('add.txt', 'w') as f:
#                 for line in lines:
#                     linesplit = line.split(',')
#                     if linesplit[0] != deletevar:
#                         f.write(line)
#             num_lines = sum(1 for line in open('add.txt'))
#             if orignalcountv != num_lines:
#                 print('line deleted')
#             else:
#                 print('given customer id is not there give proper id  ')
#
#     def display(self):
#         di = {}
#
#         with open("add.txt", "r") as file:
#             try:
#                 for line in file.readlines():
#                     sp = line.split(",")
#                     Date_of_birth = sp[3]
#                     dob = Date_of_birth.split('/')
#                     day = int((dob[0]))
#                     month = int((dob[1]))
#                     year = int((dob[2]))
#                     age = dt.datetime.now() - dt.datetime(day=day, month=month, year=year)
#                     ageyear = age.days / 365
#                     ageyear = round(ageyear)
#                     di[ageyear] = line
#             except IndexError:
#                 print("File is Empty")
#         try:
#             for keys in sorted(di.keys(), reverse=True):
#                 print(di[keys])
#         except Exception:
#             print("Files is Empty")
#
#
# while True:
#     print("1. Add customer  \n 2. Delete customer \n 3. List of customer \n 4. Exit")
#     choice = int(input("Enter your choice"))
#     if choice == 4:
#         break
#     else:
#         c = Pro(choice)




#RECURSIVE FUNCTION
# def call():
#     n=int(input("enter upto number"))
#     a=0
#     b=1
#     c=0
#     for i in range(n):
#
#         if c <=n:
#             print(a,end=' ')
#             c=a+b
#             a=b
#             b=c
# call()



# EMPHISIS INTERVIEW QUESTIONS GIVEN BY NARENDRA SATHYA........................................
# 2.. write the o/p
# def odds(n):
#     i=10
#     odd=[i for i in range[n+1] if i%2!=0]
#     for i in odd:
#         yield i
#     for i in odds(8):
#         print(i)

# 3..TO REMOVE DUPLICATES
# l=[2,3,4,3,3,3,2,2,1,6]
# print(list(set(l)))

#4..o/p of the code
# a=set([1,2,[3,4])
# O/P IS SyntaxError

#5.. O/P OF BELOW CODE
# dictionary={"apple":10,"for":45,"orange":90}
# print("apple" in dictionary)
# ans is True

#6..write o/p
# test={1:'A',2:'B',3:'C'}
# del test[1]
# print(test)
# test[1]='D'
# print(test)
#
# O/P
# {2: 'B', 3: 'C'}
# {2: 'B', 3: 'C', 1: 'D'}

#7..O/P
# mylist=['ab','cd']
# for i in mylist:
#     mylist.append(i.upper())
# print(mylist)


#8..O/P
# my_string=['python','gfh']
# for i in range(my_string):
#     print(i)
# O/P:TypeError: 'str' object cannot be interpreted as an integer

#9..O/P
# t=(1,2,3,4,5,6,7,8,9)
# print(t(t.index(5)))
# print(t[t[t[6]-3]-6])
# print(t[-1])

# O/P::
# 5
# 9
# 9

#12..
# def extend(val,list=[]):
#     list.append(val)
#     return list
# list1=extend(10)
# list2=extend(123,[])
# list3=extend('a')
# print "list1=%s"%list1
# print "list1=%s"%list1
# print "list1=%s"%list1
#
# O/P::SyntaxError: Missing parentheses in call to 'print'. Did you mean print("list1=%s"%list1)?

#ZIP AND UNZIP
# name=["vinod", "kumar","sivala"]
# marks=[98,78,89]
# subj=["maths","sci","soc"]
# a=zip(name,marks,subj)
# a=list(a)
# print(a)
# UNZIP
# nam,mark,sub=zip(*a)
# print(nam)
# print(mark)

# SUM OF VALUES IN DICTIONARY
# d={"a":1,"b":2,"c":3}
# sum=0
# for k,v in d.items():
#     sum=sum+v
# print(sum)


# l=[1,2,3,4,5,6,7,8,9]
# n=eval(input("enter number"))
# for x in l:
#     for y in l:
#         z=int(y)
#         if x+z==n:
#             print(x,z)
# enter number5
# 1 4
# 2 3
# 3 2
# 4 1


