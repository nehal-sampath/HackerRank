n = int(input())
a = list(map(int, input().split()))

result = 0
for i in a:
    result = result ^ i       #do the bit operations
print(result)
