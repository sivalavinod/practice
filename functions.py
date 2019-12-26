# def dis(country="norawy"):
#     print("my country is ",country)
# dis("india")
# dis("aus")
# dis()
# dis("USA")
# OUTPUT:::::::::::::
# my country is  india
# my country is  aus
# my country is  norawy
# my country is  USA

# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
# print("\n\nRecursion Example Results")
# tri_recursion(6)
# OUTPUT:::::::::::
#    1
#    3
#    6
#    10
#    15
#    21

# def fun():
#     a,b=1,2
#     if a==1:
#         return True
#     else: return False
#
# fun()
# print(fun())

# def fun(x,l=[]):
#     for a in range(x):
#        l.append(a*a)
#     print(l)
# fun(2)
# fun(3,[3,2,1])
# fun(3)
# OUTPUT::::::::::::::::::::::::::::::
# [0, 1]
# [3, 2, 1, 0, 1, 4]
# [0, 1, 0, 1, 4]


# def fun(z):
#     ax=z.count("a")
#     bx=z.count("b")
#     resa=ax%3
#     resaa=ax//3
#     ao = 0
#     bo=0
#     co,do=0,0
#     for x in z:
#         if x=="a":
#             count+=1
#             if count%3==0:
#                 a=130
#                 ao+=a
#             else:
#                 a=50
#                 ao+=a
#
#         if x=="b":
#             bou+=1
#             if bou%2==0:
#                 b=45
#                 bo+=b
#             else:
#                 b=30
#                 bo+=b
#         if x=="c":
#             c=20
#             co+=c
#         if x=="d":
#             d=15
#             do+=d
#     print(ao+bo+co+do)
# l=["a","b","a","d","b","c"]
# fun(l)

# no=6
# res=no%3
# re=no//3
# print(res,re)

# l=["a","a","b","c","c","d","d"]
# ax=l.count("a")
# bx=l.count("b")
# cx=l.count("c")
# dx=l.count("d")
# res={"a":ax,"b":bx,"c":cx,"d":dx}
# print(res)

# def fun(l):
#     ax=l.count("a")
#     bx=l.count("b")
#     cx=l.count("c")
#     dx=l.count("d")
#     res={"a":ax,"b":bx,"c":cx,"d":dx}
#     print(res)
#     for k,v in res.items():
#         if k=="a":
#             aa=v%3
#             aaa=v//3
#             resa=aa*50
#             resaa=aaa*130
#             x=resa+resaa
#         if k=="b":
#             bb = v % 2
#             bbb = v // 2
#             resb = bb * 30
#             resbb = bbb * 45
#             y = resb + resbb
#         if k=="c":
#             cc=v*20
#         if k=="d":
#             dd=v*15
#     total=x+y+cc+dd
#     print(total)
# l="cdba"
# fun(l)
# OUTPUT:::::::::::::::::::::::::::::::;              a=50  aaa=130
# {'a': 1, 'b': 1, 'c': 1, 'd': 1}                    b=30  bb=45
# 115                                                 c=20
#                                                     d=15


# l=[1,2,3,[4,5,6],7,8,9]
# l2=[]
# c=0
# for x in l:
#     c+=1
#     if c==4:
#         l2.append(l[3][0])
#         l2.append(l[3][1])
#         l2.append(l[3][2])
#     else:
#         l2.append(x)
# print(l2)
# OUTPUT::::::::::::::::::::::::
# [1, 2, 3, 4, 5, 6, 7, 8, 9]






#
# xx=100
# def kumar(y=20):
#     """hfdjhdd
#     jghdhgd
#     gffgff"""
#     # print(y,xx)
#
# kumar(10)
#
# # print(dir())
# # print(kumar.__doc__)
#
# print(help(__doc__))





# def fun():
#     a,b=1,2
#     z=a+b
#     print(z)
# w=fun()
# print(w)
# print(type(w))



