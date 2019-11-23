import json #notað til að vinna úr listunspent
import os #notað til að kalla smileycoin-cli listunspent

unspent = os.popen('ls') # tekur inn unix shell command og skilar hvað er prentað í breytu
jason = unspent.read() # jason er núna útak úr os kallinu
print(jason) # til að prufa hvað kemur