import requests
import json
import pandas as pd

#Cryptopunks contract adress   0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB

####################################################################################################################################################################################################################
####################### All token transaction by contract address
#https://etherscan.io/apis#accounts
response = requests.get('https://api.etherscan.io/api?module=account&action=tokentx&contractaddress=0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB&page=1&offset=3&sort=asc&apikey=3SJEA6GFDBZNAGPYG26SRTR5JF9MW7DNCB')
print(response.text)
print(response.json())
type(response)

#   {"status":"1","message":"OK","result": 
#   [{"blockNumber":"3919706","timeStamp":"1498251906","hash":"0xb28b
#
# first section  not needed

resp2 = response.text
print(resp2)

resp3 = resp2.replace('}]}','}]')
print(resp3)

resp4 = resp3.replace('{"status":"1","message":"OK","result":','')
#resp4 = resp3.split("[",1)
print(resp4)

data = json.loads(resp4)
print(data)

dfs = pd.json_normalize(data)
print(dfs)

dfs.to_excel('tx_history_by_adress.xlsx')


####################################################################################################################################################################################################################
####################### details of 1 transaction
#https://etherscan.io/apis#proxy
#eth_getTransactionByHash
#Returns the information about only (1) transaction requested by transaction hash
response1 = requests.get('https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash=0xb28b5f2c186bf534e4fc4b8604b1496c9632e42269424f70ef1bdce61ea8ba52&apikey=YourApiKeyToken')
resp2 = response1.text
resp3 = resp2.replace('}}','}')
resp4 = resp3.replace('{"jsonrpc":"2.0","id":1,"result":','')
data = json.loads(resp4)
dfs2 = pd.json_normalize(data)
dfs2.to_excel('single_tx_details.xlsx')
############### "The numbers mason! what do they mean?" 
'               acceptBidForPunk(uint256 punkIndex, uint256 minPrice)'
'input column = methodID                   + input1          + input2'
'input column =   10                       + 64              + 64 characters'

#input_original: 0x23165b750000000000000000000000000000000000000000000000000000000000000220000000000000000000000000000000000000000000000000002386f26fc10000
'acceptBidForPunk' #methodID:0x23165b75

'punkIndex' #input1:0000000000000000000000000000000000000000000000000000000000000220
tokenid = int("0000000000000000000000000000000000000000000000000000000000000220", 16)
print(tokenid)

'minPrice'#input2:000000000000000000000000000000000000000000000000002386f26fc10000
price = int("000000000000000000000000000000000000000000000000002386f26fc10000", 16)
print(price)

print(dfs2[input])

dfs2['methodID'], dfs2['tokenid'], dfs2['price'] = map(dfs2['input'].str.slice, [0, 10, 64], [10, 64, 128])

dfs2['tokenid'] = int(dfs2['tokenid'].value, 16)
dfs2['price'] = int(dfs2['price'].value, 16)
dfs2['price']

#######

eth_getTransactionReceipt

Returns the receipt of a transaction by transaction hash

https://api.etherscan.io/api?module=proxy&action=eth_getTransactionReceipt&txhash=0x1e2910a262b1008d0616a0beb24c1a491d78771baa54a33e66065e03b1f46bc1&apikey=YourApiKeyToken