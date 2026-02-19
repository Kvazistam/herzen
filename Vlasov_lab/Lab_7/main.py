# import make_image
#
# if __name__ == '__main__':
#     make_image.app.run(debug=True)


# n = int(input())
# if n < 1 or n > 10 ** 7:
#     print("NO")
# x = str(input())
# l = x.split()
# if len(l) != n:
#     print("NO")
# int_l = [int(i) for i in l]
# sum_l = sum(int_l)
# if sum_l % 2 == 0:
#     print("YES")
# else:
#     print("NO")

# days = {"MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6, "SUN": 7}
# first_week = [days[i] for i in str(input()).split()]
# second_week = [days[i]+7 for i in str(input()).split()]
# third_week = [days[i]+14 for i in str(input()).split()]
# fourth_week = [days[i] + 21 for i in str(input()).split()]
# first_week.sort()
# second_week.sort()
# third_week.sort()
# fourth_week.sort()
# month = first_week + second_week + third_week + fourth_week + [29]
# delta = 0
# start =0
# new_start = 1
# end = 0
# for i in range(len(month)):
#     new_delta = month[i]-new_start
#     if new_delta>delta:
#         delta = new_delta
#         end = month[i]-1
#         start=new_start
#     new_start = month[i]+1
#
# print(start, " ", end)
# class Vending:
#     def __init__(self, k):
#         self.change = 0
#         self.min_candy = k
#         self.min_cost = 3 * k
#
#     def selling(self, coin):
#         self.change += coin
#         if self.change >= self.min_cost:
#             delta = self.change - self.min_cost
#             a = delta // 3
#             self.change -= (self.min_candy + a)*3
#             return self.min_candy + a
#         else:
#             return 0
#
# l = input().split()
# n = int(l[0])
# k = int(l[1])
# a = int(l[2])
# m = int(l[3])
#
# my_vending = Vending(k)
#
#
#
# def lcg(e):
#     return (a * e + 11) % m
#
#
# def generator(seed):
#     sequence = []
#     candies = 0
#     coins = 0
#     while True:
#         seed = lcg(seed)
#         coin = (abs(seed % 3 - 1) * 5 + abs(seed % 3) * 2) % 8
#         sequence.append((abs(seed % 3 - 1) * 5 + abs(seed % 3) * 2) % 8)
#         candies += my_vending.selling(coin)
#         coins +=1
#         if candies >= n:
#             print(coins)
#             return candies
#
# generator(0)

# def min_moves_to_make_practical(n, m, intervals):
#
#     centers = [(i[0] + i[1]) / 2  for i in intervals]
#     centers.sort()
#     median_center = centers[m // 2]
#     print(median_center)
#
#     total_moves = 0
#     for center, interval in zip(centers, intervals):
#         if median_center < interval[0]:
#             total_moves +=
#         return total_moves
l=[]
for i in range(4):
    for j in range(4):
        for k in range(4):
            for m in range(4):
                l.append([i,j,k,m])
count=0
def proverka(lst):
    if lst[0]==lst[1]==lst[2]==lst[3]:
        return True
    unique_fruits = []
    for fruit in lst:
        if fruit not in unique_fruits:
            unique_fruits.append(fruit)
    if unique_fruits == lst:
        print(lst)
        return True

for i in l:
    if proverka(i):
        count+=1
print(count)

# Чтение входных данных
n, m = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(m)]

# Вычисление и вывод результата
print(min_moves_to_make_practical(n, m, intervals))
print(intervals)


# l = input().split()
# n = int(l[0])
# m = int(l[1])
# pairs = []
# for i in range(m):
#     input_l = input().split()
#     a = int(input_l[0])
#     b = int(input_l[1])
#     pairs.append((a,b))
# print(pairs)
#
# variant = []
# def dfs (int v) :
#   used[v] = 1;
#   for (size_t i=0; i<g[v].size(); ++i) {
#     int to = g[v][i];
#     if (used[to] == 0) {
#       p[to] = v;
#       dfs (to);
#     }
#   else if (used[to] == 1)
#     cycle=true;
#   }
#   used[v] = 2;
# }

# from collections import deque, defaultdict
#
#
# def t_sort(n, edges):
#
#     graph = defaultdict(list)
#     in_degree = {i: 0 for i in range(1, n + 1)}
#
#     for a, b in edges:
#         graph[a].append(b)
#         in_degree[b] += 1
#
#     queue = deque([node for node in in_degree if in_degree[node] == 0])
#     sorted_order = []
#
#     while queue:
#         node = queue.popleft()
#         sorted_order.append(node)
#
#         for neighbor in graph[node]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
#
#     if len(sorted_order) == n:
#         return True, sorted_order
#     else:
#         return False, []
#
#
#
# n, m = map(int, input().split())
# edges = [tuple(map(int, input().split())) for _ in range(m)]
#
#
# possible, order = t_sort(n, edges)
#
# if possible:
#     print("Yes")
#     print(" ".join(map(str, order)))
# else:
#     print("No")