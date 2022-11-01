import requests

url = "https://eth-mainnet.g.alchemy.com/v2/YourAPIKeyHere/getNFTs?owner="
address = 'vitalik.eth'

Cryptopunks     = "&contractAddresses[]=" + "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB"
BAYC            = "&contractAddresses[]=" + "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"
WorldofWomen    = "&contractAddresses[]=" + "0xe785E82358879F061BC3dcAC6f0444462D4b5330"

filterlist =   Cryptopunks + BAYC + WorldofWomen

result = requests.get(url + address + "&withMetadata=False" + filterlist).json()
totalbluechips = result['totalCount']

