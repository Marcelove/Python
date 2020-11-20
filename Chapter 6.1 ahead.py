#Exercise 6.1. Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.

#x = float(input('first value:'))
#y = float(input('second value:'))

#if x > y:
#    print ('1')

#elif x == y:
#    print('0')

#elif x < y:
#    print('-1')

#Exercise 6.2

#from math import sqrt

#while True:

# print('GIve me the values of the 2 legs of the triangle.')
# print ('I will return the hypothenuse for you.\n')
# print('.\n')

# f = float(input(':'))
# s = float(input(':'))

# h  = sqrt(f**2 + s**2)
 

# print ('O valor da hipotenusa é:', (h))

#Exercise 6.3. Write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False otherwise.

#x = int(input('x:'))
#y = int(input('y:'))
#z = int(input('z:'))
        
#def is_between():
#    if x <= y <=z:
#        print ('True')

#    else:
#        print ('False')
        
#is_between()

#Factorial of a number exercise

#while True:

#    factorial = 1

#    x = int(input('Type the number you want to discover the factorial:'))

#    if x<0:
#        print ('There is no factorial for negative numbers')

   # elif x ==0:
#        print ('The factorial of 0 is 1')

  #  else:
    #    for i in range(1, x+1):
     #       factorial = factorial*i
            
   #         print ('THe factorial of ', x, 'is ', factorial)

   # break




total = 0
a = range (1, 250)

for i in a:
    total += i
    
print (total)

#Exercise 6.7
#A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
# Write a function called is_power that takes parameters a and b andreturns True if a isapowerof b.

#a = int(input('Number a is:'))
#b = int(input('Number b is:'))

#d = a/b
#if d.is_integer():
 #   d2 = a/d
  #  if d2.is_integer():
  #      print ('True. A is power of B.')

#else:
#    print('False. A is not power of B.')

#Exercise 6.8
#Write a function called gcd that takes parameters a and b and returns their greatest common divisor.
#One way to ﬁnd the GCD of two numbers is based on the observation that if r is the remainder
#when a is divided by b, then gcd(a,b) = gcd(b,r).

a = int(input('Number a is:'))
b = int(input('Number b is:'))

r = a%b

if r == 0:
    print ('GCD = ', (b))

else:
    x = b%r
    if x == 0:
        print ('GCD = ', (r))
        
    else:
        
    










      

    
