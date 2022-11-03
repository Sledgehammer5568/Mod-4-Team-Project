# Emanuel Ramos, Jose Lopez, and David Serna
# Options 1 - 4 are written by Emanuel ramos, last edited on 11/02/2022
# Options 5 - 8 are written by David Serna, last edited on 10/29/2022
# 11/06/2022
#
# Description: give a user choices and provide them with something
#

IN = int(input("""Hello What would you like to do today?
1. Get a nice message 100 times!
2. Draw a triangle or square using turtle
3. Do simple math!
4. Create a password
5. option 5
6. option 6
7. option 7
8. option 8\n"""))

if IN == 1:  # this option prints out a greeting using the users name
    name = input("What is your name?\n")
    for names in range(1, 101):
        print("Hello, I hope you have a wonderful day!", name)

elif IN == 2:  # this option allows the user to draw a triangle or a square of different colors
    import turtle

    Object = turtle.Turtle()

    length = int(input("What is the length of the sides?\n"))
    color = input("What color do you want the object to be filled with?\n")
    shape = int(input("""What shape would you like to make?
    1. Triangle
    2. Square\n"""))

    if shape == 1:  # this option draws a triangle
        canvas = turtle.Screen()
        Object.speed(1)  # you can change the speed of the animation here (1 - 10)
        Object.shape("turtle")  # this changes the shape of the turtle
        Object.fillcolor(color)
        Object.begin_fill()
        for triangle in range(3):
            Object.forward(length)
            Object.left(120)
        Object.end_fill()
        print("click on screen to exit")
        canvas.exitonclick()

    else:  # this option draws a square
        canvas = turtle.Screen()
        Object.speed(1)  # you can change the speed of the animation here (1 - 10)
        Object.shape("turtle")  # this changes the shape of the turtle
        Object.fillcolor(color)
        Object.begin_fill()
        for square in range(4):
            Object.forward(length)
            Object.left(90)
        Object.end_fill()
        print("click on screen to exit")
        canvas.exitonclick()

elif IN == 3:  # this option is just a simple calculator to Multiply or Divide, and Add or subtract
    # the user gets to choose what type of math problem he would like to do
    choice = int(input("""What would you like to do?
    1. Multiply
    2. Divide
    3. Add
    4. Subtract\n"""))
    if choice == 1:  # this choice multiplies two inputted numbers
        num1 = int(input("What is your first number?"))
        num2 = int(input("what is your second number?"))
        Final_Answer = num1 * num2
        print("This is your first number:", num1)
        print("This is your second number:", num2)
        print("This is the answer:", Final_Answer)
    elif choice == 2:  # this choice divides two inputted numbers
        num1 = int(input("What is your first number?"))
        num2 = int(input("what is your second number?"))
        Final_Answer = num1 / num2
        print("This is your first number:", num1)
        print("This is your second number:", num2)
        print("This is the answer:", int(Final_Answer))
    elif choice == 3:  # this choice adds two inputted numbers
        num1 = int(input("What is your first number?"))
        num2 = int(input("what is your second number?"))
        Final_Answer = num1 + num2
        print("This is your first number:", num1)
        print("This is your second number:", num2)
        print("This is the answer:", Final_Answer)
    elif choice == 4:  # this choice subtracts two inputted numbers
        num1 = int(input("What is your first number?"))
        num2 = int(input("what is your second number?"))
        Final_Answer = num1 - num2
        print("This is your first number:", num1)
        print("This is your second number:", num2)
        print("This is the answer:", Final_Answer)
    else:
        print("incorrect input please try again")

elif IN == 4:  # this is a password generator found at
    # https://www.geeksforgeeks.org/create-a-random-password-generator-using-python/
    # the code was edited by Emanuel Ramos
    import string
    import random

    # Getting password length
    length = int(input("Enter password length: "))

    print('''Choose character set for password from these :
    1. Letters
    2. Digits
    3. Special characters
    4. Exit''')

    characterList = ""

    # Getting character set for password
    while True:
        choice = int(input("Pick a number "))
        if choice == 1:

            # Adding letters to possible characters
            characterList += string.ascii_letters
        elif choice == 2:

            # Adding digits to possible characters
            characterList += string.digits
        elif choice == 3:

            # Adding special characters to possible
            # characters
            characterList += string.punctuation
        elif choice == 4:
            break
        else:
            print("Please pick a valid option!")

    password = []

    for i in range(length):
        # Picking a random character from our
        # character list
        randomchar = random.choice(characterList)

        # appending a random character to password
        password.append(randomchar)

    # printing password as a string
    print("The random password is " + "".join(password))


elif IN == 5:
    print("SOMETHING 5")

elif IN == 6:
    print("SOMETHING 6")

elif IN == 7:
    print("SOMETHING 7")

elif IN == 8:
    print("SOMETHING 8")

else:
    print("Wrong Input!")
