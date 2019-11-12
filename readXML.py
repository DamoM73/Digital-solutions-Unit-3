import xml.etree.ElementTree as ET

# read the xml file and establish the root
tree = ET.parse('roadcrash_factors.xml')
root = tree.getroot()

#print(root.tag, root.attrib)

'''
for child in root:
    print(child.tag, child.attrib, child.text)
'''

'''
for elem in root.iter():
    print(elem.tag)
'''

'''
xml_string = ET.tostring(root).decode()
print(xml_string)
'''

'''
for child in root:
    print(child.tag, child.attrib, child.text)
    for sub_child in child:
        print(sub_child.tag, child.attrib, sub_child.text)

'''

line_count = 0

for child in root:
    for  sub_child in child:
        if sub_child.tag == "Crash_Year":
            year = sub_child.text
        elif sub_child.tag == "Crash_Severity":
            severity = sub_child.text
        elif sub_child.tag == "Involving_Drink_Driving":
            drink_driving = sub_child.text
        elif sub_child.tag == "Involving_Driver_Speed":
            speed = sub_child.text
        elif sub_child.tag == "Involving_Fatigued_Driver":
            fatigue = sub_child.text
        elif sub_child.tag == "Involving_Defective_Vehicle":
            vehicle_defect = sub_child.text
            line_count += 1
            print(f'In {year} an accident of severity {severity} was caused by drink driving:{drink_driving}, speeding: {speed}, fatigue: {fatigue}, defective vehicle: {vehicle_defect}')

print(f'Processed {line_count-1} accidents')
