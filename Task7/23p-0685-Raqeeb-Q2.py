import os 
import xml.etree.ElementTree as ET


My_File_Path_XML='/home/raqeeb/My_data/3rd_Semester/Programming_for_AI_Lab/Programmin_For_AI/My_data/CTIDataset'


for My_Xml_file in os.listdir(My_File_Path_XML):
    if My_Xml_file.endswith('.xml'):
        try:
            My_Tree= ET.parse(os.path.join(My_File_Path_XML,My_Xml_file))
            My_Root=My_Tree.getroot()
            # print(My_Root)
        except Exception as e:
            print(f"Error processing {My_Xml_file}: {str(e)}")

print("************************************")
print("CATEGORY")
Event_data=My_Root.findall('Event/Attribute')
for Attribute in Event_data:
    for items in Attribute:
        for Cate in items:
            if(Cate.tag == 'category'):
                print(Cate.text)

print("************************************")
print("VALUES")
for Attribute in Event_data:
    for items in Attribute:
        for Cate in items:
            if(Cate.tag == 'value'):
                print(Cate.text)
            
            


            