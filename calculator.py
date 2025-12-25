num1 = int( input ( " Enter number 1 : "))
num2 = int( input ( " Enter number 2 : "))
print ( " Addition (a), Subtraction (s), Multiply (m), Division (d)" )
action = str( input ( " Enter your choice : "))
if action =="a" :
    print(f'{num1} + {num2} = {num1+num2}')
elif action == "s" :
    print(f'{num1} - {num2} = {num1-num2}')
elif action == "m" :
    print(f'{num1} * {num2} = {num1*num2}')
else :
    print(f'{num1} / {num2} = {num1/num2}')