#SELECT RANDOM LINES FROM FILE
# import random
# with open("vinod.txt",'r') as v:
#      p=v.readlines()
#      p1=random.choice(p)
# print(p1)

#SELECT ALTERNATIVE LINES
# with open("vinod.txt",'r') as v:
#     p=v.readlines()
#     for x in p[::2]:
#         print(x)


# TO OPEN ANY TYPE OF FILE(doc,mp3,mp4,xlsx,......)
# import os
# os.startfile(r"F:\MOVIES\b.mkv")

#TO COUNT THE NUMBER OF LINES
# c=0
# with open("vinod.txt",'r') as v:
#     d=v.readlines()
# for x in d:
#     c+=1
# print(c)

# TO FIND THE SUM OF NUMBERS IN FILE
# l=[]
# sum=0
# with open("vinod.txt",'r') as v:
#     d=v.read().split()
# for x in d:
#     if x.isdigit():
#         l.append(x)
# for m in l:
#     s=int(m)
#     sum=sum+s
# print(sum)


# TO COUNT THE NUMBER OF DIGITS
# l=[]
# with open ("vinod.txt",'r') as v:
#     d=v.read()
# for s in d:
#     if s.isdigit():
#         l.append(s)
# print(len(l))
# print("the len of words",l)


# TO COUNT THE NUMBER OF WORDS IN FILE
# c=0
# with open("vinod.txt",'r') as v:
#     d=v.read().split()
# for x in d:
#     if x.isalpha():
#         c+=1
# print(c)


#READ MOST COMMON WORD IN FILE
# from collections import Counter
# with open("vinod.txt",'r') as k:
#     v=k.read().split()
# coun=Counter(v)
# most=coun.most_common(1)
# print(most)

#SELECT THE ROW WHICH IS STARTED WITH GIVEN LETTER
# n=input("enter the letter")
# with open("vinod.txt",'r')as k:
#    #v=k.readline()
#     b=k.read()
#     for x in range(1):
#         for y in b[0]:
#             if n==y:
#                 print(b)

# REMOVE THE FILE
# import os
# os.remove('kumar.txt')
# REMOVE THE FOLDER
# os.rmdir(r"C:\Users\vinu\Desktop\delete")
# print("removed successfully")


# r=[]
# with open("inde.txt") as p:
#     s=p.read().split()
# for i in s:
#     if i[0]==[a:z]:
#         print("A",i)


# from collections import Counter
# a="abcdebcbdefcf"
# r=Counter(a)
# print(r)
# OUTPUT:::::::::::::::
#Counter({',': 12, 'b': 3, 'c': 3, 'd': 2, 'e': 2, 'f': 2, 'a': 1})

# print(r['b'])
# OUTPUT:::::3


# from collections import Counter
# with open ("vinod.txt") as v:
#     a=v.readlines()
#     for x in a:
#         res=Counter(x)
#         print(res)
# OUTPUT::::::::::
# C:\Users\vinu\AppData\Local\Programs\Python\Python36\python.exe "D:/PYTHON/DJANGO PROGRAMS/practice/file_handling.py"
# Counter({' ': 14, 's': 7, 'd': 7, '1': 4, '5': 4, 'g': 4, 'a': 3, 'f': 3, '4': 3, '2': 2, '3': 2, 'b': 2, '6': 1, 'k': 1, '\n': 1})
# Counter({'s': 3, 'd': 3, 'f': 2, ' ': 1, 'a': 1, '\n': 1})
# Counter({'a': 2, 'k': 2, 's': 1, 'j': 1, 'h': 1, 'd': 1, '\n': 1})
# Counter({'k': 1, 'j': 1, 'h': 1, 's': 1, 'd': 1, 'a': 1, '\n': 1})
# Counter({' ': 5, 'k': 4, 's': 4, 'd': 4, '4': 3, 'h': 2, '2': 2, '5': 2, 'j': 2, 'a': 1, 'l': 1, '6': 1, '\n': 1})
# Counter({'l': 1, 'h': 1, '3': 1, '5': 1})

#READING A FILE AS CHUNK OF LINES
# from itertools import islice
# n=eval(input("enter number of lines"))
# with open("vinod.txt") as v:
#     res=islice(v,n)
#     for result in res:
#         print(result)
# OUTPUT:::::::
# enter number of lines 2
# 21 1 5 3  safsdggb da 145sdgsdg 54ds 54 21 63 bk sda fsdf
# fsdf sdasd

#Reading a Specific Line from a File
# linenumber=3
# with open("vinod.txt",'r')as v:
#     currentline=1
#     for x in v:
#         if currentline==linenumber:
#             print(x)
#             break
#         currentline+=1
# OUTPUT::::::::::
# sajhkdka

# add="kfkdfdbkfhdsf kjsdbksajdb kjashfkjahf kjskdjhaskjhas kjhsda" \
#     "kjshkjsahfjkhf" \
#     "lksdlkasfhfv"
# with open("vinod.txt",'a') as v:
#     res=v.writelines( add)
#     print(res)

#with open(r"vinod/kumar/sivala",'r') as v:
#    print(v.read())
#OUTPUT::::::::::::
#hello every one

# with open(r"C:\Users\vinu\Desktop\Empty\nothing\hello.txt") as vp:
#     print(vp.read())


# import os
# path="/Empty"
# print(os.path.join(path , "nothing","empty.txt"))
# OUTPUT::::::::::
# helloooooooooooo

# with open("vinod.txt",'r') as v:
#     print(v.read(6))
# OUTPUT::::::::::
#umbrill

# l=[1,2,3,4,5,6,7,8,9]

# if l[::2]:l[1:2]


# with open('add.txt','r')as v:
#     r=v.read()
#     print([r[x:x+3] for x in range(0,len(r),3)])
#  OUTPUT:::::::::::::::
# ['125', ',gf', 'dh,', 'gfd', 'ghh', 'd,1', '8/0', '7/1', '992', ',12', '304', '56A', 'FCs', 'dfs', 'AR\n']


# l=[]
# with open('add.txt','r')as v:
#     r=v.read()
#     res=[r[x:x+1] for x in range(0,len(r),1)]
#     for y in res:
#         if y.isupper():
#             l.append(y)
# print(l)
# #  OUTPUT:::::::::::::::
# ['A', 'F', 'C', 'A', 'R']


# l=[]
# with open('add.txt','r')as v:
#     r=v.read()
#     for x in r:
#         res=x.split()
#         ree=str(res)
#         if ree.isupper():
#             l.append(ree)
# print(l)
# print(type(l))
# OUTPUT:::::::::::::::
# ["['A']", "['F']", "['C']", "['A']", "['R']", "['A']", "['J']", "['A']", "['Y']", "['S']"]


# l=[]
# with open("add.txt",'r')as v:
#     for x in v:
#         res=l.append(x)
# print(l)
# OUTPUT:::::::::::::::

# ['125,gfdh,gfdghhd,18/07/1992,1230456AFCsdfsAR\n', 'dashdkasjh2.sad/sda,sad\n', 'sadkj2\n', '4 sdalkj\n', '45jasAjayJAYs\n', 'sadsaSa\n']




















