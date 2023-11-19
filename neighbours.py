import numpy as np

a = np.array([[17, 24, 18, 15, 16],
              [23,  5,  7, 14, 16],
              [ 4,  6, 13, 20, 22],
              [10, 12, 19, 21,  3],
              [11, 18, 25,  2,  9]
            ])
print('a : \n', a)

b = int(input('\n\nEnter the row(0 to 4) : '))
c = int(input('Enter the column(0 to 4) : '))

print('\n\nElement : ', a[b,c])

N4 = []

if b+1 < 5 :
    N4.append(a[b+1,c])

if b-1 >= 0 :
    N4.append(a[b-1,c])

if c+1 < 5 :
    N4.append(a[b,c+1])

if c-1 >= 0 :
    N4.append(a[b,c-1])

print('\n\n4 neighbours : ', N4) 

N8 = []

if b+1 < 5 :
    N8.append(a[b+1,c])

if b-1 >= 0 :
    N8.append(a[b-1,c])

if c+1 < 5 :
    N8.append(a[b,c+1])

if c-1 >= 0 :
    N8.append(a[b,c-1])

if  b+1 < 5 and c+1 < 5 :
    N8.append(a[b+1,c+1])        

if b+1 < 5 and c-1 >= 0 : 
    N8.append(a[b+1,c-1])

if b-1 >= 0 and c-1 >= 0 :
    N8.append(a[b-1,c-1])

if b-1 >= 0 and c+1 < 5 :
    N8.append(a[b-1,c+1])

print('\n\n8 neighbours : ', N8)    

ND = []

if  b+1 < 5 and c+1 < 5 :
    ND.append(a[b+1,c+1])        

if b+1 < 5 and c-1 >= 0 : 
    ND.append(a[b+1,c-1])

if b-1 >= 0 and c-1 >= 0 :
    ND.append(a[b-1,c-1])

if b-1 >= 0 and c+1 < 5 :
    ND.append(a[b-1,c+1])

print('\n\nD neighbours : ', ND, '\n\n')    

