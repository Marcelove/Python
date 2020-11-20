#Basic Calculator. Its pretty self explanatory


print ('Hi, my name is Walter and I will be your calculator today.')
print ('I can do the 5 basic operations of math')
print ('Type the number of the operation you wish to do and press ENTER: \n')
print ('1 - Add')
print ('2 - Subtract')
print ('3 - Multiply')
print ('4 - Division')
print ('5 - Elevate')
op=int (input(' '))

if (op==1):
                print ('You choose Add. Type the number you want to operate with AND PRESS ENTER: \n')
                n1 = int(input(' '))
                
                print ('Now, type the number you want to add to the last number AND PRESS ENTER: \n')
                n2 = int(input(' '))

                z = (n1 + n2)
                print ('Your result is: ', (z))

if (op==2):
                print ('You choose Subtract. Type the number you want to operate with AND PRESS ENTER:\n')
                n1 = int(input(' '))

                print ('Now, type the amount you want to subtract from the last number AND PRESS ENTER: \n')
                n2 = int(input(' '))

                z = (n1 - n2)

                print ('Your result is: ', (z))

if (op==3):
                print ('You choose Multiply. TYpe the number you want to operate with AND PRESS ENTER: \n')
                n1 = int(input(' '))

                print ('Nowm type the amount of times you want to multiply the last number AND PRESS ENTER:\n ')
                n2 = int(input(' '))

                z = (n1 * n2)

                print ('Your result is: ', (z))

if (op==4):
                print ('You choose Division. Type the number you want to operate with AND PRESS ENTER: \n')
                n1 = int(input(' '))

                print ('Now, type the amount of times you want to divide the last number AND PRESS ENTER: \n')
                n2 = int(input(' ' ))

                z = (n1 / n2)

                print ('Your result is: ', (z))

if (op==5):
                print ('You choose to Elevate. Type the number you want to operate with AND PRESS ENTER: \n')
                n1 = int(input(' ' ))

                print ('Now, type the amount of times you want to elevate the last number AND PRESS ENTER: \n')
                n2 = int(input(' '))

                z = (n1 ** n2)

                print ('Your result is: ', (z))


  
                

                


                
                       
       
