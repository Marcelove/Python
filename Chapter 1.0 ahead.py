#Basic Introduction
#Login loop Haha bitch
import time                                     #THis imports time so I can use time.sleep and other stuff


while True:
                x = input('Tell me your fucking name: \n')                                 #The command "\n" skips one line 
                if x != 'Marcelo':
                                print ('Hello, ', (x), ',', ' please fuck off.')
                
                if x == 'Marcelo':
                                print ('Checking...')
                                time.sleep(3)
                                print ('All hail the Birdman!')                            #It only reads the rest of the code if the name == "Marcelo"
                                time.sleep(5)
                                break                                                      #This command breaks the 'While true' loop



#SOme Guanabara Shit
snack = ('Hamburguer')
for food in snack:
                print (f'Im gonna eat {food}') #Notice how this code made the word split
                                                 
                
drinks = ('WHey Protein', 'Orange Juice')
for drinking in drinks:
                print (f'And, im gonna drink {drinking}')

print ('What a SNACK man!')

#Tuplas em TImtes de futebol(Guanabara aula 073
teams = ('Sport', 'Santa Cruz', 'Náutico', 'ABC', 'Brasil de pelotas',)
for t in teams:

                print (t)



#Calculating the volume of a sphere with radius 5. (V= 4/3pir^3)

x = float(4/3)
y = float (3.14)
z = int(5**3)          #Radius goes here before "**3"
a = (x*y)

print (a*z)

#Cover price of a book is 24.95. Bookstores get a 40% discount.
#Shipping costs 3$ for the first copy and 0,75$ for each add.
#What is the total wholesale cost for 60 copies?

a = float(24.95/100) #Cover price 
b = float(a*40)      #Cover Price + discount
s = float(0.75*59)   #Shipping cost
st = float(s+3)      #Shipping cost + 3

print (b+st)

#Math Functions
#Notice that the math. HAs to be present for the program to identify the function
#1 The expression math.pi gets the variable pi from the math module
import math

radians = 2
degrees = 45
y = radians - degrees / 360.0 *2* math.pi #1
math.sin(radians)
print (y)

#
import math
math.sqrt(4)                         #Using "raiz quadrada"

#
from math import pi
print (pi)                        #THis prints the value of pi
#or
import math
print (math.pi)                 #This also prints the value of pi

#Defining functions

def call_trogo():
                print ('Hey, dumbass! Come right here') #Try this in interactive mode

def repeat_call():
                call_trogo()
                call_trogo()
                
#
michael = 'Michael is in love with Jackie'              #Try this in interactive mode
def print_twice(x):                                     #Remember that "x" is a variable.
                print (x)                               #In this case, x = Michael = phrase
                print (x)
                print ('Yes she knows, she cares')
#
line1 = ('Wubba Lubba')                                 #Same as the Michael example
line2 = ('Dub Dubb')                                    #Difference is it concatenates the 2 variables
def print_five_times(line1, line2):
                print (line1, line2)
                print (line1, line2)
                print (line1, line2)
                print (line1, line2)
                print (line1, line2)

print_five_times(line1, line2)

#
def call_bruce():                                       #Created a variable inside a function
                bruce = ('Bruce Wayne')                 #THe variable only exists here
                print (bruce)


#While loops

a = 10
while (a > 0):
                a -= 1  
                print(a)                                #10 9 8 7 6 5 4 3 2 1 0

                

#
while True:
                usr_command = input ('Enter Your Command: ')
                if usr_command == "quit":
                                break
                else:
                                print ('You Typed ' + usr_command)
#
quit = input('Type "enter" to quit: ')
while quit != "enter":
                quit = input('Type "enter" to quit: ') #It never quits




                




           
