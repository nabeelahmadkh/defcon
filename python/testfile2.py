class Solution(object):
    def coinChange(self, coins, amount):
        if not coins:
            return 0

        monValue = amount
        output = []
        biggest = coins[0]
        for coin in coins:
            if (coin > biggest) & (coin <= amount):
                biggest = coin
        coins.remove(biggest)

        mod = amount % biggest
        quotient = amount/biggest
        for i in range(quotient):
            output.append(biggest)

        while(mod != None):
            if coins:
                biggest = coins[0]
            else:
                break
            for coin in coins:
                if (coin > biggest) & (coin <= mod):
                    biggest = coin
            if biggest == 0:
                break
            quotient = mod/biggest
            mod = mod % biggest
            for i in range(quotient):
                output.append(biggest)
            coins.remove(biggest)

        sum = 0    
        for coin in output:
            sum += coin
        if sum != monValue:
            return 0
        print("output is ",output)
        return len(output)



variable = Solution()
output = variable.coinChange([20,10,5,1],53)