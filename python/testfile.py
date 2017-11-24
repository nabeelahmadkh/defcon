def count_coins(coinDenominations, monetaryValue):
    if not coinDenominations:
        return [0]

    monValue = monetaryValue
    output = []
    biggest = coinDenominations[0]
    for coins in coinDenominations:
        if (coins > biggest) & (coins < monetaryValue):
            biggest = coins
    coinDenominations.remove(biggest)

    mod = monetaryValue % biggest
    quotient = monetaryValue/biggest
    for i in range(quotient):
        output.append(biggest)

    while(mod != None):
        if coinDenominations:
            biggest = coinDenominations[0]
        else:
            break
        for coins in coinDenominations:
            if (coins > biggest) & (coins < mod):
                biggest = coins
        if biggest == 0:
            break
        quotient = mod/biggest
        mod = mod % biggest
        for i in range(quotient):
            output.append(biggest)
        coinDenominations.remove(biggest)

    sum = 0    
    for coins in output:
        sum += coins
    if sum != monValue:
        return [0]
    print("output is ",output)
    return output


count_coins([20,10,5,1],53)