"""
Assignemnt 2: Page 202 answers to Programing Practice Section 
"""
def joke_program():
    # Welcome message
    print("Jokes")

    # list containing questions 
    list_of_jokes = ["What do you call an ant who fights crime ? ","Why did the teddy bear say no to dessert?","Why did the kid cross the playground?","How does a vampire start a letter?","What kind of tree fits in your hand?"]
    # list containing answers 
    list_of_answers = ["A vigilanty!", "Because she was stuffed.","To get to the other slide.","Tomb it may concern...","A palm tree!"]

    # Loop that iterates through the list and displays corresponding answers
    for i in range(len(list_of_jokes)):
            # prints the question 
            print(list_of_jokes[i])
            # Waits for user to press enter
            ask_input = input("Press Enter for the Answer: ")
            # checks if enter is pressed
            if ask_input == "":
                # prints answer
                print("\t"+list_of_answers[i]+"\n")
    # End message
    print("END of Jokes")



def days_left():
    # asks for date 
    date = int(input("Enter today's date(if today is 7th July, enter 7): "))
    # asks for month
    month = input("Enter the present month's name(If July, enter july): ")
    # checks if particular month in list and if so month has 31 days
    if month.lower() in ["january","march","may","july","august","october","december"]:
        days_in_month = 31
    # checks if particular month in list and if so month has 30 days
    if month.lower() in ["april","june","september","november"]:
        days_in_month = 30 
    
    # for feb asks if year is a leap year 
    if month.lower() == "february":
        ask = input("is this a leap year ?:(enter yes or no): ")
        if ask[0].lower() == 'y':
            days_in_month = 29
        else:
            days_in_month = 28
    # finally returns number of days left
    print(f"This month has {days_in_month-date} days left")

#Example of a using operators 
def operator_example():
    a = 5
    print("\n")
    print(a)
    b = 2*a
    print(b)
    c = b - 1 
    print(c)


#Executing function
joke_program()
days_left()
operator_example()