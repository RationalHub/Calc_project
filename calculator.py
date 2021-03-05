import math


def simple_calc():
    a = int(input("enter first no."))
    b = int(input("enter second no."))

    op = str(input("enter the operation(add,subtract,multiply,divide)"))

    if op == "add":
        (print(a + b))
        restart1 = str(input("Retry Simple Calculator?[Y/N]"))
        if restart1 == "Y":
            simple_calc()
        elif restart1 == "N":
            complex_op1 = str(input("Switch To Complex Calculator?[Y/N]"))
            if complex_op1 == "Y":
                comp_calc()
            elif complex_op1 == "N":
                print("Thanks")
    elif op == "subtract":
        (print(a - b))
        restart2 = str(input("Retry Simple Calculator?[Y/N]"))
        if restart2 == "Y":
            simple_calc()
        elif restart2 == "N":
            complex_op2 = str(input("Switch To Complex Calculator?[Y/N]"))
            if complex_op2 == "Y":
                comp_calc()
            elif complex_op2 == "N":
                print("Thanks")

    elif op == "multiply":
        (print(a * b))
        restart3 = str(input("Retry Simple Calculator?[Y/N]"))
        if restart3 == "Y":
            simple_calc()
        elif restart3 == "N":
            complex_op3 = str(input("Switch To Complex Calculator?[Y/N]"))
            if complex_op3 == "Y":
                comp_calc()
            elif complex_op3 == "N":
                print("Thanks")
    elif op == "divide":
        (print(a / b))
        restart4 = str(input("Retry Simple Calculator?[Y/N]"))
        if restart4 == "Y":
            simple_calc()
        elif restart4 == "N":
            complex_op4 = str(input("Switch To Complex Calculator?[Y/N]"))
            if complex_op4 == "Y":
                comp_calc()
            elif complex_op4 == "N":
                print("Thanks")
    else:
        print("COMPLEX OPERATIONS NOT AVAILABLE !")
        complex_op = str(input("Switch To Complex Calculator?[Y/N]"))
        if complex_op == "Y":
            comp_calc()
        elif complex_op == "N":
            restart = str(input("Retry Simple Calculator?[Y/N]"))
            if restart == "Y":
                simple_calc()
            elif restart == "N":
                start_over = str(input("Start Over?[Y/N]"))
                if start_over == "Y":
                    greeting()
                else:
                    print("Thank You !!!!")


def comp_calc():
    print("Hi")
    print("Welcome to the complex calculator!")
    calc = str(input("Which operation do you like to perform?"
                     "[Exponential,Factorial,Reciprocal,Root]"))
    if calc == "Exponential":
        c = int(input("enter the base."))
        d = int(input("enter the power."))
        print(c ** d)
        restart5 = str(input("Retry Complex Calculator?[Y/N]"))
        if restart5 == "Y":
            comp_calc()
        elif restart5 == "N":
            complex_op5 = str(input("Switch To Simple Calculator?[Y/N]"))
            if complex_op5 == "Y":
                simple_calc()
            elif complex_op5 == "N":
                print("Thanks")
    elif calc == "Factorial":
        x = int(input("enter the no."))
        print(math.factorial(x))
        restart6 = str(input("Retry Complex Calculator?[Y/N]"))
        if restart6 == "Y":
            comp_calc()
        elif restart6 == "N":
            complex_op6 = str(input("Switch To Simple Calculator?[Y/N]"))
            if complex_op6 == "Y":
                simple_calc()
            elif complex_op6 == "N":
                print("Thanks")
    elif calc == "Reciprocal":
        z = int(input("enter the no."))
        print(1 / z)
        restart7 = str(input("Retry Complex Calculator?[Y/N]"))
        if restart7 == "Y":
            comp_calc()
        elif restart7 == "N":
            complex_op7 = str(input("Switch To Simple Calculator?[Y/N]"))
            if complex_op7 == "Y":
                simple_calc()
            elif complex_op7 == "N":
                print("Thanks")
    elif calc == "Root":
        fx = int(input("enter the no. to be taken root of"))
        fy = int(input("enter the principle root"))
        print(fx ** (1 / fy))
        restart8 = str(input("Retry Complex Calculator?[Y/N]"))
        if restart8 == "Y":
            comp_calc()
        elif restart8 == "N":
            complex_op8 = str(input("Switch To Simple Calculator?[Y/N]"))
            if complex_op8 == "Y":
                simple_calc()
            elif complex_op8 == "N":
                print("Thanks")
    else:
        print("No Such Function Is Available")
        try_it_again = str(input("Start The Complex Calculator?[Y/N]"))
        if try_it_again == "Y":
            comp_calc()
        elif try_it_again == "N":
            start_over = str(input("Start Over?[Y/N]"))
            if start_over == "Y":
                greeting()
            else:
                print("Thank You !!!!")


def greeting():
    print("Hi")
    print("Welcome To Anhad Jha's Calculator!")
    qwerty = str(input("Which Type Of Operation Do You Want?[Simple,Complex]     "))
    if qwerty == "Simple":
        print("initializing", qwerty, "calculator ........... ")
        simple_calc()
    elif qwerty == "Complex":
        print("initializing", qwerty, "calculator ........... ")
        comp_calc()
    else:
        print("This Type Of Calculator Is NOT Available")
        try_again = str(input("Try Again?[Y/N]"))
        if try_again == "Y":
            greeting()
        else:
            print("Thank You !!!!")


greeting()
