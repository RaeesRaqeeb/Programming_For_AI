def display_inventory(Inven_Diction):
    
    while(1):
        print("*********************\nGAME INVENTORY\n*********************\n")
        print("What you like to do?:")
        print("1)Add new Item\n2)Display items present in inventory\n3)Remove any item\n4)Replace any Item\n5)End Operation\nUserInput:")
        Input_value=int(input())
        value2=0
        check=False
        if Input_value==1:
            print("************************************")
            print("\nEnter the name of Item:")
            user_input=input()
            if(len(Inven_Diction)!=0):
                for value in Inven_Diction:
                    if(value==user_input):
                        value2=Inven_Diction[value]
                        Inven_Diction[value]=(value2+1)
                        check=True
                if(check==False):
                    Inven_Diction[user_input]=(value2+1)
            else:
                Inven_Diction[f"{user_input}"]=1
            print("************************************")
            
                
        elif Input_value== 2:
            print("************************************")
            if(len(Inven_Diction) == 0):
                print("The Inventory is empty. First add new items!!!")
            else:
                i=1
                print("Names      :   Quantity")
                for value in Inven_Diction:
                    print(i,")",value,"        ",Inven_Diction[value])
                    i+=1
            print("************************************")
            
        elif Input_value == 3:
            print("************************************")
            
            i=1
            for value in Inven_Diction:
                    print(i,")",value,":",Inven_Diction[value])
                    i+=1
            print("Which item you want to remove:")
            temp=input()
            for j in Inven_Diction:
                if(j==temp):
                    temp2=j
                    del Inven_Diction[j]
                    break
    
            print(temp2," is removed successfully from the dictionary")
            print("************************************")
            
        elif Input_value == 4:
            print("************************************")
            
            i=1
            for value in Inven_Diction:
                    print(i,")",value,":",Inven_Diction[value])
                    i+=1
            print("Which item you want to Replace:")
            temp3=input()
            print("\nFrom which item you want to replace:")
            item=input()
            k=1
            new_diction={}
            temp4=False
            for value in Inven_Diction:
                if(value==temp3):
                    new_diction[item]=1
                    temp4=True
                else:
                    new_diction[value]=Inven_Diction[value]
                k+=1
            if(temp4==False):
                print("\nNo such item exit in the Inventory.")
            else:
                Inven_Diction=new_diction
                print("\n***Replacement done SUccessfully***")
            print("************************************")
                
        elif Input_value==5:
            break
            print("************************************")
        


diction={}
display_inventory(diction)