score=int(input('Enter total score: '))
if score>=80 and score<=100:
    grade='A' 
    print(f'This student got a grade {grade} in the course.')
elif score>=60 and score<=79:
    grade='B'
    print(f'This student got a grade {grade} in the course.')
elif score>=50 and score<=59:
    grade='C'
    print(f'This student got a grade {grade} in the course.')
elif score>=40 and score<=49:
    grade='D'
    print(f'This student got a grade {grade} in the course.')
elif score>=25 and score<=39:
    grade='E'
    print(f'This student got a grade {grade} in the course.')
elif score>=0 and score<=24:
    grade='F'
    print(f'This student got a grade {grade} in the course.')    
else:
    print('Invalid score')    
    

