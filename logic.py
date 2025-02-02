def formul1(a, b):
    sch=0     
    while a !=b:
        if a > b:
            a=a-b
        else:
            b=b-a
        sch+=1
    
    return a, sch

def formul2(a, b):
    sch=0     
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
        sch+=1
    
    return a or b, sch

