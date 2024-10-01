def Unpacking(my_tuple):

    a,b,c,d=My_tuple[0],My_tuple[1],My_tuple[2],My_tuple[3]

    return a,b,c,d
My_tuple=(10,20,30,40)



a,b,c,d=Unpacking(My_tuple)
print("After unpacking the Tuple:")
print("Value in a:",a,"\nValue in b:",b,"\nValue in c:",c,"\nValue in d:",d)