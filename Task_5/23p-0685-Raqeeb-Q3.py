import json
import statistics

with open("data.json", "r") as f:
    j_files = f.read()

j_data = json.loads(j_files)

# print(j_data)

num=0
total=0
average_age=0
ages=[]
#For average Age 
for i in j_data:
    for value in i:
        if(value=="age"):
            total+=i[value]
            ages.append(i[value])
            num+=1

average_age=total/num
print("************************************")

print("Average of age:\n",average_age)
All_skills=[]

for i in j_data:
    for value in i:
        if(value=="skills"):
            All_skills.extend(i[value])

#Most common skill
Common_skill=statistics.mode(All_skills)
print("************************************")

print("\nMost common Language:")
print(Common_skill)
Skill_frequency={}

for i in All_skills:
    Skill_frequency[f"{i}"]=All_skills.count(i)

print("************************************")
print("\nFrequency of Language:")
for value in Skill_frequency:
    print(value,":",Skill_frequency[value])

print("\n************************************")

Country_wise_skill_diction={}

country_skills=[]
same=False
diff=True
index_outer=0
for i in j_data:
        index_inner=0
        for tem1 in j_data:
                    if(i["country"]==tem1["country"]):
                        same=True
                        if(index_inner<=index_outer):
                            diff=False
                            
                            
                            country_skills.extend(tem1["skills"])
                    index_inner+=1
        if(same==False):
            value=i["country"]
            value2=i["skills"]
            Country_wise_skill_diction[f"{value}"]=value2
        elif diff==False:
            country_skills=set(country_skills)
            country_skills=list(country_skills)
            value3=i["country"]
            Country_wise_skill_diction[f"{value3}"]=(country_skills)
            same=False
        else:
            diff=True
            same=False
        country_skills=[] 
        
        index_outer+=1
        

for value in Country_wise_skill_diction:
    print(value,":",Country_wise_skill_diction[value])

age_groups=[]
ages2=[]
max_age=max(ages)

i=20
while(i<=max_age):
    for age in j_data:
        if(age["age"]>i and age["age"]<i+11):
            ages2.append(age)
    if(ages2!=[]):
        age_groups.append(ages2)
    ages2=[]
    
    i+=10

k=20
print("\n")
for value2 in age_groups:
    print("************************************")
    print("Age range:",k+1,"-",k+10)
    print("************************************")
    
    for j in value2:
        for p in j:
            print(p,":",j[p])
    
    print("\n\n")
    k+=10