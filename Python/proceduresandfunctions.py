def fourcandles(numberofcandles=4):
    candlelist = []
    for i in range(numberofcandles):
        candlelist.append('candle')
    return candlelist



print('Here are your first four candles, for free!', end="\n\n\n")

returnlist = fourcandles()
print(returnlist)

moreleons = '4'

while moreleons !=0:
    moreleons = int(input('How many more candles would out like?: '))
    if moreleons !=0:
        returnlist = fourcandles(moreleons)
        print(returnlist)

