while True:
    g=input('benzinin gallon ile miqdarini daxil edin ')
    if g.isnumeric():
        g=float(g)
        litr=3.784*g
        print('litr = ',litr)
        barrel=g/19.5

        print('barrel = ',barrel)
        co=20*g

        print('CO2 = ',co)
        btu=115000*g

        print('BTU = ',btu)
        usd=4*g

        print('Dollar ile qiymeti = ',usd)
    else:
        print('reqem daxil edin')
        continue