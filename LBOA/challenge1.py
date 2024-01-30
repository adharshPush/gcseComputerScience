'''
subprogram has 3 parmaters
num1, num2, num3
should take in 3 numbers
return highest number

'''

def highest_number(num1, num2, num3):
    try:
        num1=int(num1)
        num2=int(num2)
        num3=int(num3)

        if num1 >= num2 and num1 >= num3:
            return num1
        elif num2 >= num1 and num2 >= num3:
            return num2
        else:
            return num3
    except:
        return "You haven't entered numbers for each comparision"
      
# test your program with different data 
    
# valid
print(highest_number(1, 2, 3))
print(highest_number(3, 2, 1))
print(highest_number(2, 3, 1))
print(highest_number(3, 3, 1))
print(highest_number(3, 3, 3))
    
# border
print(highest_number(1, "2", "3"))

# border
print(highest_number("1", "2", "3"))

# erroneous
print(highest_number(1, "two", "3"))
                                                                                                                                                                                                                                                                        
