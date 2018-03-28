import numpy as np
class Hill_cipher:
    'Hill cipher is use matrix as key. in this block by block encryption'
	
    list1=[]
    list2=[]
    pt=[]
    pt1=[]
    ct=[]
    k=[]
    n=1
    key=[]
    inverseKey=[]
    result=[]
	
    planeText=""
    cipherText=""
    
        
    def input_pt(self):
        #only enter 9 element 
        self.planeText=input('enter the plane text:')
        #self.key=[[2,4,5],[9,2,1],[3,17,7]]
        self.key=[[3,10,20],[20,9,17],[9,4,17]]
        self.inverseKey=[[11,22,14],[7,9,21],[17,0,3]]

    def input_key(self):
        print('for matrix size')
        print('enter 1 for 3x3')
        print('enter 2 or greter than 2 for 4x4')
        self.n=int(input('enter 1 or 2 for matrix size:'))
        if(self.n==1):
            #self.key=[[0,0,0],[0,0,0],[0,0,0]]
            for i in list(range(3)):
                for j in list(range(3)):
                    self.key[i][j]=int(input())
        else:
            self.key=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            for i in list(range(4)):
                for j in list(range(4)):
                    self.key[i][j]=int(input())


    def encryption(self):
        self.pt=list(self.planeText)
        for i in list(range(len(self.pt))):
            self.pt1.append(ord(self.pt[i])-97)

        m=0
        if(self.n>-1):
            a=[[0],[0],[0]]
            for i in list(range(3)):
                for j in list(range(3)):
                    a[j][0]=ord(self.pt[m])-97
                    m=m+1
                #print(a)
                r=np.matmul(self.key,a)
                #print(r)
                for q in list(range(3)):
                    self.ct.append(chr(r[q][0]%26+97))
                #print(self.ct)

            self.cipherText = ''.join(str(e) for e in self.ct)
        else:
            print('1')

    def decryption(self):
        self.ct1=list(self.cipherText)
        m=0
        #print(self.inverseKey)
        a=[[0],[0],[0]]
        for i in list(range(3)):
                for j in list(range(3)):
                    a[j][0]=ord(self.ct1[m])-97
                    m=m+1
                #print(a)
                r=np.matmul(self.inverseKey,a)
                #print(r)
                for q in list(range(3)):
                    self.pt1.append(chr(r[q][0]%26+97))
                #print(self.ct)
                    
        self.cipherText = ''.join(str(e) for e in self.ct1)
            
            
    def display1(self):
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('-----------encryption--------------')
        print('plane text is :  ',self.planeText)
        print('cipher text is:  ',self.cipherText)
        print('key is        :  ',self.key)
        print('--------------------------------------------------------------------------------------------------------------------------------------------')

    def display2(self):
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('-----------encryption--------------')
        print('plane text is :  ',self.planeText)
        print('cipher text is:  ',self.cipherText)
        print('key is        :  ',self.inverseKey)
        print('--------------------------------------------------------------------------------------------------------------------------------------------')

h=Hill_cipher()
h.input_pt()
print(h.key)
#h.input_key()
h.encryption()
h.display1()
h.decryption()
h.display2()
    
