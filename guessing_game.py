
value_assigned = 50
guessValue = int(input("Guess the correct number by choosing any number(1- 100): "))
count = 0
while (guessValue != value_assigned):

    guess = int(input("Enter the correct number: "))
    count = count + 1;
    if (guess == value_assigned):
        print("correct")
        print("You entered a wrong answer" , count , " times" )

     

