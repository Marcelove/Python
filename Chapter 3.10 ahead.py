#Drawing a figure

print ('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')
print ('l', ' ', ' ', ' ', ' ', 'l', ' ', ' ', ' ', ' ', 'l')
print ('l', ' ', ' ', ' ', ' ', 'l', ' ', ' ', ' ', ' ', 'l')
print ('l', ' ', ' ', ' ', ' ', 'l', ' ', ' ', ' ', ' ', 'l')
print ('l', ' ', ' ', ' ', ' ', 'l', ' ', ' ', ' ', ' ', 'l')
print ('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')
print ('l', ' ', ' ', ' ', ' ', 'l', ' ', ' ', ' ', ' ', 'l')
print ('l', ' ', ' ', ' ', ' ', 'l', ' ', ' ', ' ', ' ', 'l')
print ('l', ' ', ' ', ' ', ' ', 'l', ' ', ' ', ' ', ' ', 'l')
print ('l', ' ', ' ', ' ', ' ', 'l', ' ', ' ', ' ', ' ', 'l')
print ('+', '-', '-', '-', '-', '+', '-', '-', '-', '-', '+')

print ('0', '0', '0', '0', '0')
print (' ', ' ', 'I', ' ', ' ')
print (' ', ' ', 'I', ' ', ' ')
print (' ', ' ', 'I', ' ', ' ')
print ('0', '0', '0', '0', '0')

#Drawing A square with a  turtle named Bob

from turtle import Turtle, Screen
import turtle                      #? Not sure why, but without the 'turtle' i cant use the window functions.
import os                          #The 'os' import the window functions, such as color and title.   

bob = Turtle(shape="turtle")      #shaping bob
wn = turtle.Screen()              #USing this function so I can call another window functions
wn.bgcolor ('white')              #Background color
wn.title ('Bob the drawer')       #WIndow title


bob.color('black', 'cyan')
bob.begin_fill()
for side in range(4):             #It repeats the code 4 times so I dont have to write it repeatdily
                bob.fd(200)       #Bob goes forward 100              
                bob.lt(90)        #Bob goes left 90 graus
                
bob.end_fill()

bob.color('black', 'red')
bob.begin_fill()
for side in range(4):
                bob.rt(90)
                bob.fd(200)
                
bob.end_fill()

bob.color('black', 'yellow')
bob.begin_fill()
for side in range(4):
                bob.fd(200)
                bob.rt(90)

bob.end_fill()
                
bob.color('black', 'green')
bob.begin_fill()
for side in range(4):
                bob.lt(90) 
                bob.fd(200)

bob.end_fill()

#bob.bk(1200)




                
#bob.rt(45)



#Desactivated
#def square():                                            #Defined a function called square
                #from turtle import Turtle, Screen             
                #bob = Turtle(shape='turtle')
                #bob.turtlesize(5)                       #Bob's size
                #bob.pensize(20)                          #Bob's pensize
                #for dr in range(4):                     #This command makes what is in its argument repeat the amount of times inside the '()'
                                #bob.fd(400)
                                #bob.lt(90)

#square()                                                 #Executed it








