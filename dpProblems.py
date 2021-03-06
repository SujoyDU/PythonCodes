#Tower of Hanoi
def Rearrange(numOfDisks,sourceRod,destinationRod,middleRod):
    if(numOfDisks ==1):
        print("moved "+str(numOfDisks)+ " from "+sourceRod+" to "+destinationRod)
        return
    Rearrange(numOfDisks-1,sourceRod,middleRod,destinationRod)
    print("moved "+ str(numOfDisks)+ " from "+ sourceRod +" to " + destinationRod)
    Rearrange(numOfDisks-1,middleRod,destinationRod,sourceRod)


def TowerOfHanoi(numOfDisks):
    Rearrange(numOfDisks,'S','D','M')



#Coin Change Problem
def CoinChange(coinsList,amount):
    amountList = [1000000000 for i in range(amount+1)]
    coinIndex = [-1 for i in range(amount+1)]
    amountList[0] =0
    for coin in coinsList:
        for i in range(coin,amount+1):
            if(amountList[i] > 1+amountList[i-coin]):
                amountList[i] = 1+amountList[i-coin]
                coinIndex[i] = coinsList.index(coin)

    print("Minimum Number of coins for "+ str(amount)+" is " +str(amountList[-1]))

    minCoins ={}
    coinTotal = amount
    while (coinIndex[coinTotal] != -1):
        coin = coinsList[coinIndex[coinTotal]]
        if coin not in minCoins:
            minCoins[coin] = 1
        else: minCoins[coin] +=1
        coinTotal = coinTotal-coin

    for coin, numOfCoins in minCoins.items():
        print(str(numOfCoins)+" times coin "+str(coin))




if __name__ == ('__main__'):
    print("Tower Of Hanoi")
    TowerOfHanoi(3)
    # print("Coin change")
    # coinsList = [10,5,1,20]
    # amount = 54
    # CoinChange(coinsList,amount)
