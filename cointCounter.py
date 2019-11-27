# Höfundur Tómas Harry Ottósson, tho89@hi.is

import json #notað til að vinna úr JSON hlutum
import os #notað til að kalla smileycoin-cli listunspent
import sys


#Fall sem er comperator til að sortera færslum eftir amount
def jsonSorter(js):
    return js['amount']

#Gildi sem er notað til að byðja notandum um magn af færslum sem eiga að vera notaðar
n=""
while not isinstance(n, int):
    try:
        n = int(input("Please write amount of transaction you would like to use\n"))
    except:
        print("please pick a valid integer!\n")

unspent = os.popen('smileycoin-cli listunspent') # kallar á unix shell command
unspent = unspent.read() # nær í output úr os kallinu

# Ef það er villa að ná í transaction frá veskinu þá hættir forritið
if "error" in unspent: 
    sys.exit(unspent)

jason = json.loads(unspent) # kasta streng yfir í JSON

#Flokkar minnst til lengst
smallest = sorted(jason,key=jsonSorter,reverse=False) 

# Gildi sem sér um að segja notanda hversu mikið af smileycoins hann á
# Til að nota í færsluna
amount = 0.0

# Passar að n er ekki lengra en hversu marga færslur notandi á
if n > len(smallest):
    n = len(smallest)
    print(f'Total txid´s are: {len(smallest)}')

#prentar hversu háa upphæð af coins notandi hefur
for i in range(0,n):
    amount = amount + smallest[i].get('amount')
print(f'Total coins available: {amount}')

# Búa til fylki af hlutum sem er í forminu
# txid:<strengur> svo vout:<int>, þetta er notað í smið af json skjalsin
theTransAction = []
for i in range (0,n):
    theTransAction.append({
        'txid': smallest[i]['txid'],
        'vout': smallest[i]['vout']
    })



#Vistar skjal sem inniheldur json hlutin
with open('smallest.json', 'w') as output:
    json.dump(theTransAction, output)

print("Data saved as smallest.json")