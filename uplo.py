while True:
	print("Enter 'x' for exit.")
	string = input("Enter any string: ")
	if string == 'x':
		break
	else:
		string_in_uppercase = string.upper()
		print("String in Uppercase =",string_in_uppercase,"\n")
