import csv

with open('roadcrash_factors.csv') as roadcrash_factors_file:
<<<<<<< HEAD
    csv_reader = csv.reader(roadcrash_factors_file)
=======
    csv_reader = csv.reader(roadcrash_factors_file, delimiter=',')
>>>>>>> 584f9b90fa74cafd30ae8e9f49271f533ba7bd64
    line_count = 0
    for row in roadcrash_factors_file:
        row = list(row.split(','))
        
        if line_count == 0:
            line_count += 1
        else:
            year = row[1]
            severity = row[3]
            drink_driving = row[4]
            speed = row[5]
            fatigue = row[6]
            vehicle_defect = row[7]
            print(f'In {year} an accident of severity {severity} was caused by drink driving:{drink_driving}, speeding: {speed}, fatigue: {fatigue}, defective vehicle: {vehicle_defect}')
            line_count += 1
        
        
    print(f'Processed {line_count-1} accidents')
