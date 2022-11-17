import matplotlib.pyplot as plt

left = [1, 2, 3, 4, 5]

height = [10, 24, 36, 42,5]

tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label = tick_label,
        width = 0.6, color = ['violet', 'indigo', 'blue', 'green', 'yellow'])

plt.xlabel('x__axis')
plt.ylabel('y__axis')

plt.title('Bar chart')
plt.show()