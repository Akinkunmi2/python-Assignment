
number = int(input("Enter any number: "))
main_number = number
reversed_number= 0
while(number > 0):
    value = number % 10
    reversed_number = reversed_number * 10 + value
    number = number //10;

if(reversed_number == main_number):
    print("The number you entered is a palindrome");



else:
    print("The number you entred is not a palindrome")





