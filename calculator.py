operator= input('Enter the operator: ')
num_1= float(input('Enter first value: '))
num_2= float(input('Enter second value: '))
import math
if operator=='+':
    result=num_1 + num_2
    print(round(result,2))
elif operator=='-':
    result=num_1 - num_2
    print(round(result,2))
elif operator=='*':
    result= num_1* num_2
    print(round(result,2))
elif operator=='/':
    result= num_1/num_2
    print(round(result,2))
elif operator=='sqrt':
    result=math.sqrt(num_1)
    print(round(result,2))
elif operator=='log10':
    result=math.log10(num_1)
    print(round(result,2))
elif operator=='sin':
    result=math.sin(num_1)
    print(round(result,2))
elif operator=='cos':
    result=math.cos(num_1) 
    print(round(result,2)) 
elif operator=='tan':
    result= math.tan(num_1)
    print(round(result,2)) 
elif operator=='**':
    result= (num_1)**(num_2) 
    print(round(result,2))
else:
    print('math error!')          
                    