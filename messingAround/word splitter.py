
MyString = input("Enter a word: ")
i = len(MyString)
print("String Length:",i)

if i%2 == 0:
    str1 = MyString[0:i//2]
    str2 = MyString[i//2:]
    print("String First Half :",str1)
    print("String Second Half:",str2)

else:
    str1 = MyString[0:(i//2+1)]
    str2 = MyString[(i//2+1):]
    print("String First Half :",str1)
    print("String Second Half :",str2)