def float_checker(y):
    try:
        float(y)
        return True
    except ValueError:
        return False
#float checker for user's inputs

def float_converter(z):
    if float_checker(z) == True:
        z = float(z)
        return z
    elif float_checker(z) == False:
        print('Your input is not valid')
#convert user's inputs to float data type after checking
