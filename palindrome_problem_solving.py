from itertools import permutations as per

def if_palindrome(text):
    
    lst = list(per(text)) 
    lst = [''.join(i) for i in lst]
    
    res = False
    for i in lst:
        if i == i[::-1]:
            res = True
            break
            
    return print(res)

if_palindrome('carrace')
