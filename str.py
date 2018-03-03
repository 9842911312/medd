while true:
    print("Enter 'x' for exit.")
    string1 = input("Enter First string:")
    string2 = input("Enter Second string:")
    if string1 == 'x':
        break
    else:
        temp = string1
        string1 = string2
        string2 = temp
        print("\n string after swapping:")
        print("First string:", string1)
        print("Second string:", string2,"\n")
