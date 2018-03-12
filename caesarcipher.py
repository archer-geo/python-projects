letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
't', 'u', 'v', 'w ', 'x', 'y', 'z' ]
cs = 1
counter = 0

word = 'bad'
wlist = list(word)
len_list = len(wlist)
while counter < len_list:

    indexnum = letters.index(wlist[counter])

    csnum = indexnum + cs
    print(letters[csnum], end = '')

    counter+=1
print("")
