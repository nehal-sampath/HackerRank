n = int(input())
arr = []

left_diag = right_diag = 0

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

for i in range(n):
    left_diag += arr[i][i]
    right_diag += arr[i][n-1-i]

print(abs(left_diag - right_diag))
