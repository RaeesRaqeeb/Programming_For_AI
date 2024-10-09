#Extracting text heading from the layout of the page
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextLine, LTChar

def extract_heading(data):
    headings=[]
    for page_layout in data:
        for element in page_layout:
            if(isinstance(element,LTTextBox)):
                for text_line in element:
                    if isinstance(text_line, LTTextLine):
                        for character in text_line:
                            if isinstance(character,LTChar):
                                if( character.size > 12):
                                    heading_text=text_line.get_text().strip()
                                    headings.append(heading_text)
                                    break
    return headings

path1=extract_pages("PDF1.pdf")
path2=extract_pages("PDF2.pdf")
path3=extract_pages("PDF3.pdf")

data1=extract_heading(path1)
data2=extract_heading(path2)
data3=extract_heading(path3)

my_diction={}
print()
my_list=[data1,data2,data3]

k=1
for i in my_list:
    for j in i:
        my_diction[f"Title:{k} "]=j
        k+=1

#For direct dictionary 
# print(my_diction) 


#For proper layot       
for key in my_diction:
    print(key,":",my_diction[key])