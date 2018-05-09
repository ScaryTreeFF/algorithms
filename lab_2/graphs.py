from matplotlib import pyplot as plt
import matplotlib.patches as mpatches


with open('time_binary-a.txt', 'r') as file1:
    time_binary_a = list(map(float, file1.read().split()))

with open('time_ternary-a.txt', 'r') as file2:
    time_ternary_a = list(map(float, file2.read().split()))

with open('time_binary-b.txt', 'r') as file1:
    time_binary_b = list(map(float, file1.read().split()))

with open('time_ternary-b.txt', 'r') as file2:
    time_ternary_b = list(map(float, file2.read().split()))

x_a = [i for i in range(100, 3801, 100)]
x_b = [i for i in range(100, 1901, 100)]

plt.figure(figsize=(14, 7))

plt.subplot(121)
blue_patch = mpatches.Patch(color='blue', label='2-heap')
red_patch = mpatches.Patch(color='red', label='3-heap')
plt.legend(handles=[blue_patch, red_patch])
plt.title('variant A')
plt.xlabel('number of vertices')
plt.ylabel('time in seconds')
plt.plot(x_a, time_binary_a, 'b-', x_a, time_ternary_a, 'r-')
plt.grid(True)

plt.subplot(122)
plt.title('variant B')
plt.xlabel('number of vertices')
plt.ylabel('time in seconds')
plt.plot(x_b, time_binary_b, 'b-', x_b, time_ternary_b, 'r-')
plt.grid(True)

plt.show()
