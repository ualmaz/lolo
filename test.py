for x in range(1, 100):
    if x % 3 == 0:
        print('Lolo')
    elif x % 5 == 0:
        print ('Pepe')
    elif x % 3 and x % 5 == 0:
        print('LoloPepe')
    else:
        print(x)
