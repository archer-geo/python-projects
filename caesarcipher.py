letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
't', 'u', 'v', 'w ', 'x', 'y', 'z', ]
counter = 0
print("Caesar Shift encryption. Enter a word and a shift key and see your word encrypted! By Rohan Arni (FYI: no punctuation or capital letters thx)")
wordi = input("Enter a word here: ")
cs_input = input("Enter a shift key here: ")
wlist = list(wordi)
len_list = len(wlist)
while counter < len_list:

    indexnum = letters.index(wlist[counter])

    csnum = indexnum + int(cs_input)
    len_list1 = len(letters)
    if (csnum > len_list1 -1):
        csnum = csnum-len_list1
    print(letters[csnum], end = '')
    counter+=1
print("")
