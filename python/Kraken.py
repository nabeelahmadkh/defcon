# Code by Nabeel Ahmad Khan 
# Solution of Unique path in Kraken Game 
# Algorithm Used is Recursion 
# Time Complexity is Polynomial 

# Solution using Recursion
class Solution(object):
    def krakenCount(self, m, n):
        #print("1 m n",m,n)
        if ((m==1) & (n==1)):
            #print("2")
            return 1
        elif ((m>1) & (n>1)):
            #print("m n ",m,n)
            return (self.krakenCount(m-1,n) + self.krakenCount(m,n-1) + self.krakenCount(m-1,n-1))
        elif ((m==1) & (n>1)):
            #print("3")
            return self.krakenCount(m,n-1)
        elif ((m>1) & (n==1)):
            #print("4 m n",m,n)
            return self.krakenCount(m-1,n)
        else:
            #print("5")
            return 0 

# Solution using Dynamic Programming
class Solution2(object):
    def krakenCount(self,m,n):
        krakenMatrix = [[1 for i in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                krakenMatrix[i][j] = krakenMatrix[i-1][j-1] + krakenMatrix[i-1][j] + krakenMatrix[i][j-1]
        print("kraken matrix ",krakenMatrix[m-1][n-1])
        return (krakenMatrix[m-1][n-1])


variable = Solution()
output = variable.krakenCount(10,10)
print("output2 of the program is ",output)

variable2 = Solution2()
output = variable.krakenCount(10,10)
print("output1 of the program is ",output)
