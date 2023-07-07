def plusMinus(arr):
    count_minus = 0
    count_plus = 0
    count_zero = 0
    for i in arr:
        if i > 0:
            count_plus += 1
        elif i < 0:
            count_minus += 1
        else:
            count_zero += 1

    n = len(arr)
    ratio_plus = count_plus / n
    ratio_minus = count_minus / n
    ratio_zero = count_zero / n

    print("{:.6f}".format(ratio_plus))
    print("{:.6f}".format(ratio_minus))
    print("{:.6f}".format(ratio_zero))      # formatting 


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
