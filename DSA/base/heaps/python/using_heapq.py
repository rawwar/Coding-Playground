import heapq

values = [5, 1, 3, 7, 4, -2]

heapq.heapify(values)

print(values)

heapq.heappush(values, 5)
print(values)

smallest = heapq.heappop(values)

print("Smallest:", smallest)
print(values)

n_smallest = heapq.nsmallest(3, values)
print("Smallest 3:", n_smallest)
print(values)

n_largest = heapq.nlargest(3, values)
print("3 largest:", n_largest)
print(values)

lst1 = [1, 2, 6]
lst2 = [2, 5, 7, 100]
lst3 = [6, 9]

res = heapq.merge(lst1, lst2, lst3)
print(list(res))