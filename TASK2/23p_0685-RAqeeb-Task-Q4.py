from datetime import date

def condition_function(my_zip):
    current_date=date.today()
    print(my_zip[0][1])
    for i in range(0,len(my_zip)-1):
        if(my_zip[i][1]>current_date):
            return my_zip[i]
    


def Extractor_Expired_Items(list1, list2):

    my_zip=list(zip(list1,list2))
    
    new_list=[]
    current_date=date.today()
    filtered_items=list((filter(lambda x:x[1]>current_date,my_zip)))
    print(f"Number of unexpired items {len(filtered_items)}")
    print("Following are the items which are not expired:")
    print(list(filtered_items))
    


items = ["Milk", "Bread", "Eggs", "Yogurt", "Cheese"]

expiration_dates= [date(2023, 9, 30), date(2024, 10, 15), date(2023, 9 ,25), date(2024, 9, 8), date(2024, 10, 10)]
current_date=date.today()
Extractor_Expired_Items(items,expiration_dates)