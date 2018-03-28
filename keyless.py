import numpy as np
class Columner_cipher:
    'Hill cipher is use matrix as key. in this block by block encryption'
	
    list1=[]
    list2=[]
    pt=[]
    pt1=[]
    ct=[]
    ct=[]
    k=[]
    n=1
    key=[]
    inverseKey=[]
    result=[]
	
    planeText=""
    planeText1=""
    cipherText=""
    cipherText1=""
    
        
    def input_pt(self):
        
        self.planeText=input('enter the plane text:')

    def encryption(self):
        self.pt=list(self.planeText)
        
        i=0
        if(len(self.pt)%5!=0):
            for i in list(range((5-len(self.pt)%5))):
                self.pt.append("x")

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

        
        for j in list(range(5)):
            for i in list(range(len(pt1))):
                self.ct.append(pt1[i][j])
        
        
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


        for j in list(range(3)):
            for i in list(range(5)):
                self.pt1.append(ct1[i][j])

        
        
        self.planeText = ''.join(str(e) for e in self.pt1)
        
    
            
    def display1(self):
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('-----------encryption--------------')
        print('plane text is :  ',self.planeText)
        print('cipher text is:  ',self.cipherText)
        #print('key is        :  ',self.key)
        print('--------------------------------------------------------------------------------------------------------------------------------------------')

    def display2(self):
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('-----------encryption--------------')
        print('cipher text is:  ',self.cipherText)
        print('plane text is :  ',self.planeText)
        #print('key is        :  ',self.inverseKey)
        print('--------------------------------------------------------------------------------------------------------------------------------------------')

c=Columner_cipher()
c.input_pt()
c.encryption()
c.display1()
c.decryption()
c.display2()
    
