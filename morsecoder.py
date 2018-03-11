while True:
    print("Write a sentence in lowercase and see it printed letter by letter! by Rohan Arni. Read readme.txt to see how to exit the program.")
    linput=input("Enter a sentence here:")
    morse_code_dict_key_find = list(linput)
    morse_code_dict = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-',
    'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--',
    'x':'-..-', 'y':'-.--', 'z':'--..' }
    len_list = len(morse_code_dict_key_find)

    counter = 0

    while counter < len_list:
        findkey = morse_code_dict_key_find[counter]
        print(morse_code_dict[findkey], end=" | ")
        counter+=1
