def mutate_string(string, position, character):
    l=list(s)
    l[5]='k'
    str1="".join(l)
    string=string[:position]+character+string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
