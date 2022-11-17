import matplotlib.pyplot as plt


x = [1,2,3,4,5,6,7]

y = [5,7,2,6,3,1,8]

plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='.', markerfacecolor='purple', markersize=17)

plt.ylim(1,9)
plt.xlim(1,9)

plt.xlabel('x~axis')
plt.ylabel('y~axis')

plt.title('plot**x_axis vs y_axis')

plt.show()