import requests
url = "https://api.poap.xyz/actions/scan/"
address = 'enteraddress'

result = requests.get(url + address).json()

totalpoaps = len(result)