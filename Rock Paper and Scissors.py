#Rock, Paper and Scissor
#''


import time

while True:
    print('Hello, I believe you want to play some R P S! \n')
    x = input('Now type the PLAYER.1 name: ')
    y = input('And now the PLAYER.2 name: ')

    print('Very well then. Now you should know the many options you can choose from:\n')

    print('1.rock')
    print('2.paper')
    print('3.scissors \n')
 

    print((x), ', you choose (TYPE AND PRESS ENTER):')
    e1 = input ('')

    print((y), ', you choose (TYPE AND PRESS ENTER):')
    e2 = input ('')

    
    
    if e1 != 'rock':
        if e1 != 'paper':
            if e1 != 'scissors':
                
                print ('You typed it wrong. Try again')

    if e2 != 'rock':
        if e2 != 'paper':
            if e2 != 'scissors':
                
                print ('You typed it wrong. Try again')


        #
    if e1 == e2:
            #           
        print ('waiting...')
        time.sleep(2)
        print ('Its a tie!')
        print (' .\n')
        print (' .\n')
        

        
    if e1 == 'rock' and e2 == 'paper' :
        #
        print ('waiting...')
        time.sleep(2)
        print ('Player ', (y), ' wins!. \n')
        print (' .\n')
        print (' .\n')
        
                    

    if e1 == 'rock' and e2 == 'scissors' :
        #
            #
        print ('waiting...')
        time.sleep(2)
        print ('Player ', (x), ' wins!. \n')
        print (' .\n')
        print (' .\n')
    

    if e1 == 'paper' and e2 == 'rock' :
        #
            #
        print ('waiting...')
        time.sleep(2)
        print ('Player ', (x), ' wins!. \n')
        print (' .\n')
        print (' .\n')
        

    if e1 == 'paper' and e2 == 'scissors' :
        #
            #
        print ('waiting...')
        time.sleep(2)
        print ('Player ', (y), ' wins!. \n')
        print (' .\n')
        print (' .\n')
        

    if e1 == 'scissors' and e2 == 'paper' :
        #
            #
        print ('waiting...')
        time.sleep(2)
        print ('Player ', (x), ' wins!. \n')
        print (' .\n')
        print (' .\n')

           

    if e1 == 'scissors' and e2 == 'rock' :
        #
            #
        print ('waiting...')
        time.sleep(2)
        print ('Player ', (y), ' wins!. \n')
        print (' .\n')
        print (' .\n')
        
        

    

    

    

            
