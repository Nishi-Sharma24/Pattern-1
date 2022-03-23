#pattern
for x in range(1,6):
    for y in range(1,6-x):
        print(' ',end=' ')
    for z in range(1,x):
        print('*',end=' ')
    for p in range(1,x+1):
       print('*',end=' ')
    print(' ')
input()    
