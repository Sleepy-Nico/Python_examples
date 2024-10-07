mil2 = int(input('Mätarställning idag?'))
mil1 = int(input('mätarställning för ett år sen?'))
if mil1 > mil2:
    print("Fel mätarställning angiven")
    #restart program
else:
    
    print('Antal körda mil:', mil2 - mil1)
    liter = float(input('Antal liter bensin? '))
    print(f'Förbrukning per mil: {liter/(mil2-mil1):.2f}')

