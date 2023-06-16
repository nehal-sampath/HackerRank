def swap_case(s):
    k=[]
    for i in s:
        if i.islower():
            k.append(i.upper())
        elif i.isupper():
            k.append(i.lower())
        else:
            k.append(i)
    return "".join(k)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
