#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:56:28 2021

@author: agneskocsis
"""

import requests
import json
import pandas as pd

#https://rarible.com/collection/0xf5b0a3efb8e8e4c201e2a935f110eaaf3ffecb8d

#https://api-reference.rarible.com/
url = "https://api.rarible.com/protocol/v0.1/ethereum/nft/items/byCollection"

querystring = {"collection":"0xb7f7f6c52f2e2fdb1963eab30438024864c313f6","size":"1000"}

response = requests.request("GET", url, params=querystring)

print(response.text)


querystring = {"collection":"0xf5b0a3efb8e8e4c201e2a935f110eaaf3ffecb8d"}

response = requests.request("GET", url, params=querystring)

print(response.text)

####################################################################
#####outerlayer is total, cont.
df = pd.json_normalize(response.json(), 'total', 'continuation')
print(df)


url = "https://api.rarible.com/protocol/v0.1/ethereum/order/orders/sell/byCollection"

querystring = {"collection":"0xf5b0a3efb8e8e4c201e2a935f110eaaf3ffecb8d"}

response = requests.request("GET", url, params=querystring)
print(response.text)
df = pd.json_normalize(response.json(), 'orders')


print(df)

