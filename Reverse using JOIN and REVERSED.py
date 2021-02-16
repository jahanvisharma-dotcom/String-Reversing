#REVERSE A STRING USING JOIN AND REVERSED 
def reverse_string(j):
    j1 = ''.join(reversed(j))
    return j1
    
input_string = 'JAHANVI'
print("reverse of string using methods are : ",reverse_string(input_string))
