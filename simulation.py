# iat_dist={1:0.5,3:0.3,6:0.2}
# st_dist={1:0.35,3:0.55,5:0.10}
import random
class digitTable:
    def __init__(self,dist):
        self.dist=dist
        self.p=1
        self.range=dict()

    def cumP(self,props):
        summ=0
        output=dict()
        for k,v in props.items():
            summ+=v
            output[k]=summ
        return output
    # self.cum=cumP(self.dist)
    
    

    def prop_range(self, p=1):
        i = 1
        cum=self.cumP(self.dist)
        output = dict()
        for k, v in cum.items():
            o = v * (10 ** p)
            output[k] = range(i, int(o)+1)
            i = int(o) + 1
        self.p=p
        self.range=output
        # return output
    

iat=digitTable({1:0.5,3:0.3,6:0.2})
st=digitTable({1:0.35,3:0.55,5:0.10})
# print(iat.prop_range())

class simulationTable:
    def __init__(self,cust,iat,p1,st,p2):
        self.cust=cust
        self.iat=iat
        self.st=st
        self.p1=p1
        self.p2=p2
        iat.prop_range()
        st.prop_range(2)
    
    def iat_ass(self):
        output=dict()
        error=dict()
        output[1]=0
        for i in range(2,self.cust+1):
            tmp=random.randint(1,10**self.p1)
            if tmp == 10**self.p1:
                tmp=0
            for k,v in self.iat.range.items():
                if tmp in v:
                    output[i]=k
                else:
                    error[i]=['rnd=',tmp,'key=',k,'value=',v]
        # print(error)
        return output
    def st_ass(self):
        output=dict()
        for i in range(1,self.cust+1):
            tmp=random.randint(1,10**self.p2)
            if tmp == 10**self.p2:
                tmp=0
            for k,v in self.st.range.items():
                if tmp in v:
                    output[i]=k
        return output
    
    def calc_arrival_time(self):
        p=0
        output=dict()
        for i in range(1,self.cust+1):
            output[i]=self.iat_ass()[i]+p
            print(output[i])
            p=output[i]
        return output


stAss=simulationTable(5,iat,1,st,2)
print(stAss.iat_ass(),'\n',stAss.st_ass(),'\n',end="")
# print(stAss.calc_arrival_time())
