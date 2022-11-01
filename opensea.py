import requests
import json
import pandas as pd

###############################################################################################################################
#Collection
headers = {"X-API-KEY": "yourapikey"}
url1 = "https://api.opensea.io/api/v1/assets"
querystring1 = {"order_direction":"desc","offset":"0","limit":"200","collection":"cryptopunks"}
collection = requests.request("GET", url1, headers=headers, params=querystring1)
print(collection.text)
df = pd.json_normalize(collection.json(), 'assets')
print(df)
df.to_excel('collection.xlsx')

####################################################################
#Sales
url2 = "https://api.opensea.io/api/v1/events"
querystring2 = {"collection_slug":"cryptopunks","event_type":"successful","only_opensea":"false","offset":"0","limit":"800"}

headers = {
    "Accept": "application/json",
    "X-API-KEY": "yourapikey"
}

sales = requests.request("GET", url2, headers=headers, params=querystring2)
dfs = pd.json_normalize(sales.json(), 'asset_events')
print(dfs)
dfs.to_excel('sales.xlsx')
