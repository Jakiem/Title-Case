def title_case(title, minor_words=''):
    resul = ''
    spl = []
    minor_spl = []
    
    if title != '':
        spl = title.split(' ')
        minor_spl = minor_words.split(' ') 
        for i in spl:
              for j in minor_spl:
                j = j.lower()
                i = i.lower()
                if i == j:
                  i = i.lower()
                  resul = resul + j + ' '  
                  i = ''
                elif i != j:
                    i = i.capitalize()   
                else:
                    i = i.lower()
              resul = resul[0].upper() + resul[1:] 
              resul = resul + i +' '
    return print(resul.rstrip())

title_case('THE WIND IN THE WILLOWS', 'The In')

