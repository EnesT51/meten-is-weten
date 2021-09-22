dieren_dressuur = int(input('hoeveel jaar heeft u ervaring met dieren-dressuur? '))
jongleren = int(input('hoeveel jaar heeft u ervaring met jongleren? '))
acrobatiek = int(input('hoeveel jaar heef u ervring met acrobatiek? '))
diploma = input('heeft u een MBO-4 ondernemings diploma? ')
Truck_license = input('bent u in bezit van een geldige vrachtwagenrijbewijs? ')
hoed = input('bent u in bezit van een hoge hoed? ')  
geslacht = input('bent u een man of een vrouw? ')
Certificaat = 'ja'
redHair = 'ja'
lengte = 150
gewicht = 90
snor = 'ja'
snor2 = 0

if geslacht == 'man':
    Certificaat = input('heeft u een certificaat? ')
    if Certificaat == 'ja':
        lengte = int(input('hoelang bent u? '))
    if lengte >= 150:
        snor = input('heeft u een snor? ')
    if snor == 'ja':
        snor2 = int(input('hoe breed is uw snor? '))

    else:
         snor2 = 0

if geslacht =='vrouw':
    Certificaat =input('heeft u een certificaat? ')
    if Certificaat =='ja':
        lengte = int(input('hoelang bent u? '))
    if lengte >= 150:
        redHair = input('heeft u rood krullig haar? ')
    if redHair == 'ja':
        haarlengte = int(input('hoe lang is uw haar? '))
else:
    haarlengte = 0

if (dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3)and(gewicht >=90 and lengte >=150 and diploma =='ja' and Truck_license == 'ja' and hoed == 'ja' and(geslacht == 'man' and snor == 'ja' and snor2 >=10 and Certificaat == 'ja') or(redHair =='ja'and Certificaat == 'ja'and haarlengte >=20 and geslacht =='vrouw')): 
    print('gefeliciteerd u bent aangenomen!!')
else:
    print('helaas, u voldoet niet aan de eisen') 



