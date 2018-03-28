import numpy as np
class Columner_cipher:
    
	
    list1=[]
    list2=[]
    pt=[]
    pt1=[]
    ct=[]
    ct=[]
    k=[]
    k1=[]
    n=1
    key=[]
    k3=[]
    k4=[]
    inverseKey=[]
    result=[]
	
    planeText=""
    planeText1=""
    cipherText=""
    cipherText1=""
    
        
    def input_pt(self):
        
        self.planeText=input('enter the plane text:')
        

    def input_key(self):
        self.key=input('enter the key(lenth5):')
        
        
    def encryption(self):
        self.pt=list(self.planeText)
        self.k=list(self.key)
        #print(self.k)
        self.k1=self.k.copy()
        self.k.sort()
        #print(self.k)
        #print(self.k1)
        
        i=0
        if(len(self.pt)%5!=0):
            for i in list(range((5-len(self.pt)%5))):
                self.pt.append("x")

        k2=[]
        #use k2 for select column from matrix
        for i in list(range(5)):
            for j in list(range(5)):
                if(self.k1[i]==self.k[j]):
                    k2.append(j)
                    #self.k3.append(i)

        self.k4=k2.copy()
        for i in list(range(5)):
            for j in list(range(5)):
                if(self.k1[j]==self.k[i]):
                    self.k3.append(j)
        
        
        self.pt.append("x")
        flag=0
        pt1=[]
        ll=[]
        for i in list(range(len(self.pt))):
            if(flag==5):
                flag=0
                pt1.append(ll)
                ll=[]
                flag=flag+1
                ll.append(self.pt[i])
            else:
                flag=flag+1
                ll.append(self.pt[i])

        
        ct=[]
        j=0
        for k in list(range(5)):
            for i in list(range(len(pt1))):
                self.ct.append(pt1[i][k2[j]])
            j=j+1
        
        self.cipherText = ''.join(str(e) for e in self.ct)
        
            
    def decryption(self):
        self.ct=list(self.cipherText)
        
        i=0
        if(len(self.ct)%5!=0):
            for i in list(range((5-len(self.ct)%5))):
                self.ct.append("x")

        self.ct.append("x")
    
        flag=0
        ct1=[]
        ll=[]
        for i in list(range(len(self.ct))):
            if(flag==3):
                flag=0
                ct1.append(ll)
                ll=[]
                flag=flag+1
                ll.append(self.ct[i])
            else:
                flag=flag+1
                ll.append(self.ct[i])

        k2=[]
        #use k2 for select column from matrix
        for i in list(range(5)):
            for j in list(range(5)):
                if(self.k1[i]==self.k[j]):
                    k2.append(j)

        for j in list(range(3)):
            for i in k2:
                self.pt1.append(ct1[i][j])

    
        
        j=0
        pt=[]
        self.pt1=[]
        for k in list(range(3)):
            for i in list(range(5)):
                self.pt1.append(ct1[self.k3[i]][k])
            j=j+1
        
        self.planeText = ''.join(str(e) for e in self.pt1)
        
    
            
    def display1(self):
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('-----------encryption--------------')
        print('plane text is :  ',self.planeText)
        print('cipher text is:  ',self.cipherText)
        print('key is        :  ',self.k4)
        print('--------------------------------------------------------------------------------------------------------------------------------------------')

    def display2(self):
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('-----------encryption--------------')
        print('cipher text is:  ',self.cipherText)
        print('plane text is :  ',self.planeText)
        print('key is        :  ',self.k3)
        print('--------------------------------------------------------------------------------------------------------------------------------------------')

c=Columner_cipher()
c.input_pt()
c.input_key()
c.encryption()
c.display1()
c.decryption()
c.display2()
    
