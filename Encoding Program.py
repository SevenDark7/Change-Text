
ans = input('Enter B to change text to binary or enter T to change binary to text: ')

if ans == 'B' or ans == 'b':   
    
    paragraph = input('Enter your text: ')

    result = 0
    print ()
    for ch in paragraph:
        if ch == ' ' :
            print (' ' , end= '')
            continue
        
        else :
            result = (ord(ch))
            print ('{:b}'.format(result) , end='')
        
        
else :
    binary = input('Enter your binary text: ')

    result = ''
    dec = 0
    print ()
    for i in binary:
        if i == ' ' :
            print(' ' , end= '')
            continue
    
        result += i
    
        if len(result) >= 7:
        
            dec = int(result , 2)
            result = ''
            print (chr(dec) , end='')
    




