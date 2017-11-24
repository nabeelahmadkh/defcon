# Code by Nabeel Ahmad Khan 
# Solution of find step to Genetic Mutation
# Algorithm Used is _______________
# Time Complexity is  _______________

class Solution(object):
    def minMutation(self, start, end, bank):
        count = 0
        for i in range(len(start)):
            if start[i] != end[i]:
                count += 1
        print("The difference in start end is ",count) 
        queue = []
        countArray = []
        initialCount = 1
        tempStart = start
        length = len(bank)
        for i in range(length+1):
            print("tempstart is ",tempStart)
            if tempStart == end:
                return (countArray[len(countArray)-1])
            counting = 0
            if not queue:
                for dna in bank:
                    misMatch = 0
                    for j in range(len(start)):
                        #print("j ",tempStart[j],dna[j])
                        if tempStart[j] != dna[j]:
                            misMatch += 1
                            #print("j",j,tempStart[j], dna[j])
                    if misMatch == 1:
                        queue.append(dna)
                        if counting == 0:
                            countArray.append(initialCount)
                            print("Initial Counter is",initialCount)
                            initialCount += 1
                        print("queue is",queue)
                        counting += 1
                        #bank.remove(dna)
                for i in range(counting):
                    bank.remove(queue[len(queue)-1-i])
                if start in bank:
                    bank.remove(start)
            else:
                counting = 0
                while(queue != None):
                    newqueue = []
                    for dna in bank:
                        misMatch = 0
                        for j in range(len(start)):
                            #print("j ",tempStart[j],dna[j])
                            if tempStart[j] != dna[j]:
                                misMatch += 1
                                #print("j",j,tempStart[j], dna[j])
                        if misMatch == 1:
                            newqueue.append(dna)
                            if counting == 0:
                                countArray.append(initialCount)
                                print("Initial Counter is",initialCount)
                                initialCount += 1
                            print("newqueue is",newqueue)
                            counting += 1
                            #bank.remove(dna)
                    for i in range(counting):
                        if newqueue[len(newqueue)-1-i] in bank:
                            bank.remove(newqueue[len(newqueue)-1-i])
                    if not queue:
                        tempStart = queue.pop(0)
                queue = newqueue
                newqueue = []

            if queue:
                tempStart = queue.pop(0)
        if end in queue:
            return (countArray[len(countArray)-1])
        else:
            return -1


    
variable = Solution()
#output = variable.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"])
#output = variable.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"])
#output = variable.minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"])
#output = variable.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])
#output = variable.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"])
#output = variable.minMutation("AAAAAAAA", "CCCCCCCC", ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA","CCCCCCCC"])
output = variable.minMutation("AAAACCCC", "CCCCCCCC", ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"])
print("output2 of the program is ",output)
