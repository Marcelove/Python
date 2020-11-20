
#Problema das cédulas
#resolver! RESOLVI CARALHO
#1 5 10 25 5
import time



while True:
    #
    print ('Olá, sou o "Vendeta", um assistente eletrônico idealizado por Marcelo Amorim Jr!. Estou na versão Beta.')
    print ('Simularei uma máquina de sacar dinheiro  dessa vez. \n')
    print ('Direi quantas e quais cédulas serão necessárias para lhe retornar o valor desejado, em reais.')
    print ('Ainda não opero com centavos :(')
    x = int(input('Digite a quantidade, em reais, que você deseja sacar e pressione ENTER.: \n'))
    

    if x>= 100:           #SE a quantidade de cédulas for maior que 100
        print ('Ok...')
        time.sleep(2)
        #
        print ('Você receberá ', int(x/100), ' cédula(s) de 100 reais\n')
        
        if x%100>0:
            #
            y = x%100
            print ('Você receberá ', int(y/50), ' cédula(s) de 50 reais \n')


            if y%50>0:
                #
                a = y%50
                print ('Você receberá ', int(a/20), ' cédula(s) de 20 reais\n')
                                                
                if a%20>0:
                    #
                                                                
                    b = a%20
                    print ('Você receberá ', int(b/10), ' cédula(s) de 10 reais\n')
                                
                    if b%10>0:
                        #
                        c = b%10
                        print ('Você receberá ', int(c/5), ' cédula(s) de 5 reais\n')
                                
                        if c%5>0:
                            #
                        
                            d= c%5
                            print ('Você receberá ', int(d/2), ' cédula(s) de 2 reais\n')
                                
                            if d%2>0:
                                #
                                    e = d%2
                                    print ('Você receberá ', int(e/1), ' cédula(s) de 1 reais\n')
                                        
                                    

    elif 100>x>=50:               #SE a quantidade de cédulas for menor que 100 e maior ou igual a 50
        
        print ('Ok...')
        time.sleep(2)
          #
        if x%100:
            
            #
            y = x%100
            print ('Você receberá ', int(y/50), ' cédula(s) de 50 reais\n')

            if y%50:
                #
                a = y%50
                print ('Você receberá ', int(a/20), ' cédula(s) de 20 reais\n')
                                                
                if a%20:
                    #
                    b = a%20
                    print ('Você receberá ', int(b/10), ' cédula(s) de 10 reais\n')
                                                                
                    if b%10:
                        #
                        c = b%10
                        print ('Você receberá ', int(c/5), ' cédula(s) de 5 reais\n')
                                                                             
                        if c%5:
                            #
                            d = c%5
                            print ('Você receberá ', int(d/2), ' cédula(s) de 2 reais\n')
                                                                                             
                            if d%2:
                                #
                                e = d%2
                                print ('Você receberá ', int(e/1), ' cédula(s) de 1 reais\n')

                                

    elif 50>x>=20:                       #SE a quantidade de cédulas for menor que 50 e maior ou igual a 20
        print ('Ok...')
        time.sleep(2)
        #
        if x%50:
            #
            y = x%50
            print ('Você receberá ', int(y/20), ' cédula(s) de 20 reais\n')

            if y%20:
                #
                a = y%20
                print ('Você receberá ', int(a/10), ' cédula(s) de 10 reais\n')
                                                
                if a%10:
                    #
                    b = a%10
                    print ('Você receberá ', int(b/5), ' cédula(s) de 5 reais\n')
                                                                
                    if b%5:
                        #
                        c = b%5
                        print ('Você receberá ', int(c/2), ' cédula(s) de 2 reais\n')

                                                                                
                        if c%2:
                            #
                            d = c%2
                            print ('Você receberá ', int(d/1), ' cédula(s) de 1 reais\n')

                            
                

    elif 20>x>=10:              #SE a quantidade de cédulas for menor que 20 e maior ou igual a 10
        
        print ('Ok...')
        time.sleep(2)
        #
        if x%20:
            #
            y = x%20
            print ('Você receberá ', int(y/10), ' cédula(s) de 10 reais\n')
                                
            if y%10:
                #
                z = y%10
                print ('Você receberá ', int(z/5), ' cédula(s) de 5 reais\n')
                                                
                if z%5:
                    #
                    w = z%5
                    print ('Você receberá ', int(w/2), ' cédula(s) de 2 reais\n')
                                                                
                                
                    if w%2:
                        #
                        c = w%2
                        print ('Você receberá ', int(c/1), ' cédula(s) de 1 reais\n')

                        

                        

    elif 10>x>=5:                                                       #SE a quantidade de cédulas for menor que 10 e maior ou igual a 5
        
        print ('Ok...')
        time.sleep(2)
        #
        if x%10:
            #
            y = x%10
            print ('Você receberá ', int(y/5), ' cédula(s) de 5 reais\n')
                                
            if y%5:
                #
                z = y%5
                print ('Você receberá ', int(z/2), ' cédula(s) de 2 reais\n')
                                
                if z%2:
                    #
                    w = z%2
                    print ('Você receberá ', int(w/1), ' cédula(s) de 1 reais\n')

                    

    elif 5>x>=2:                     #SE a quantidade de cédulas for menor que 5 e maior ou igual a 2
        print ('Ok...')
        time.sleep(2)
        #
        if x%5:
            #
            
            y = x%5
            print ('Você receberá ', int(y/2), ' cédula(s) de 2 reais\n')
            if x%2:
                #
                y = x%2
                print ('Você receberá ', int(y/1), ' cédula(s) de 1 reais\n')

                

    elif 2>x>=1:                        #SE a quantidade de cédulas for menor que 2 e maior ou igual a 1
        print ('Ok...')
        time.sleep(2)
        #
        if x%2:
            #
            y = x%2
            print ('Você receberá ', int(y/1), ' cédula(s) de 1 reais\n')


    
            







