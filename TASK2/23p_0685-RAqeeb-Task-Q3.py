def Finder(my_list):
    counter=0
    new_list=[]
    for i in my_list:
        if(i[0]=='A'):
            new_list.append(i)
            counter+=1
    
    print(f"Number of the words who start with A are: {counter}")
    print('Following are the words who start with A:')
    for k in new_list:
        print(k, sep=',')
    pass



word_list = ["Apple", "Banana", "Avocado", "Cherry", "Apricot","Grapes"]
Finder(word_list)
