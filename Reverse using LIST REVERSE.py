#REVERSE A STRING USING LIST REVERSE
def reverse_string(j):
    if len(j) == 0:
        return j 
    else:
        return reverse_string(j[1:]) + j[0]
        
input_string = 'JAHANVI'
print("reverse of string using reverse is : ",reverse_string(input_string))
