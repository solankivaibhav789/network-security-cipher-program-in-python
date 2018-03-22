class Vigenere_cipher:
    'vigenere cipher is use repeted keyword.'
	
    list1=[]
    list2=[]
    pt=[]
    ct=[]
    k=[]
	
    planeText=""
    cipherText=""
    key=""

        
    def input_pt(self):
        self.planeText=input('enter the plane text:')

    def input_key(self):
        self.key=input('enter the key(string):')
		
    def encryption(self):
        self.pt=list(self.planeText)              #plane text list so we can use separate char
        self.k=list(self.key)
        j=0
        for i in self.pt:
            a=ord(i)-97                 # minus 97 so a=00, b=01, so on z=25 and ord-->ascii to integer converter
            p=ord(self.k[j])-97
            b=a+p
            j=j+1
            if(j>len(self.k)-1):
                j=0
        
            n=b%26
            n=n+97                      #for give ascii value to interger so using chr fun we covert interger to ascii
            self.list1.append(chr(n))
		
        self.cipherText = ''.join(str(e) for e in self.list1)

    def decryption(self):
        self.ct=list(self.cipherText)
        j=0
        for i in self.ct:
            a=ord(i)-97                 # minus 97 so a=00, b=01, so on z=25 and ord-->ascii to integer converter
            p=ord(self.k[j])-97
            b=a-p
            j=j+1
            if(j>len(self.k)-1):
                j=0
            n=b%26
            n=n+97
            self.list2.append(chr(n))
            
        self.planeText = ''.join(str(e) for e in self.list2)
        
    def display1(self):
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('-----------encryption--------------')
        print('plane text is :  ',self.planeText)
        print('cipher text is:  ',self.cipherText)
        print('key is        :  ',self.key)
        print('--------------------------------------------------------------------------------------------------------------------------------------------')

    def display2(self):
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('-----------decryption--------------')
        print('cipher text is:  ',self.cipherText)
        print('plane text is :  ',self.planeText)
        print('key is        :  ',self.key)
        print('--------------------------------------------------------------------------------------------------------------------------------------------')

		
oa1=Vigenere_cipher()
oa1.input_pt()
oa1.input_key()
oa1.encryption()
oa1.display1()
oa1.decryption()
oa1.display2()
