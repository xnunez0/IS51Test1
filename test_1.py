"""
The program is trying to determine the best payment option. 
The first payment option is for $100 a day for 10 days
The second payment option is for $1 the first day, $2 the second day and so on until it has reached 10 days.
Find a solution to see which option produces the most money at the 10th day or see if they are the same.

Fuction1 will output 100 * 10

Function2 will loop 10 times, each time doubling, and add the amount to the total

If the total amounts ae equal, we output to the user, "Option 1 and Option 2 are the same"
If option 1 is better, we output to the user, "Option 1 is better"
If option 2 is better, we output to the user, "Option 2 is better"
"""

"""
#   Option1 
     Return 100 * 10 

#   Option2 
    amount = 1 
    list1 = []
    loop 10 times 
        add amount to list1 
        amount *= 2
    sum = sum of all items in the loop
    return sum

#   Main
     Var1= Option1
     Var2= Option2

    if Var1 = Var2
        "option 1 and option 2 are the same"
    if Var1 < Var2 
        "Option 2 is better"
    if Var2 < Var1
        "Option 1 is better"

    Main
    """

def option1():
    return 100 * 10

def option2(): 
    amount = 1 
    list1 = []
    for i in range (0, 10):
        list1.append(amount)
        amount *= 2
    print("list1", list1)
    total = sum(list1) 
    return total

def main():
    answer = ""
    var1 = option1()
    var2 = option2()
    print("from main: var1", var1, 'var2', var2)
    if var1 == var2:
        answer = "option 1 and option2 are the same"
    if var1 < var2:
        answer = "option 2 is better"
    if var2 < var1:
        answer = "option 1 is better"
    print(answer)


main()


