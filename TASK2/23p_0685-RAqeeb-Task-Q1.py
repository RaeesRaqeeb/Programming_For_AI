from datetime import date
import time
def  My_Chat_Bot():
    user_input=''
    while(user_input!='exit'):
        user_input=input("\nHello sir/Ma'am How may I assis you?\nInput:")
        if(user_input!='exit' or user_input!='bye' or user_input!='quite'):
            Response(user_input)

def Response(user_input):
    days=['Sunday','Monday','Tuesday','Wednesday','Thuesday','Friday','Satureday']
    Possible_questions=["how are you?","what is day today?","did you love anyone?","Which is the top video games of all time?","When GTA 6 will release?"]
    responses_of_questions=["I am fine. Thank you for asking!",f"Today is {days[date.today().day]}","No personal questions please :(","I am happy to guide you\nTheir are many games which considered most liked game in the world.\nSuch as GTA 5, RDR, Call of Duty","Their are many rumorse about the release of GTA 6.\nSome says some of its data or file were leaked therefore \nROCKSTAR company delayed its release date. According to Google it will release in 2026." ]

    zipped_Q_A=list(zip(Possible_questions,responses_of_questions))
   
    for i in zipped_Q_A:
        if(user_input==i[0]):
            for j in i[1]:
                print(j,end='')
        else:
            pass 
        
          
    



#Main functions

My_Chat_Bot()
