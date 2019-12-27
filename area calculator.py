def get_func(shape,size1=0,size2=0):
    if shape=='square':
        return size1*size1        #caculate  area of square
    if shape=='circle':
        return 3.14*size1*size1   #caculate  area of circle
    if shape=='rectanle':
        return size1*size2        #caculate  area of rectanle
    if shape=='triangel':
        return size1*size2/2      #caculate  area of triangel
Is=['square','circle','rectanle','triangel']
print('Square: 0 ,','Circle: 1 ,','Rectanle: 2 ,','Triangel: 3 ,')
shape=int(input("Enter number of shapes:"))
if shape==0:
    size1=int(input("Enter Size1:"))
    print (get_func(Is[shape],size1))
elif shape==1:
    size1=int(input("Enter Size1:"))
    print (get_func(Is[shape],size1))
elif shape==2:
    size1=int(input("Enter Size1:"))
    size2=int(input("Enter Size2:"))
    print(get_func(Is[shape],size1,size2))
elif shape==3:
    size1=int(input("Enter Size1:"))
    size2=int(input("Enter Size2:"))
    print(get_func(Is[shape],size1,size2))
else:
    print("The number is not define!!!")