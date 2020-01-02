# d={"a":1,"b":2,"c":3}
# d1={"a":"x","b":"y","c":"z"}
# res=dict((d1[key],value) for key,value in d.items())
# print(res)
# output::::::::::::::::::::::::::::
# {'x': 1, 'y': 2, 'z': 3}


# a=[["a","s"],["d","f"],["q","e"]]
# l=[]
# for x in a:
#     l.append(ord(x[0])+ord(x[1]))
# print(sum(l))
# OUTPUT:::::::::::::::::
# 628


# def cl():
#     v=int(input("enter value"))
#     b=int(input("enter value"))
#     print(v+b)
# d={"a":1,3.6:2,(1,2):cl(),True:4,1:24,0:12}
# print(d)
# OUTPUT:::::::::::::::
# enter value4
# enter value5
# 9
# {'a': 1, 3.6: 2, (1, 2): None, True: 24, 0: 12}



# TWO WAYS TO DECLARE DICTIONARY
# d=dict(a=1,b="dfsdf",vK=2.5,c=[1,2,3])
# print(d)
# OUTPUT:::::::::::::
# {'a': 1, 'b': 'dfsdf', 'vK': 2.5, 'c': [1, 2, 3]}
# BUT IN THIS key MUST BE CHARACTER vslue CAN BE ANYTHING

# another way
# d1={"a":1,2:"ssf",1.5:[1,2,3],True:(1,2,3),}
# print(d1)


# d=dict(a= dict(b=dict(c=123)))
# print(d)
# d1={"a":{"b":{"c":123}}}
# print(d1)
# OUTPUT:::::::::::::::
# {'a': {'b': {'c': 123}}}
# {'a': {'b': {'c': 123}}}

# d1={"a":1,2:"ssf",1.5:[1,2,3],True:(1,2,3)}
# for x in d1:
#     print(d1[x])
# print(d1.values())
# OUTPUT:::::::::::::::::
# 1
# ssf
# [1, 2, 3]
# (1, 2, 3)
# dict_values([1, 'ssf', [1, 2, 3], (1, 2, 3)])


# a={5:"a",2:"b",3:"c"}
# a[1]=a.pop(5)
# print(a)
# OUTPUT:::::::::
# {2: 'b', 3: 'c', 1: 'a'}

# a=dict(q="c",w="e",e="r")
# b=dict(a="A",b="B",c="C")
# d=dict((a[key],value) for key,value in b.items())
# print(d)
# OUTPUT:::::::::::::::::
# we get an error because these operation is not done in this type of dict declaration a=dict(q="c",w="e",e="r")

# myDict = {1:"one",2:{3:"three",4:"four"}}
# myDict[2][5] = myDict[2].pop(3)
# print (myDict)
# print(len(myDict))
# Output::::::::::::::::::::::::::::::::::::::
# {1: 'one', 2: {3: 'three', 5: 'four'}}
# 2

# d={1:"a",2:"b",3:"c",4:{5:"d"},5:"e"}
# d[2][10]=d[2].pop(4)
# d[4][0]=d[4].pop[0]
# print(d)

# for x in d:
#     print(x.values)


# d = {1:2,3:4}
# p=dict(a=12,b=14)
# d=dict(zip(p,list(d.values())))
# print(d)
# output:::::::::::::::::::::::::::::::::
# {'a': 2, 'b': 4}

# d = {1:2,3:4,5:6}                                         # it is not possible because keys in both dict are not same
# d1=dict(a="A",b="B",c="C")
# d={"a":1,"b":2,"c":3}                                     # it is possible bcz both dict(d,d1) have same keys BUT KEYS MUST BE CHARACTERS
# d1={"a":"x","b":"y","c":"z"}
# d1=dict((d1[key],value) for key,value in d.items())      #output in dict format
# print(d1)
# OUTPUT:::::::::::::::::::::::::::::::::
# {'x': 1, 'y': 2, 'z': 3}                              #DICT format

# d={"a":1,"b":2,"c":3}
# d1={"a":"x","b":"y","c":"z"}
# d1={(d1[key],value) for key,value in d.items()}     #output in TUPLE format
# print(d1)
# OUTPUT:::::::::::::::::::::::::::::::::
# {('z', 3), ('x', 1), ('y', 2)}                      #set format (un order)


# a={"a":"b","c":"d","e":"f"}
# b={"g":"h","i":"j","k":"l"}
# c={"x":"x"}
# a.update(b)                                 #to merge TWO dictionaries
# print(a)
# OUTPUT:::::::::::::::::::::::::::::::::
# {'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h', 'i': 'j', 'k': 'l'}


# def fun(a,b,c):
#     res={**a,**b,**c}                        # to merge TWO OR MORE DICTs
#     return res
# a={"a":"b","c":"d","e":"f"}
# b={"g":"h","i":"j","k":"l"}
# c={"x":"x"}
# print(fun(a,b,c))
# OUTPUT:::::::::::::::::::::::::::::::
# {'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h', 'i': 'j', 'k': 'l', 'x': 'x'}



# d={"code":["cc","ce","ha"]}
# c={"cc":"cyber","ce":"cage","ha":"heat"}
# print(list("".join(v) for k,v in c.items()))
# print(",".join([c[i] for i in d['code']]))
# OUTPUT:::::::::::::::::::::::::::::::::::::::::
# ['cyber', 'cage', 'heat']
# cyber,cage,heat


# a={"a":1,"b":"c"}
# b={"d":"55.5",6.2:"v"}
# z=[*a,*b]                           # to print all keys
# res=[{**a,**b}]                     # to print both key and value from all
# print(res)
# print(z)
# for k,v in a.items():
#     print(k)
#
# s=b.keys()
# print(s)
#
# OUTPUT:::::::::::::::
# [{'a': 1, 'b': 'c', 'd': '55.5', 6.2: 'v'}]
# ['a', 'b', 'd', 6.2]
# a
# b
# dict_keys(['d', 6.2])


# d={"+":"a","-":"b","*":12,"/":12.5,1:"asd"}
# print(type(d))                     # <class 'dict'>
# print(type(d.items()))             # <class 'dict_items'>
# print(d)                           # {'+': 'a', '-': 'b', '*': 12, '/': 12.5}
# print(d.items())                   # dict_items([('+', 'a'), ('-', 'b'), ('*', 12), ('/', 12.5)])
# print(d.keys())                    # dict_keys(['+', '-', '*', '/'])
#print(d[+])                         # SHOWS ERROR    INVALID SYNTAX

# d={'a':"A","b":"B","c":"C","d":"D"}
# d[2]["z"]=["Z"].pop(2)
# print(d)
