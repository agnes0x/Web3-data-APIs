import requests

address='0x2A209589119688574E65Cb9Fba546e33012a9edC'

url = "https://api.paperhands.gg/wallet-stats?walletAddress="

result = requests.get(url + address).json()
paperhands = result['paperhandsReportSummary']['totalLossInEth']