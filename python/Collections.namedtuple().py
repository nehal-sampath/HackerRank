# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
headers = input().split()
marks_index = headers.index('MARKS')
total_marks = 0

for _ in range(N):
    row = input().split()
    total_marks += int(row[marks_index])

average = total_marks / N
print(average)
