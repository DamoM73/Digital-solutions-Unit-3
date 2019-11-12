import xml.etree.ElementTree as ET

tree = ET.parse('roadcrash_factors.xml')

root = tree.getroot()

# print(root.tag, root.attrib)

line_count = 0
for elem in root.iter():
    if elem.tag == "Crash_Year":
        year = elem.text
    elif elem.tag == "Crash_Severity":
        severity = elem.text
    elif elem.tag == "Involving_Drink_Driving":
        drink_driving = elem.text
    elif elem.tag == "Involving_Driver_Speed":
        speed = elem.text
    elif elem.tag == "Involving_Fatigued_Driver":
        fatigue = elem.text
    elif elem.tag == "Involving_Defective_Vehicle":
        vehicle_defect = elem.text
        print(f'In {year} an accident of severity {severity} was caused by drink driving:{drink_driving}, speeding: {speed}, fatigue: {fatigue}, defective vehicle: {vehicle_defect}')
        line_count += 1

    #print(elem.tag, elem.attrib, elem.text)

print(f'Processed {line_count} accidents')