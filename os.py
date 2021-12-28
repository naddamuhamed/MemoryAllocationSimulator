import copy
from tabulate import tabulate


def firstfit(block, proc):
 ballo = []
 pnotallo=[]
 b1=copy.deepcopy(block)
 p1=copy.deepcopy(proc)
 fit=False
 for x in proc:
    for y in b1:
        if y >= x:            
            ballo.append(y)
            b1.remove(y)
            fit=True
            break
    if fit==False:
        pnotallo.append(x)
        p1.remove(x)
    else: 
        fit=False      

 return ballo,pnotallo,p1,b1

def bestfit(block, proc):
 b2=copy.deepcopy(block)
 b2.sort()
 ballo1,pnotallo1,pallo1,bnotallo=firstfit(b2,proc)
 return ballo1,pnotallo1,pallo1,bnotallo

def worstfit(block, proc):
 b3=copy.deepcopy(block)
 b3.sort(reverse=True)
 ballo2,pnotallo2,pallo2,bnotallo=firstfit(b3,proc)
 return ballo2,pnotallo2,pallo2,bnotallo

def pb():
    block = []
    n = int(input("\nEnter number of blocks: "))
    print("\nEnter block sizes: ")
    for i in range(0, n):
        e = int(input())
        block.append(e)

    proc = []
    n = int(input("\nEnter number of processes: "))
    print("\nEnter process sizes: ")
    for i in range(0, n):
        e = int(input())
        proc.append(e)
    return block,proc    



n=True
while(n==True):
    print("\nFor first fit press 1 \nFor best fit press 2 \nFor worst fit press 3 \nTo quit press 0 ")
    x=int(input())
    match x:
        case 1:
            block,proc=pb()
            ballo,pnotallo,pallo,bnotallo=firstfit(block,proc)
            data2=[["Free blocks"]+bnotallo,["Blocks allocated"]+ballo,["Processes allocated"]+pallo,["Processes not allocated"]+pnotallo]
            print(tabulate(data2,headers=["First fit method"],tablefmt="fancy_grid"))
        case 2:
            block,proc=pb()
            ballo,pnotallo,pallo,bnotallo=bestfit(block,proc)
            data2=[["Free blocks"]+bnotallo,["Blocks allocated"]+ballo,["Processes allocated"]+pallo,["Processes not allocated"]+pnotallo]
            print(tabulate(data2,headers=["Best fit method"],tablefmt="fancy_grid"))
        case 3:
            block,proc=pb()
            ballo,pnotallo,pallo,bnotallo=worstfit(block,proc)
            data2=[["Free blocks"]+bnotallo,["Blocks allocated"]+ballo,["Processes allocated"]+pallo,["Processes not allocated"]+pnotallo]
            print(tabulate(data2,headers=["Worst fit method"],tablefmt="fancy_grid"))
        case 0:
            print("\nThank you! Bye")
            n=False

        case _:
            print("\nPlease enter a valid value for x\n")    
                

exit()






