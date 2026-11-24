string = input("Enter a word: ")
length_of_string = len(string)
reverse = " "
for count in range ( 0, length_of_string):
    reverse = string[count] + reverse 


print(reverse)

