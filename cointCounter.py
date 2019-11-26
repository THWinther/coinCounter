# Höfundur Tómas Harry Ottósson, tho89@hi.is
import json #notað til að vinna úr listunspent
import os #notað til að kalla smileycoin-cli listunspent

class shortTransaction:
    def __init__(self,txid,vout):
        self.txid = txid
        self.vout = vout


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

unspent = os.popen('smileycoin-cli listunspent') # tekur inn unix shell command og skilar hvað er prentað í breytu
unspent = unspent.read() # jason er núna útak úr os kallinu
jason = json.loads(unspent) # færir hreinan streng yfiri í JSON
smallest = sorted(jason,key=jsonSorter,reverse=False) #Flokkar minnst til lengst 

# Gildi sem sér um að segja notanda hversu mikið af smileycoins hann á
# Til að nota í færsluna
amount = 0.0

# Passar að n er ekki lengra en hversu marga færslur notandi á
if n > len(smallest):
    n = len(smallest)
    print(f'Total txid´s are: {len(smallest)}')

#prentar hversu háa upphæð af coins notandi hefur
for i in range(0,n):
    amount =amount+smallest[i].get('amount')
print(f'Total coins available: {amount}')

theTransActionArr = []
for p in smallest:
    tempObj = shortTransaction(p["txid",p["vout"]])

theTransaction = json.dumps(theTransActionArr)
print(theTransaction)