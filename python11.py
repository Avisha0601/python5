import matplotlib.pyplot as plt

x= [1, 2, 3, 4, 5, 6, 7]
y= [7, 2, 6, 4, 2, 5, 1]

plt.plot(x, y, color='cyan', linestyle='dashed', linewidth=3,
         marker='.', markerfacecolor='yellow', markersize=17)

plt.xlim(1,7)
plt.ylim(1,7)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Plot')
plt.show()