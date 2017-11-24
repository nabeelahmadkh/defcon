# Code by Nabeel Ahmad Khan 
# Solution of find step to Genetic Mutation
# Algorithm Used is _______________
# Time Complexity is  _______________

class Solution(object):
    def minMutation(self, start, end, bank):
        count = 0
        if not bank:
            return -1
        for i in range(len(start)):
            if start[i] != end[i]:
                count += 1
        print("The difference in start end is ",count) 
        queue = []
        tempStart = start
        startLength = len(start)
        stepCount = 0
        bankLength = len(bank)
        for i in range(bankLength):
            print("tempstart is ",tempStart)
            print("queue is ",queue)
            print("bank is ",bank)
            if tempStart == None:
                stepCount = 0
                break
        
            if (end in queue) | (tempStart == end):
                break
            
            if not queue:
                #mismatchCount = 0
                for dna in bank:
                    mismatchCount = 0
                    for j in range(startLength):
                        if(tempStart[j] != dna[j]):
                            mismatchCount += 1
                    if mismatchCount == 1:
                        queue.append(dna)
                for k in queue:
                    bank.remove(k)
                if tempStart in bank:
                    bank.remove(tempStart)
                tempStart = None
                stepCount += 1
            else:
                tempQueue = []
                for dnaQueue in queue:
                    #mismatchCount = 0
                    for dnaBank in bank:
                        mismatchCount = 0
                        for l in range(startLength):
                            if(dnaQueue[l] != dnaBank[l]):
                                mismatchCount += 1
                        if mismatchCount == 1:
                            tempQueue.append(dnaBank)
                for dnaBank in bank:
                    mismatchCount = 0
                    for l in range(startLength):
                        if(tempStart[l] != dnaBank[l]):
                            mismatchCount += 1
                    if mismatchCount == 1:
                        tempQueue.append(dnaBank)
                for dna in tempQueue:
                    if dna in bank:
                        bank.remove(dna)
                queue = tempQueue
                tempQueue = []
                stepCount += 1
            print("queue at the end is ",queue)
            if queue:
                tempStart = queue.pop(0)
    
        if stepCount == 0:
            return -1
        else:
            return stepCount


    
variable = Solution()
#output = variable.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"])
#output = variable.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])
#output = variable.minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"])
#output = variable.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])
#output = variable.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"])
#output = variable.minMutation("AAAAAAAA", "CCCCCCCC", ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA","CCCCCCCC"])
#output = variable.minMutation("AAAACCCC", "CCCCCCCC", ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"])
#output = variable.minMutation("AACCGGTT", "AAACGGTA", [])
#output = variable.minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"])
output = variable.minMutation("AAAAAAAA", "GGAAAAAA", ["GAAAAAAA","AAGAAAAA","AAAAGAAA","GGAAAAAA"])

print("output2 of the program is ",output)
