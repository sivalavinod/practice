#
# def fun(l):
#     for x in l:
#         if type(x)==list:
#             fun(x)
#         else:l2.append(x)
#
# # l=[[1,2,3],[4,5,6],[7,8],9]
# l=[1,2,[3,4,[5,6,[7],8],9,[10,11],[12]]]
# l2=[]
# fun(l)
# print(l2)


# l=[1,2,[3,4,[5,6,[7],8],9,[10,11],[12]]]
# l2=[]
# res=[l2.append(x) for x in l ]
# print(l2)


# l=["a"]
# s=set("a",)
# t=("a")
# dict={"a"}
# str="a"
# p=l.__sizeof__()
# q=s.__sizeof__()
# r=t.__sizeof__()
# s=dict.__sizeof__()
# t=str.__sizeof__()
# print("size of list" ,p)
# print("size of set",s)
# print("size of tuple",r)
# print("size of dict",s)
# print("size of str",t)

# def fun():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
# a=fun()
# print(a.__next__())
# print(a.__next__())

# a=[[1,2],[3,4],[5,6]]
# l=[]
# for x in a:
#     l.append(x[0])
#     l.append(x[1])
# print(l)
# OUTPUT::::::::::
# [1, 2, 3, 4, 5, 6]


# f_set1=frozenset({'d','e'})
# f_set=frozenset({'a',f_set1,'b'})
# l=[1,2,3,[4,5,[6,7]]]
# s={1,2,3,f_set}
# t=(1,2,3,(4,5,(6,7)))
# d={"a":"z","b":{"c":"d","e":{"f": "g"}}}
# print(l)
# print(s)
# print(t)
# print(d)

# di={5.1:"a",True:"re",('a','d'):"as",{'a','b'}:'xz',['a','sa']:'sd'}
# print(di)

# print(hash(l))
# print(hash(s))
# print(hash(t))
# s='asd'
# print(hash(s))


# a=()
# print(hash(a))

# def vinod():
#     for x in range(10,20):
#         print(x)
#         print(type(x))
# vinod()



# #FIND THE BIGGEST NUMBER IN NESTED LIST
# l2=[]
# def big(l1):
#     for i in l1:
#         if type(i)==list:
#             big(i)
#         else:
#             l2.append(i)
# l1=[7,9,[12,5,[30,[48,[199],99],15],17],7]
# big(l1)
# print(max(l2))

# import json
# x={"name":"vinod","age":25,"sal":125000}
# y=json.dumps(x)
# print(y)
# z=json.loads(y)
# print(z)


# ========================================================================================================





# a=range(10,20)
# print(type(a))

# l={1:{1,2,5,6,4}}
# l1={"a":{1,5,'k','6k',5.5}}
# l2={1.5:{1,"5",'6k','6g','dfg',12.5}}
#  l3={(1,5,6):{'df',5,'fdg','fgeer','dgdg',},"ra":"sa"}
# # l4={{1,5,6}:{'df',5,'fdg','fgeer','dgdg',True}}
# l5={range(1,2,5):{'df',5,'fdg','fgeer','dgdg',True}}

# print(type(l))
# print(type(l1))
# print(type(l2))
# print(type(l3))
# # print(type(l4))
# print(type(l5))

# print(l3.values())
# print(l[1])
# print(l1['a'])
# print(l2[1.5])
# print(l3[(1,5,6)])
# print(l5[range(1,2,5)])


# f2=frozenset({6,7})
# f=frozenset({4,5,f2,8,9})
#
# l={1,2,3,f,10}
# print(l)

# a=list(input("enter the values"))
# b=tuple(a)
# print("type of a:",type(a))
# print("type of b:",type(b))


# for x in range(1,6):
#     for y in range(5,x,-1):
#         print(" ",end="")
#     for z in range(x):
#         print("*",end="")
#     print()

# l=[1,2,3,4,5,6,7,8,9,1,2,3]
# y=5
# for x in l:
#     if x==y:
#         pass
#     else:
#         print(x)
#
#
# l=[1,2,3,4,5,6,7,8,9,1,2,3]
# y=5
# for x in l:
#     if x==y:
#         continue
#     else:
#         print(x,end="")



# for x in range(100):
#     print(x)

# a=1
# y=int(input("enter no"))
# while a<y:
#     print(a)
#     a+=1

# a="vinodranga"
# print(a[2:8])

# print(a[2],end="")
# print(a[3],end="")
# print(a[4],end="")
# print(a[5],end="")
# print(a[6],end="")
# print(a[7],end="")

# a=2+7
# b="vin"+"od"
# print(a)
# print(b)

#
# a=["vinod",1,25]
# b=["kumar",2,32]
# c=["sivala",3,54]
# z=zip(a,b,c)
# print(list(z))
#
# r,s,t=zip(*z)
# print(list(r))


# t=zip(a,w,r)
# print(list(t))
# l,k,j=zip(*t)
# print(l)


# s=["ranga is going to 45 54k python class"]
# z=s.replace('class','ClAss')
# print(z)

# l=str(s)
# s=l.split()
# for x in s:
#     if x.isalnum():
#         print(x)




# a="r"
# s="v"
# if s<a:
#     print("a is a big")
# else:print("s is a big")
# print("a",ord(a))
# print("s",ord(s))

# s=('vinodrangamani')
# a="vinod is.a GOOD. boY.Sad.ewet.gfgfdg gfgdf fDFfdg "
# l=a.capitalize()
# print(l,end=" ")

# a=eval(input("enter"))
# print(type(a))


