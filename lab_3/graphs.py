from matplotlib import pyplot as plt

with open('time_prim.txt', 'r') as file1:
    time_prim = file1.read().split()

with open('time_kruskal.txt', 'r') as file2:
    time_kruskal = file2.read().split()

n = [i ** 2 / 10 for i in range(100, 10001, 100)]

plt.plot(n, time_prim, 'b-', n, time_kruskal, 'r-')
plt.show()
