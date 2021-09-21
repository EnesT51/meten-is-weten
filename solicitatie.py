dieren_dressuur = int(input('hoeveel jaar heeft u ervaring met dieren-dressuur? '))
jongleren = int(input('hoeveel jaar heeft u ervaring met jongleren? '))
acrobatiek = int(input('hoeveel jaar heef u ervring met acrobatiek? '))

if dieren_dressuur >= 4 or jongleren >= 5 or acrobatiek >= 3:
    opleiding = input('heeft u een MBO-4 ondernemings opleiding gevlogd? ')
    if opleiding == 'ja':
        diploma = input('heeft u uw opleiding met succes afgerond? ')
        if diploma == 'nee':
            print('helaas, u voldoet niet aan ons eisen')
    else:
        print('helaas, u voldiet niet aan ons eisen') 



else:
    Truck_licnese = input('ben u in bezit van een vrachtwagen rijbewijs? ')
    if Truck_licnese == 'ja':
        hoed = input('bent u bezit van een hoge hoed? ')

    else:
        print('helaas, u voldoet niet aan ons eisen')

    if hoed == 'ja':
        geslacht = input('bent u een man of een vrouw? ')

    else:
        print('helaas, u voldoet niet aan ons eisen')
    if geslacht == 'man':
        snor = int(input('heeft u een snor zoja, hoe breed is deze in cm? '))
    elif geslacht == 'vrouw':
            haar = int(input('heeft u roodkrullig haar zoja, hoe lang is uw haar in cm? ')) 
    if    snor >= 10 or haar >= 20:
        lengte = int(input('wat is uw lengte? '))

    else:
        print('helaas, u voldoet niet aan ons eisen')

    if lengte >= 150:
        gewicht = int(input('wat is uw gewicht type het in KG '))

    else:
        print('helaas, u voldoet niet aan ons eisen')

    if gewicht >= 90:
        Certificaat = input('heeft u een certificaat? ')

    else:
        print('helaas, u voldoet niet aan ons eisen')

    if Certificaat == 'ja':
        print('gefeliciteerd u bent de juiste kanidaat waar wij naar opzoek zijn. U bent aangenomen!')

    else:
        print('helaas, u voldoet niet aan de eisen. Helaas u bent niet aangenomen')
