#CeasarCipher

######***###

def generate_key(num):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ceaser_key = {}
    count = 0
    for i in letters:
        ceaser_key[i] = letters[(count+num) % len(letters)]
        count += 1
    return ceaser_key
    
ceaser_key = generate_key(5)
print(ceaser_key)




def generate_key(num):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ceaser_key = {}
    for i in letters:
        ceaser_key[i] = letters[(num)]
        
        return ceaser_key           # {'A': 'F'}
        return i                    # A    - dict_key
        return ceaser_key[i]        # F    - dict_value
    
    
ceaser_key = generate_key(5)                   # key(100) -- IndexError: string index out of range
print(ceaser_key)



    
    