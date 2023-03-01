n = int(input())
A = list(map(int, input().split()))
first = max(A)
c=A.count(first)
for i in range(c):
    A.remove(first)
print(max(A))
