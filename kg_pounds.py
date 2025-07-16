unit= input('Enter weight unit in kg or lbs: ')
weight= float(input('Enter the weight: '))
if unit.lower()== 'kg':
    result=(weight*2.20462)
    print(f'{round(result,2)}lbs')
elif unit.lower()=='lbs':
    result= (weight/2.20462)
    print(f'{round(result,2)}kg')
else:
    print('Invalid unit!')    
