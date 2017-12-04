import sys
import t_data
from time import time

def dailyTemperatures1(temperatures):
    t=time()
    long_ar=[]
    longitude=len(temperatures)
    def lam(array,point,position,count):
        if position >= longitude:
            return 0
        elif array[position] >array[point]:
            return count
        return lam(array,point,position+1,count+1)    
    while True:
        steps=0
        current=temperatures[0]
        del(temperatures[0])
        if max(temperatures) <= current:
            long_ar.append(0)
            continue
        for i in range(len(temperatures)):
            steps+=1
            if current > temperatures[i]:
                long_ar.append(steps)
    print(time.time() - t)
    return long_ar

data=[73,74,75,71,69,72,76,73]

for item in data:
    print(item,type(item))





def dailyTemperatures2(tem):
    tmp=[[],[]]
    #tmp1=[]
    mx=max(tem)
    result=list()
    for i in range(len(tem)):
        current=tem[i]
        append=1
        if current == mx:
            result.append([i,0])
            append=0
        for r in tmp[0]:
            pos,val,step=r
            step +=1
            if current > val:
                result.append([pos,step])
                #tmp.remove(r)
                continue
            
            tmp[1].append([pos,val,step])
        #for ir in tmp:
            #if ir == 0:
                #tmp.remove(ir)
        if append==1:
            tmp[1].append([i,current,0])
        #tt=time()
        tmp[0],tmp[1]=tmp[1],[]
        #tmp[1]=[]
        #print(time()-tt)
    for item in tmp[0]:
        result.append([item[0],0])
    print(result)
    
    
    #for i in range(len(tem)):
        #no_append=0
        ##if tem[i] == mx:
            ##result.append([i,0])
            ##no_append=1
        #for item in tmp:
            #position,value,steps=item
            ##print(position,steps)
            #if tem[i] > value:
                #if position == 3:
                    #print(steps)
                #result.append([position,steps + 1])
                #tmp.remove(item)
                #continue
            #tmp.remove([position,value,steps])
            #tmp.append([position,value,steps + 1])
        #if no_append == 0:
            #tmp.append([i,tem[i],0])
    l=[]
    ##print(time() - t)
    #if not tmp == []:
        #for item in tmp:
            #position=item[0]
            #result.append([position,0])
    result.sort(key=lambda x: x[0])
    
    for item in result:
        l.append(item[1])
    return result
        
        
            
def daily(tem):
    tmp={}
    for i in range(len(tem)):
        dat=tem[i]
        if not tem[i] in tmp:
            tmp[tem[i]]=[i]
        else:
            tmp[tem[i]].append(i)
        
    print(tmp)
    array_keys=list(key for key in tmp)
    array_keys.sort()
    temp_result=[]
    for item in tmp[array_keys[-1]]:
        temp_result.append([item,0])
    print(temp_result)
    
    #for k,v in tmp.items():
        #print(k)

#print(dailyTemperatures2(data))
#print(dailyTemperatures(data))
print(daily(t_data.data1))