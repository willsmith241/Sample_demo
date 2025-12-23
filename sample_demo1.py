def just_demo():
    n = 'Malayalam'
    d = {}
    for i in n:
        if i == 'm':
            i = 'M'
        if i in d:
            d[i] += 1
        
        else:
            d[i] = 1    
    print(d)

just_demo()

    