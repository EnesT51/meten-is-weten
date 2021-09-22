dieren_dressuur = int(input('hoeveel jaar heeft u ervaring met dieren-dressuur? '))
jongleren = int(input('hoeveel jaar heeft u ervaring met jongleren? '))
acrobatiek = int(input('hoeveel jaar heef u ervring met acrobatiek? '))
diploma = input('heeft u een MBO-4 ondernemings diploma? ')
Truck_license = input('bent u in bezit van een geldige vrachtwagenrijbewijs? ')
hoed = input('bent u in bezit van een hoge hoed? ')  
Certificaat = input('heeft u een certificaat? ')
Lengte = int (input('hoe lang bent u? '))
gewicht =  int (input('wat is uw gewicht? '))
geslacht = input('bent u een man of een vrouw? ')


if geslacht == 'man':
    snor = input('heeft u een snor? ')
    if snor == 'ja':
        snor2 = int(input('hoe breed is uw snor? '))
    else:
         snor2 = 0

if geslacht =='vrouw':
    redHair = input('heeft u rood krullig haar? ')
    if redHair == 'ja':
        haarlengte = int(input('hoe lang is uw haar? '))
else:
    haarlengte = 0

if (dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3) and diploma == 'ja' and Truck_license == 'ja' and hoed == 'ja' and Certificaat == 'ja' and Lengte > 150 and gewicht >90 and ((geslacht == 'man' and snor2 >10) or (geslacht == 'vrouw' and haarlengte >20)):       
    print('gefeliciteerd u bent aangenomen!!')
else:
    print('helaas, u voldoet niet aan de eisen')