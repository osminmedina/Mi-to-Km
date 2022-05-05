print('How many miles did you run? ')
miles = input()
kms = float(miles)/1.609
kms = round(kms, 2)

print(f"Your {miles}mi run was {kms}km")
