# code here


def Word_frequency_counter(input):
    List1=input.split()
    Word_diction={}
    for i in List1:
        Word_diction[i]=List1.count(i)
        
    return (Word_diction)
user_input=input("Enter any string:")


print(Word_frequency_counter(user_input))



