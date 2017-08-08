# Python Program for HackerRank Problem Trans.
# Code started on 11/02/2015
# Last Edit on 07/08/2017
# Code by Nabeel Ahmad Khan


oper= ['+','-','*','/','^']
paren= ['(',')']

t=int(raw_input())

for case in range(t):
    exp=str(raw_input())
    stk=[]
    lexp=list(exp)
    outp=[]

    for token in lexp:
        if token not in oper and token not in paren:
            outp.append(token)
        elif token in oper:
            if not stk:
                stk.append(token)
            else:
                if stk[-1] not in paren:
                    if oper.index(token) <= oper.index(stk[-1]):
                        outp.append(stk[-1])
                        stk[-1]=token
                    else:
                        stk.append(token)
                if stk[-1]=='(':
                    stk.append(token)
        else:
            if not stk:
                stk.append(token)
            else:
                if token=='(':
                    stk.append(token)
                else:
                    temp=stk[-1]
                    while(temp!='('):
                        outp.append(temp)
                        stk.pop()
                        temp=stk[-1]
                    stk.pop()
    while(len(stk)>0):
        outp.append(stk.pop())

    print ''.join(outp)
        
