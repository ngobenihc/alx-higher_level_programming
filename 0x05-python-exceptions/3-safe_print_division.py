#!/usr/bin/python3

def safe_print_division(a, b):
    
    #divides two integers and prints the result catches divide by zero exception
    
    try:
        divi = a / b
    except:
        divi = None
    finally:
        print("Inside result: {}".format(divi))
    return divi