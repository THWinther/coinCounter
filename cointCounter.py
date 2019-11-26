import json #notað til að vinna úr listunspent
import os #notað til að kalla smileycoin-cli listunspent


def jsonSorter(js):
    return js['amount']

unspent = os.popen('smileycoin-cli listunspent') # tekur inn unix shell command og skilar hvað er prentað í breytu
unspent = unspent.read() # jason er núna útak úr os kallinu
jason = json.loads(unspent)
smallest = sorted(jason,key=jsonSorter,reverse=False)
print(jason[0])
print(smallest[0])
