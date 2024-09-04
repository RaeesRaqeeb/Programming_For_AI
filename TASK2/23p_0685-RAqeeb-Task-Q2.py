

def Main_function(Inventory_list):

    
    print('**************WELCOME TO JUNGEL MAI MANGAL***************')
    print('You are out in a journey to complete the mission of your father to explore the LOST CITY OF CREATURES')
    print('You collect the Map found in the beg of your father')
    
    Inventory_list.append('map')

    print("You started your journey. You crossed a river and entered a forest.")
    print("You walk through the forest for sometime and then end up with multiple paths:")
    userinput=''
  
    print("************************************************")
    while(1):
        print("Enter 0 Exit ")
        print("enter 'i'  for inventory action")
        userinput=Movement_1()
        if(userinput=='1'):
            print("\n******************************")
            print("You move to right side of Path.")
            print("After moving for a while then you say a shinning stone attached to the wall")
            print("Want to add it to your inventory?(1/0):")
            userinput=int(input())
            if(userinput==1):
                Inventory_list.append('Gamstone')
                print('*******ITEM ADDED TO INVENTORY SUCCESSFULLY*******')
                
            elif(userinput==0):
                pass
            print("Then you pass through the Garden full of flowers.")
            
            print("From a far distance you saw something written on the big wall")
            print("Want to see what it is from close?(1/0):")
            userinput=int(input())
            if(userinput==1):
                print("You Start to walk towards the wal.......")
            
                print("Walk.....")
                print("You saw their was written something like this LLIKOUY.\nI may be helpfull in the path\n so you write it down. ")
                Inventory_list.append("LLIKOUY")
                print("********CODE WORD ADDED TO INVENTORY************")

            elif(userinput==0):
                pass

            print("\n****************************\nYou continued your journey from the garden and reached at bottom of a huge Mountain in the forest")
            print("When you reached near the mountain end you realized their is a face on the bottom of the mountain like a gate")
            print("When you tried to touch it .")
            print("GATE_FACE: HEY WHAT ARE YOU DOING?")
            print("AHhhhhhhhhhhhhh")
            print("GATE_FACE: If you want to stay alive give me the keyword")
            for i in Inventory_list:
                if(i=="LLIKOUY"):
                    print("you have two choices:\n1)Think\n2)RUn")
                    userinput=int(input('User input:'))
                    if(userinput==1):
                        print("You start thinking !!!!!")
                        print("Then you suddenly remember about that word on the wall")
                        print(f"Player code is {i}")
                        print("Your code is correct you can pass:")
                        print("You found a sward hang with wall of cave")
                        print("Want to pick the sword?(1/0)")
                        userinput=int(input())
                        if(userinput==1):
                            Inventory_list.append('sword')
                            print("you crossed the cave and reached the end of forest where you finally meet the LOST CITY CREATURES")
                            print("They asked if you have the sword or not?(1/0)")
                            userinput=int(input())
                            value=False
                            for i in Inventory_list:
                                if(i=='sword' and userinput==1):
                                    print("THey received the sword and welcome you ")
                                    print("GAME END")
                                    
                                    return True
                            
                            if(value==False):
                                print("You didn't have the sword so they killed you and burn you down into ashes")
                                return False

                    elif(userinput==0):
                        print("\nYou tried to run but the Gate mouth took a great breath and eat you as a lunch")
                        print("\nYOU DEAD AND YOUR FATHERS JOURNEY ENDS HERE>........")
                        return False
                    
            
            print("1 to run")
            userinput=int(input())
            if(userinput==1):
                print("\nYou tried to run but the Gate mouth took a great breath and eat you as a lunch")
                print("\nYOU DEAD AND YOUR FATHERS JOURNEY ENDS HERE>........")
                return False
        elif(userinput=='2'):
            print("You move to left side of Path.")
            
            print("After moving for a while then you say a shinning Knife attached to the wall")
            print("Want to add it to your inventory?(1/0):")
            userinput=int(input())
            if(userinput==1):
                Inventory_list.append('Knife')
                print('*******ITEM ADDED TO INVENTORY SUCCESSFULLY*******')
                
            elif(userinput==0):
                pass
            print("Then you pass through the green Medows.")
            
            print("You saw something in the middle of Medows on the glass box")
            print("Want to see what it is from close?(1/0):")
            userinput=int(input())
            if(userinput==1):
                print("You Start to walk towards the wal.......")
            
                print("Walk.....")
                print("You saw it is a big ancient key")
                print("1)Want to break it and take the key")
                print("2)Look around to open the box")
                userinput=int(input("Input:"))
                if(userinput==1):
                    print("You broke the glass and took the key")
                    print("But all at sudden the land crushed down and you died")
                    return False
                elif(userinput==2):
                    print("You looked around and found rolling stone. you rolled it and opend the box")
                    print("Want to add the key to inventory?(1/0):")
                    userinput=int(input())
                    if(userinput==1):
                        Inventory_list.append('key')
                        print("******KEY ADDED TO INVENTORY SUCCESSFULLY**********")


            

            elif(userinput==0):
                pass

            print("You continued your journey from the garden and reached at bottom of a huge Mountain in the forest")
            print("When you reached near the mountain end you realized their is a face on the bottom of the mountain like a gate")
            print("When you tried to touch it .")
            print("GATE_FACE: HEY WHAT ARE YOU DOING?")
            print("AHhhhhhhhhhhhhh")
            print("GATE_FACE: If you want to stay alive give me the keyword or Key")
            for i in Inventory_list:
                if(i=='key'):
                    print("you have two choices:\n1)Think\n2)RUn")
                    userinput=int(input('User input:'))
                    if(userinput==1):
                        print("\n\nYou start thinking !!!!!")
                        print("Then you suddenly remember about that Key on the Glass box")
                        print(f"Player code is {i}")
                        print("Your code is correct you can pass:")
                        print("You found a sward hang with wall of cave")
                        print("Want to pick the sword?(1/0)")
                        userinput=int(input())
                        if(userinput==1):
                            Inventory_list.append('sword')
                            print("you crossed the cave and reached the end of forest where you finally meet the LOST CITY CREATURES")
                            print("They asked if you have the sword or not?(1/0)")
                            userinput=int(input())
                            value=False
                            for i in Inventory_list:
                                if(i=='sword' and userinput==1):
                                    print("THey received the sword and welcome you ")
                                    print("GAME END")
                                    
                                    return True
                            
                            if(value==False):
                                print("You didn't have the sword so they killed you and burn you down into ashes")
                                return False
                            

                        

                    elif(userinput==0):
                        print("\nYou tried to run but the Gate mouth took a great breath and eat you as a lunch")
                        print("\nYOU DEAD AND YOUR FATHERS JOURNEY ENDS HERE>........")
                        return False
                    
            
            print("1 to run")
            userinput=int(input())
            if(userinput==1):
                print("\nYou tried to run but the Gate mouth took a great breath and eat you as a lunch")
                print("\nYOU DEAD AND YOUR FATHERS JOURNEY ENDS HERE>........")
                return False
        elif(userinput=='i'):
            print("\n1)Remove any item\n2)Watch the items you have")
            userinput=int(input('input:'))
            if(userinput==1):
                num=1
                for i in Inventory_list:
                    print(num,i)
                    num+=1
                print("Which item you want to remove?:")
                userinput=int(input())
                Inventory_list.remove(Inventory_list[userinput-1])
            elif(userinput==2):
                print("**********IIEMS in INVENTORY**********")
                num=0
                for i in Inventory_list:
                    print(num+1,": ",i)
                print("*******************************************")
                if(num==i):
                    print("***********LIST IS EMPTY****************")

        elif(userinput=='0'):
            break
        else:
            print("Invalid input!!!!!")
            



        

    
    
def Movement_1():

    print("1)Move to right path")
    print("2)Move to left path")
 
 
    print("User_iput=")
    User_input=(input())
    return User_input
    


Inventory_list=[]

Main_function(Inventory_list)
