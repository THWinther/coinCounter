# coinCounter

## Description
 A python Script that gets the n smallest tx:ids from you smilecoin wallet and builds a JSON to use in the first part of createrawtransaction. 
 
 It will also tell you how many coins you have when it is done running.

## Requirements
 Python3
 
 So far it only works with the smilecoin-cli for Linux

## Usage
just type 'python3 coinCounter.py'

it will ask you how many txids you would like to place into the transaction


It will then save a json file in the directory it was ran in (smallest.json)
