#REVERSE A STRING USING FOR LOOP

def reverse_string(j):
    j1 = ''
    for s in j:
        j1 = s + j1
    return j1
        
input_string = 'JAHANVI'
print("reverse of string using for loop is : ",reverse_string(input_string))
