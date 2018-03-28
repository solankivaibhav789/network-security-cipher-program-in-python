import numpy as np
class Playfair_cipher:
    'Playfair cipher is use matrix as key'

    list1=[]
    list2=[]
    kw=[]
    kw1=[]
    pt=[]
    pt1=[]
    ct=[]
    k=0
    m=0
    remain=[]
    
    planeText="wearediscoveredsaveyourselfx"
    cipherText=""
    keyword="moniarchy"
    keyword1=""
    alpha="abcdefghijklmnopqrstuvwxyz"
    a=list(alpha)

    key=np.matrix('"a",0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0')

    def input_pt(self):
        self.planeText=input('enter the plane text:')

    def input_keyword(self):
        self.keyword=input('enter the key(keyword):')

    def encryption(self):
        self.kw=list(self.keyword)
        self.pt=list(self.planeText)        #plane text list so we can use separate char
        p=''
        for i in self.kw:
            if i not in self.kw1:
                self.kw1.append(i)

        for i in self.a:
            if i not in self.kw1:
                self.remain.append(i)

        #making key matrix
        ii=False;       #this for is there is i come(1) or not(0)
        for i in list(range(5)):
            for j in list(range(5)):
                if(self.k<len(self.kw1)):
                    self.key[i,j]=self.kw1[self.k]
                    self.k=self.k+1
                elif(self.m<len(self.remain) and self.remain[self.m]!='j'):
                    self.key[i,j]=self.remain[self.m]
                    self.m=self.m+1
                else:
                    self.m=self.m+1
                    self.key[i,j]=self.remain[self.m]
                    self.m=self.m+1

        #if length is even than replace X with second occurence
        #if length is odd than add X after second occurence
        if(len(self.pt)%2==0):
            for i in list(range(len(self.pt))):
                if(self.pt[i]==p):
                    self.pt1.append('x')
                else:
                    self.pt1.append(self.pt[i])
                    p=self.pt[i]
        else:
            for i in list(range(len(self.pt))):
                if(self.pt[i]==p):
                    self.pt1.append('x')
                    self.pt1.append(self.pt[i])
                else:
                    self.pt1.append(self.pt[i])
                    p=self.pt[i]

        row1=0
        row2=0
        col1=0
        col2=0
        for m in range(0,len(self.pt1),2):
            for i in list(range(5)):
                for j in list(range(5)):
                    cur=self.pt1[m]
                    n=m+1
                    nxt=self.pt1[n]
                    if(cur==self.key[i,j]):
                        row1=i
                        col1=j
                    if(nxt==self.key[i,j]):
                        row2=i
                        col2=j

            if(row1==row2):
                col1=(col1+1+5)%5
                col2=(col2+1+5)%5
            elif(col1==col2):
                row1=(row1+1+5)%5
                row2=(row2+1+5)%5
            else:
                temp1=col1
                col1=col2
                col2=temp1
                
            self.ct.append(self.key[row1,col1])
            self.ct.append(self.key[row2,col2])
                

        self.cipherText= ''.join(str(e) for e in self.ct)

    def decryption(self):
        self.pt=list(self.cipherText)        #plane text list so we can use separate char
        
        row1=0
        row2=0
        col1=0
        col2=0
        for m in range(0,len(self.pt1),2):
            for i in list(range(5)):
                for j in list(range(5)):
                    cur=self.pt1[m]
                    n=m+1
                    nxt=self.pt1[n]
                    if(cur==self.key[i,j]):
                        row1=i
                        col1=j
                    if(nxt==self.key[i,j]):
                        row2=i
                        col2=j

            if(row1==row2):
                col1=(col1-1+5)%5
                col2=(col2-1+5)%5
            elif(col1==col2):
                row1=(row1-1+5)%5
                row2=(row2-1+5)%5
            else:
                temp1=col1
                col1=col2
                col2=temp1
                
            self.ct.append(self.key[row1,col1])
            self.ct.append(self.key[row2,col2])
                

        self.cipherText= ''.join(str(e) for e in self.ct)

    
    def display(self):
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('-----------encryption--------------')
        print('plane text is :  ',self.planeText)
        print('cipher text is:  ',self.cipherText)
        print('key is        :  ')
        print(self.key)
        print('--------------------------------------------------------------------------------------------------------------------------------------------')


    def display1(self):
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('-----------decryption--------------')
        print('cipher text is:  ',self.cipherText)
        print('plane text is :  ',self.planeText)
        print('key is        :  ')
        print(self.key)
        print('--------------------------------------------------------------------------------------------------------------------------------------------')   
                    
p=Playfair_cipher()
#p.input_pt()
#p.input_keyword()
p.encryption()
p.decryption()
p.display()
p.display1()
