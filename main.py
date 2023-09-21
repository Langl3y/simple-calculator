from float_functions import *

operator_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
#operator dictionary

print('A SIMPLE CALCULATOR')
#title

op_one = (input('Enter your first operand:'))
op_two = (input('Enter your second operand:'))
oper = (input('Choose a math operation (+,-,*,/): '))
#user's input 

if type(float_converter(op_one)) == float and type(float_converter(op_two)) == float:  #checking inputs
    converted = float_converter(op_one)   #convert operand 1
    converted_two = float_converter(op_two) #convert operand 2
    print('Result:', converted , oper , converted_two , '=' , operator_dict[oper](converted,converted_two))
#print the result of the calculator



