
#Question 4
import csv

filename = 'data.csv'

import csv

def display():
    temp2=""
    found = False
    
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file) 
        data = {}

        # Initialize the dictionary with column names
        for header in reader.fieldnames:
            data[header] = []

        # adding the dictionary with values
        for row in reader:
            for key in row:
                if row[key]:  
                    data[key].append(row[key])

        
        for category, values in data.items():
            if values:  
                print(f"{category}: {', '.join(values)}")



def update_csv(filename, new_value=None, column=None, delete_value=None):
    # Read the existing data from the CSV file
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader]

    if not rows:
        print("The Inventory file is empty.")
        return

    # Append the new value to the specified column
    if new_value is not None and column is not None:
        # Check if the column exists
        if column in rows[0]:
            # Find the first empty row in the specified column
            for row in rows:
                if row[column] == "": 
                    row[column] = new_value  # Set the new value in the specified column
                    break  # Exit after adding the new value
            else:
                new_row = {col: "" for col in rows[0].keys()}  # Create a new row with empty values
                new_row[column] = new_value  # Set the new value in the specified column
                rows.append(new_row)  # Append the new row to the rows
        else:
            print(f"does not exist in the Inventory.")

    #Delete the value in the specified column without affecting other columns
    if delete_value is not None:
        found = False
        for row in rows:
            for key in row.keys():
                if row[key] == delete_value:
                    deleted_value = row[key]  # Store the deleted value
                    row[key] = ""  # Clear the value in the specified cell
                    found = True
                    break 
            if found:  
                break
        if not found:
            print(f" '{delete_value}' does not exists in the Inventory")
            return False



    # Write the updated data back to the CSV file
    with open(filename, mode='w', newline='') as file:
        fieldnames = rows[0].keys()  # Get the field names from the first row
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header
        writer.writerows(rows) 
    return delete_value
        
        
def inventory_action():
    print("\n1)Remove any item\n2)Watch the items you have")
    userinput=int(input('input:'))
    if(userinput==1):
        print("**********IIEMS in INVENTORY**********")
        if(None!=display()):
            pass
        else:
            print("***********LIST IS EMPTY****************")
        
        print("Which item you want to remove write name?:")
        userinput=(input())
        update_csv(filename, delete_value=userinput, column='Age')
        
    elif(userinput==2):
        print("**********IIEMS in INVENTORY**********")
        if(None!=display()):
            pass
        else:
            print("***********LIST IS EMPTY****************")


#In this game their are two paths with different ending 
#During game we can remove items from the inventory which will change the output
#Like if you add the sword and then after while you deleted it then the ending will be different
#Similar for key and the code word 

def Main_function():

    
    print('**************WELCOME TO JUNGEL MAI MANGAL***************')
    print('You are out in a journey to complete the mission of your father to explore the LOST CITY OF CREATURES')
    print('You collect the Map found in the beg of your father')
    
    print('*****************\nMap added to inventory succesfully\n***********************')
    update_csv(filename, new_value="map", column="Tools")
    update_csv(filename, new_value="apple", column="Food")
    update_csv(filename, new_value="banana", column="Food")
    update_csv(filename, new_value="grapes", column="Food")


    print("You started your journey. You crossed a river and entered a forest.")
    print("You walk through the forest for sometime and then end up with multiple paths:")
    userinput=''
  
    print("************************************************")
    while(1):
        print("Enter 0 Exit ")
        print("enter 'i'  for inventory action")
        userinput=Movement_1()
        #Path 1
        if(userinput=='1'):
            print("\n******************************")
            print("You move to right side of Path.")
            print("After moving for a while then you say a shinning stone attached to the wall")
            print("Want to add it to your inventory?(1/0):")
            userinput=int(input())
            if(userinput==1):
                update_csv(filename, new_value='Gamstone', column='Tools')
                print('*******ITEM ADDED TO INVENTORY SUCCESSFULLY*******')
                
            elif(userinput==0):
                pass
            print("'e' to eat food")
            userinput=(input())
            if(userinput=='e'):
                print("You are hungry. You eat the food from your inventory.")
                update_csv(filename, delete_value="apple", column='Food')
            
            while(1):   
                print("Then you pass through the Garden full of flowers.")
                print("From a far distance you saw something written on the big wall")
                print("Want to see what it is from close?(1/0):")
                print("'i' for inventory action:")
                userinput=(input())
                if(userinput=='1'):
                    print("You Start to walk towards the wal.......")
                
                    print("Walk.....")
                    print("You saw their was written something like this LLIKOUY.\nI may be helpfull in the path\n so you write it down. ")
                    update_csv(filename, new_value='LLIKOUY', column='Tools')
                    
                    print("********CODE WORD ADDED TO INVENTORY************")
                    break 
                
                elif(userinput=='0'):
                    break
                    
                elif(userinput=='i'):
                    print("You are in inventory mode")
                    inventory_action()
                    
                   
            print("\n****************************\nYou continued your journey from the garden and reached at bottom of a huge Mountain in the forest")
            print("When you reached near the mountain end you realized their is a face on the bottom of the mountain like a gate")
            print("When you tried to touch it .")
            print("GATE_FACE: HEY WHAT ARE YOU DOING?")
            print("AHhhhhhhhhhhhhh")
            print("GATE_FACE: If you want to stay alive give me the keyword")
            print("you have two choices:\n1)Think\n2)RUn")
            userinput=int(input('User input:'))
            if(userinput==1):
                if("LLIKOUY"==update_csv(filename, delete_value="LLIKOUY", column='Tools')):
                        print("You start thinking !!!!!")
                        print("Then you suddenly remember about that word on the wall")
                        print("Player code is LLIKOUY ")
                        print("Your code is correct you can pass:")
                        print("You found a sward hang with wall of cave")
                        print("Want to pick the sword?(1/0)")
                        userinput=int(input())
                        if(userinput==1):
                            update_csv(filename, new_value='Sword', column='Weapons')
                        else:
                            pass
                        
                        while(1):
                                print("you crossed the cave and reached the end of forest where you finally meet the LOST CITY CREATURES")
                                print("They asked if you have the sword or not?(1/0)")
                                print("'i' for inventory actions")
                                userinput=(input("Input:"))
                                if(userinput=='i'):
                                    inventory_action()
                                else:
                                    break
                        if('Sword'==update_csv(filename, delete_value='Sword', column='Weapons')):
                                print("THey received the sword and welcome you ")
                                print("GAME END")
                                return True

                        elif(False==update_csv(filename, delete_value='Sword', column='Weapons')):
                                print("You didn't have the sword so they killed you and burn you down into ashes")
                                print("THE END")
                                return False
            #ENDING 1
            elif(userinput==2):
                    print("\nYou tried to run but the Gate mouth took a great breath and eat you as a lunch")
                    print("\nYOU DEAD AND YOUR FATHERS JOURNEY ENDS HERE>........")
                    return False
    
        elif(userinput=='2'):
            print("You move to left side of Path.")
            print("After moving for a while then you say a shinning Knife attached to the wall")
            print("Want to add it to your inventory?(1/0):")
            userinput=int(input())
            if(userinput==1):
                update_csv(filename, new_value='knife', column='Weapons')
                print('*******ITEM ADDED TO INVENTORY SUCCESSFULLY*******')
                
            elif(userinput==0):
                pass
            print("Then you pass through the green Medows.")
            print("want to eat something?(1/0)")
            userinput=input()
            if(userinput=='1'):
                update_csv(filename,delete_value='grapes',column='Food')
                print("You have eaten the grapes")
            while(1):   
                print("You saw something in the middle of Medows on the glass box")
                print("Want to see what it is from close?(1/0):")
                print("'i' for inventory action")
                
                userinput=(input())
                if(userinput=='1'):
                    print("You Start to walk towards the wal.......")
                
                    print("Walk.....")
                    print("You saw it is a big ancient key")
                    print("1)Want to break it and take the key")
                    print("2)Look around to open the box")
                    userinput=int(input("Input:"))
                    #Second Ending****************************
                    if(userinput==1):
                        print("You broke the glass and took the key")
                        print("But all at sudden the land crushed down and you died")
                        print("THE END")
                        return False
                    elif(userinput==2):
                        print("You looked around and found rolling stone. you rolled it and the box opened automatically")
                        print("Want to add the key to inventory?(1/0):")
                        userinput=int(input())
                        if(userinput==1):
                            update_csv(filename, new_value='key', column='Tools')
                            print("******KEY ADDED TO INVENTORY SUCCESSFULLY**********")
                            break
                    break

                elif(userinput=='i'):
                    inventory_action()

                elif(userinput==0):
                    break

            print("You continued your journey from the garden and reached at bottom of a huge Mountain in the forest")
            print("When you reached near the mountain end you realized their is a face on the bottom of the mountain like a gate")
            print("When you tried to touch it .")
            print("GATE_FACE: HEY WHAT ARE YOU DOING?")
            print("AHhhhhhhhhhhhhh")
            print("GATE_FACE: If you want to stay alive give me the Key")
        
            print("you have two choices:\n1)Think\n2)RUn")
            userinput=(input('User input:'))
            if(userinput=='1'):
                print("\n\nYou start thinking !!!!!")
                if('key'==update_csv(filename, delete_value='key', column='Weapons')):
                    print("Then you suddenly remember about that Key on the Glass box")
                    print("you have the key know you can pass:")
                    print("You found a sward hang with wall of cave")
                    print("Want to pick the sword?(1/0)")
                    userinput=(input())
                    if(userinput=='1'):
                        update_csv(filename,new_value='sword',column='Weapons')
                    print("you crossed the cave and reached the end of forest where you finally meet the LOST CITY CREATURES")
                    while(1):
                        
                            print("They asked: you have the sword or not?(1/0)")
                            print("'i' For inventory action")
                            userinput=(input())
                            #Third ending
                            if(userinput=='1'):
                                    if('sword' ==  update_csv(filename, delete_value='sword', column='Weapons')):
                                            print("THey received the sword and welcomed you ")
                                            print("GAME END")
                                            return True
                                    else:
                                        print("You didn't have the sword so they killed you and burn you down into ashes")
                                        return False
                            #4th ending
                            elif(userinput=='0'):
                                    print("You didn't have the sword so they killed you and burn you down into ashes")
                                    return False
                            elif(userinput=='i'):
                                inventory_action()
                   
                #5th ending 
                else:
                    print("GATE_FACE: You don't have the key You die HAHAHAHAHA!!!")
                    return  False
                
            #6th ending
            elif(userinput==2):
                print("\nYou tried to run but the Gate mouth took a great breath and eat you as a lunch")
                print("\nYOU DEAD AND YOUR FATHERS JOURNEY ENDS HERE>........")
                return False            
        elif(userinput=='i'):
            inventory_action()
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
    


Inventory = {
    "Weapons": ["pin"],
    "Food": [""],
    "Tools": [""]
}

# Write sample data to CSV for testing
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(Inventory.keys())
    # Write rows
    for row in zip(*Inventory.values()):
        writer.writerow(row)



#Main game function
Main_function()


print("\n********************************nTHANKS FOR PLAYING\n********************************")
