arr=["01100110","01100001","01110011",
     "01110100","01100101","01110010",
     "01110000","01110101","01110011",
     "01110011","01111001","01100011",
     "01100001","01110100","01100110",
     "01101001","01101100","01101101",
     "01101000","01100101","01100001",
     "01100100","01100101","01110010",
     "01110011","01110011","01110101",
     "01101101"]



def plusser(bbbs_array):
    result=''
    def worker(result,bbb):
        temp=[]
        if result=='':
            #print(bbb) 
            return bbb
        for a,b in zip(result.split(),bbb.split()):
            if (a == "0" and b == "0") or (a == "1" and b == "1" ):
                temp.append("0")
            elif (a == "1" and b== "0") or (a == "0" and b == "1"):
                temp.append("1")
        return ''.join(temp)
    for bbb in bbbs_array:
#        print(bbb)
        res_tmp=result
        print(result)
        result=worker(res_tmp,bbb)
#        print(result)
    return result


print(plusser(arr))

