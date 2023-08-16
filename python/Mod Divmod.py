# Enter your code here. Read input from STDIN. Print output to STDOUT
# Take two integer inputs
num1 = int(input())
num2 = int(input())

quotient, remainder = divmod(num1, num2)

result_string = f"{quotient}\n{remainder}\n({quotient}, {remainder})"
print(result_string)
