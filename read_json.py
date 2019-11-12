import json

# importing data from a json file is called deserialization

with open('roadcrash_factors.json', 'r') as roadcrash_factors_file:
    roadcrash_factors_data = json.load(roadcrash_factors_file)

line_count = 0

for record in roadcrash_factors_data['records']:
    year = record[1]
    severity = record[3]
    drink_driving = record[4]
    speed = record[5]
    fatigue = record[6]
    vehicle_defect = record[7]
    print(f'In {year} an accident of severity {severity} was caused by drink driving:{drink_driving}, speeding: {speed}, fatigue: {fatigue}, defective vehicle: {vehicle_defect}')
    line_count += 1

print(f'Processed {line_count} accidents')