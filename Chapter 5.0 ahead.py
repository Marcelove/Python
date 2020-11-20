#IF statement

#x = int(input(''))
#if x < 0:
    #pass         #'Pass' juts skips the execution. Its normally used to keep in-
                 #-blank something that i want to write after


#if x%2 == 0:
    #print ('X is even')
#else:
    #print ('X is odd')


#x = int(input('number:'))
#y = int(input('number:'))

#if x > y:
    #print ('{} is bigger than {}'.format(x, y))

#elif x < y:                                          #elif makes python only check one of the statements. its faster
                                                     # Even if more than one condition is true, only the ﬁrst true branch executes.(THink Python)
    #print('{} is bigger than {}'.format(y, x))

#else:                                           #not obligatory to use an else. But if you do so, it has to be at the end
    #print('x and y are equal')
                                                     
#n = int(input('n:'))

#def countdown(n):
    #if n == 0:
    #    print ('0')
#    else:
#        print (n)
#        countdown(n-1)                          #this goes back to the beginning

#countdown(n)

#x = int(input('x='))

#def countdown(x):
#    if x ==0:
#        print ('0')
#    else:
#        print (x)
#        countdown(x-1)

#countdown(x)

#x = input('frase:')
#y = int(input('número de repetições:'))

#def Hello(y):
    #print (x)
    #Hello(y-1)

#Hello(y)

#def infinity():                               #Take a look at the error message.
#    infinity()

#infinity()

#Cheking a triangle
#print ('HELLO, LETS SEE IF YOU CAN FORM A TRIANGLE WITH YOUR 3 STICKS')
#fi =  int(input('Type the length of the first stick:\n'))
#se =  int(input('Type the length of the second stick:\n'))
#th =  int(input('Type the length of the third stick:\n'))

#if (fi+se) < th or (fi+th) < se or (th+se) < fi:
#    print ('NOt a triangle')

#else:
#    print ('Yes, a triangle!')

#Drawing a Pyramid
import turtle

bob = turtle.Turtle()

bob.penup()
bob.setposition(-500, 0)
bob.pendown()
bob.lt(90)
bob.speed(0)

for i in range(20):
    bob.fd(10)             #10
    bob.rt(90)             #90
    bob.fd(10)
    bob.lt(90)

bob.rt(180)

for i in range(20):
    bob.fd(10)
    bob.lt(90)
    bob.fd(10)
    bob.rt(90)

bob.rt(90)
bob.fd(400)


    


