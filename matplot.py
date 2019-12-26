from matplotlib import pyplot as plt

# x=[15,56,48,21,32]
# y=[4,2,3,5,6]
# plt.title('table')
# plt.subplot(x,y)
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

a = ['a','b','v']
b = [10, 12, 15]

plt.plot(a,b,'r',label='vinod')

plt.title("Line graph")
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()


# from matplotlib import style
#
# style.use('ggplot')
#
# x = [5, 8, 10]
# y = [12, 16, 6]
#
# x2 = [6, 9, 11]
# y2 = [7, 15, 7]
#
# plt.bar(x, y, color='y', align='center', label='xy' )
# plt.bar(x2, y2, color='c', align='center', label="x1y1")
#
# plt.title('Information')
#
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# plt.show()