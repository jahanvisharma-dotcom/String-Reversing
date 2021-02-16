REVERSE A STRING USING WHILE LOOP      

def while_loop(j):
    j1 = ''
    length = len(j) - 1 
    while length >= 0:
        j1 = j1 + j[length]
        length = length - 1 
    return j1

input_string = 'JAHANVI'
print("reverse of string using while loop is : ",while_loop(input_string) )
