# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
s_ar = input().split()

A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in s_ar]))
