# iat_dist={1:0.5,3:0.3,6:0.2} iat-> interarrival time
# st_dist={1:0.35,3:0.55,5:0.10} st-> service time
#dist -> distribution prob -> probability
import random
class digitTable:
    def __init__(self,dist):
        self.dist=dist
        self.p=1
        self.range=dict()

    def cummulative_prob(self,probs):
        summ=0
        output=dict()
        for k,v in probs.items():
            summ+=v
            output[k]=summ
        return output
    
    

    def prob_range(self, p=1):
        i = 1
        cp=self.cummulative_prob(self.dist)
        output = dict()
        for k, v in cp.items():
            o = v * (10 ** p)
            if o == 10 ** p:
                o-=1
            output[k] = range(i, int(o)+1)
            i = int(o) + 1
        self.p=p
        self.range=output
        return output
    

iat=digitTable({1:0.5,3:0.3,6:0.2})
st=digitTable({1:0.35,3:0.55,5:0.10})

class simulationTable:
    def __init__(self,custNo,iat,p1,st,p2):
        self.custNo=custNo
        self.iat=iat
        self.st=st
        self.p1=p1
        self.p2=p2
        iat.prob_range()
        st.prob_range(2)
    
    def iat_assign(self):
        output=dict()
        output[1]=0
        for i in range(2,self.custNo+1):
            tmp=random.randint(0,10**self.p1-1)
            if tmp == 0:
                tmp=10**self.p1-1            
            for k,v in self.iat.range.items():
                if tmp in v:
                    output[i]=k
        return output
    def st_assign(self):
        output=dict()
        for i in range(1,self.custNo+1):
            tmp=random.randint(0,10**self.p2-1)
            if tmp == 0:
                tmp=10**self.p2-1
            for k,v in self.st.range.items():
                if tmp in v:
                    output[i]=k
        return output
    
    
    def calc_arrival_time(self):
        iat=self.iat_assign()
        p=0
        output=dict()
        for i in range(1,self.custNo+1):
            output[i]=iat[i]+p
            p=output[i]
        return output

 #debugging:
# simTable=simulationTable(5,iat,1,st,2)
# tmp=digitTable({1:0.5,3:0.3,6:0.2})
# print(tmp.prob_range())
# print(simTable.iat_assign(),'\n',simTable.st_assign(),'\n',end="")
# print(simTable.calc_arrival_time())
