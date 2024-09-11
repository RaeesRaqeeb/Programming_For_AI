def Set_Operation(My_Set):
    num=1
    for i in range(0,4):
        My_Set.add(num)
        num+=2
    print(My_Set)

    for i in My_Set:
        if(i==3):
            print("Yes 3 is in the given set")

    My_Set.remove(5)

    print("After removing the 5 from the set:",My_Set)
    

    
    


My_set=set()

Set_Operation(My_set)