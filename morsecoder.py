msg = 'this is working'
morse_code_dict_key_find = ['a', 'b', 'c']
morse_code_dict = {'a':'.-', 'b':'-...', 'c':'-.-.'}
len_list = len(morse_code_dict_key_find)

counter = 0

while counter < len_list:
    findkey = morse_code_dict_key_find[counter]
    print(morse_code_dict[findkey])
    counter+=1
