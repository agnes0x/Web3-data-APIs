import json
import requests
#Price estimator
fromChain = "DAI"
toChain =  "POL" #optimism
fromToken = "0x4ECaBa5870353805a9F068101A40E0f32ed605C6"
toToken = "0x7ceb23fd6bc0add59e62ac25578270cff1b9f619"
fromAmount = "1000000"
fromAddress = "0x552008c0f6870c2f77e5cC1d2eb9bdff03e30Ea0"


def getStats(self, fromChain, toChain, fromToken, toToken, fromAmount, fromAddress):
    url = "https://staging.li.quest/v1/quote?"
    queryBridge = "&allowBridges=optimism&allowBridges=avalanche&allowBridges=polygon&allowBridges=hop&allowBridges=multichain&allowBridges=cbridge&allowBridges=connext&allowBridges=hyphen&allowBridges=arbitrum"
    queryExchange = "&allowExchanges=1inch&allowExchanges=paraswap&allowExchanges=openocean&allowExchanges=0x"
    query = url + "fromChain=" + fromChain + "&toChain=" + toChain + "&fromToken=" + fromToken + "&toToken=" + toToken + "&fromAddress=" + fromAddress + "&fromAmount=" + fromAmount + queryBridge + queryExchange
    headers = {"Accept": "application/json"}
    response = requests.get(query, headers=headers)
    data = response.json()
    stepsType=[]
    stepsTool=[]
    stepsID=[]
    estimateMinReceive=[]
    for i, item in enumerate(data.get("includedSteps")):
        stepsType.append(data.get("includedSteps")[i].get("type"))
        stepsTool.append(data.get("includedSteps")[i].get("tool"))
        stepsID.append(data.get("includedSteps")[i].get("id"))
        estimateMinReceive.append(data.get("estimate").get("toAmountMin"))
        
    return stepsType, stepsTool, stepsID,estimateMinReceive
    
    #bridging fee: assuming we migrate usd2usd, weth2weth etc -> 0th step will be bridging.
    #as estimated
    #estimateCost = (float(data.get("includedSteps")[0].get("estimate").get("fromAmountUSD")) - float(data.get("includedSteps")[0].get("estimate").get("toAmountUSD")))/float(data.get("includedSteps")[0].get("estimate").get("fromAmountUSD"))
    #actual fee percenatges
    #gasFee = data.get("includedSteps")[0].get("estimate")["feeCosts"][0].get("percentage")
    #relayFee =  data.get("includedSteps")[0].get("estimate")["feeCosts"][1].get("percentage")
    #routerFee =  data.get("includedSteps")[0].get("estimate")["feeCosts"][2].get("percentage")
