import random
import time

while True:
    #

    x = str(input('Choose between an Easy or a Hard passwrod:\n'))

    if x == 'easy':
        print ('Very well then. Computing your password...\n')
        time.sleep(3)

        s = 'abcde12345'
        l = 5
        z = ''.join(random.sample(s, l))

        print ('Your password is: ', (z))

    if x == 'Easy':
        print ('Very well then. Computing your password...\n')
        time.sleep(3)

        s = 'abcde12345'
        l = 5
        z = ''.join(random.sample(s, l))

        print ('Your password is: ', (z))

    if x == 'Hard':
        print ('Very well then. Computing your password...\n')
        time.sleep(3)

        s = 'abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$%&*()'
        l = 20
        z = ''.join(random.sample(s, l))

        print ('Your password is: ', (z))
        



    if x == 'hard':
        print ('Very well then. Computing your password...\n')
        time.sleep(3)

        s = 'abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$%&*()'
        l = 20
        z = ''.join(random.sample(s, l))

        print ('Your password is: ', (z))

        

    if x != 'easy':
        if x != 'hard':
            if x != 'Hard':
                if x!= 'Easy':
                    #
            
                    print ('You typed it wrong. Please, try again.\n')
                    print ('.\n')
                    print ('.\n')

    #if x != 'hard':
        #if x != 'easy':
            
           # print ('You typed it wrong. Please, try again.\n')
            #print ('.\n')
            #print ('.\n')



    
    


       



       
