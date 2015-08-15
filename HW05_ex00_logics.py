#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    while True: # keeps the loop running until a valid entry is evaluated
        try:
            num = int(raw_input("Enter an integer:\n>"))
            if (num % 2 == 0):
                print "The number you entered is even."
                return None
            else:
                print "The number you entered is odd."
                return None 
        except: # handles exceptions for all non int entries
            print "Bad entry, try again."
            continue

        

    
def ten_by_ten():
    for num in range(1, 101):   
        if num % 10 != 0:   # This loop ensures only 10 numbers are printed on a single line
            if num < 10:
                print str(num) + " ", # nums 1-9 need a space added to preserve grid format
            else:
                print num,
        else:
            print num
            continue


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    list_ = []
    list_entries = 0

    while True:
        entry = raw_input("Enter numbers to be average.  Type 'done' to finish.\n>")
        if entry == 'done':
            try:    # If the first entry is 'done' division by zero crashes function
                return sum(list_[:]) / list_entries # average all numbers added to list
            except:
                print "You need to enter at least one number." 
        else:
            try:
                list_.append(int(entry)) 
                list_entries += 1
            except:
                print "Enter an integer."

    

##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print find_average()
if __name__ == '__main__':
    main()
