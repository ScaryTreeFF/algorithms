from matplotlib import pyplot as plt


with open('time_prim.txt', 'r') as file1:
    time_prim = list(map(float, file1.read().split()))

with open('time_kruskal.txt', 'r') as file2:
    time_kruskal = list(map(float, file2.read().split()))

n = [i for i in range(100, 10001, 100)]

plt.plot(n, time_prim, 'b-')
# plt.plot(n, time_kruskal, 'r-')
plt.grid(True)
# plt.yscale('symlog')
# plt.axis([0, 10001, 0, 100])

plt.show()
# print(min(time_prim))
# print(max(time_kruskal))
