# t=((1,2)+(3,4))
# print(t)
# output:::::::::::::::::::
# (1, 2, 3, 4)

# names = "{2}, {0} and {1}".format('John', 'Bill', 'Sean')
# print(names)
# output:::::::::::::::::::::::::::::
# Sean, John and Bill


#__str__ vs. __repr__  DIFFERENCES

# a="vinod"
# print(str(a))
# print(repr(a))
# output::::::::::::::::::::
# vinod
# 'vinod'

# def vinod():
#     print("hiiiiiiiiii")
#     """jfljfsdjf;lkf;lsdfsdkjfsjf;ljf;ljf"""
# print(vinod.__doc__)
#help(vinod())
# output::::::::::::::::::::::::::::::::::::::::::::::::::
# jfljfsdjf;lkf;lsdfsdkjfsjf;ljf;ljf
# Help on NoneType object:
#
# class NoneType(object)
#  |  Methods defined here:
#  |
#  |  __bool__(self, /)
#  |      self != 0
#  |
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  __repr__(self, /)
#  |      Return repr(self).


# def sq(l1):
#     sqs=list(zip(l1,list(map(lambda x:x**2,l1))))
#     return sqs
# num=[1,2,3,4,5]
# z,z=zip(*sq(num))
# print(z)
# OUTPUT::::::::::::::;
# (1, 4, 9, 16, 25)

