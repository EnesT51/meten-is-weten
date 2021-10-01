game = input('welkom bij The shootergame wil je de game spelen ja/nee? ')
vijand2 = (200)
rocketLauncher = False
Granaat = False

if game == 'ja': 
    huis = input('je schuilt in een huis, er wachten drie vijanden buiten op jou een vijand op dak en een vijand achter auto en laatstevijand achter een muur welke van de drie wil je uitschakelen? kies uit> auto/muur/dak ')
    if huis == 'auto':
        answer = input("ga naar de kelder in de kast ligt er een rocketlauncher wil je die pakken ja/nee? ")
        if answer == "ja":
            rocketLauncher = True    
            answer2 = input("in de kleder ligt ook aantal granaten wil je die pakken ja/nee? ")
            if answer2 =="ja":
                Granaat = True
                vijand1 = input('wil je de vijand uitschakelen ja/nee? ')
                if vijand1 == 'ja' and rocketLauncher ==True and Granaat == True:
                    print('vijand is vernietigd!!') 

            else:
                print("helaas je hebt de vijand niet kunnen vernietigen je hebt de game verloren begin opnieuw") 
        else:
            print("helaas")

    elif huis == "dak":
        print('ga naar de schuur pak de sniper')
        vijand2 =  int (input('je heb de sniper gepakt hoeveel meter is de vijnad van je vandaan tpye het in cijfers? '))
        if vijand2 >=200:
            vijand2 = input("je hebt de 8x scope gepakt, wil je de vijand uitschakelen ja/nee? ") 
        elif vijand2 <=200: 
            vijand2 = input("de vijand is niet zo ver wil je de vijand uitschakelen ja/nee? ")
        if vijand2 =="ja":
                print("BOOOOOOM HEADSHOT!! vijand is uitgeschakeld!!")
        else:
            print("je hebt de vijand niet kunnen uitschakelen je hebt de game verloren")

    else:
        huis = input("er liggen aantal granaten in de kast wil je wil je deze pakken ja/nee? ")
        if huis == "ja":
            granaat = int(input("hoeveel granaten pak je? tpye het is cijfers "))
            if granaat != 1:
                print("je hebt genoeg granaten gepakt je heb het gegeooit en de vijand is dood je hebt gewonnen!") 
            else:
                print("je hebt te weinig granaten gepakt het was niet genoeg je hebt verloren!. ")

else:
  print('jammer!') 