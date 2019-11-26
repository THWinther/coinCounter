import json #notað til að vinna úr listunspent
import os #notað til að kalla smileycoin-cli listunspent


def jsonSorter(js):
    return js['amount']

n=""
while not isinstance(n, int):
    try:
        n = int(input("Please pick number of txids you would like to clear!\n"))
    except:
        print("please write a valid integer!\n")

unspent = os.popen('smileycoin-cli listunspent') # tekur inn unix shell command og skilar hvað er prentað í breytu
unspent = unspent.read() # jason er núna útak úr os kallinu
jason = json.loads(unspent)
smallest = sorted(jason,key=jsonSorter,reverse=False)

for i in range(0,n):
    print(smallest[i])