class Affine_cipher:
    'Affine cipher is combination of Addtive and muliplicative cipher'
	
    list1=[]
    list2=[]
    pt=[]       #plane text
    it1=[]       #intermedeate text
    it2=[]
    ct=[]       #cipher text
	
    planeText=""
    cipherText=""
    intermediateText1=""
    intermediateText2=""
    key1=""
    key2=""

        
    def input_pt(self):
        self.planeText=input('enter the plane text:')

    def input_key1(self):
        print("key of muliplicative cipher is only prime number between 0 to 26 which muliplicative inverse availabel")
        print("muliplicative inverse of x availabel only if gcd(x,inverser of x)=1")
        print("same condition for prime number also so")
        print("key domain : 1,3,5,7,9,11,15,17,19,21,23,25")
        self.key1=input('enter the key1(numeric):')

    def input_key2(self):
        self.key2=input('enter the key2(numeric):')
    
    def encryption(self):
        self.pt=list(self.planeText)              #plane text list so we can use separate char 

        for i in self.pt:
            a=ord(i)-97                 # minus 97 so a=00, b=01, so on z=25 and ord-->ascii to integer converter
            b=a*int(self.key1)
            n=b%26
            n=n+97                      #for give ascii value to interger so using chr fun we covert interger to ascii
            self.it1.append(chr(n))
		
        #self.cipherText = ''.join(str(e) for e in self.list1)
        for i in self.it1:
            a=ord(i)-97                 # minus 97 so a=00, b=01, so on z=25 and ord-->ascii to integer converter
            b=a+int(self.key2)
            n=b%26
            n=n+97                      #for give ascii value to interger so using chr fun we covert interger to ascii
            self.list1.append(chr(n))
		
        self.cipherText = ''.join(str(e) for e in self.list1)
        self.intermediateText1=''.join(str(e) for e in self.it1)
        
    def muliplicative_inverse(self):
        a=int(self.key1)
        for i in list(range(26)):
            if(((i*a)% 26)==1):
                self.key1=i

    def decryption(self):
        self.ct=list(self.cipherText)

        for i in self.ct:
            a=ord(i)-97
            b=a-int(self.key2)
            n=b%26
            n=n+97
            self.it2.append(chr(n))

        
        for i in self.it2:
            a=ord(i)-97
            b=a*int(self.key1)
            n=b%26
            n=n+97
            self.list2.append(chr(n))
            
        #self.planeText = ''.join(str(e) for e in self.list2)
        self.planeText = ''.join(str(e) for e in self.list2)
        self.intermediateText2=''.join(str(e) for e in self.it2)
        
    def display1(self):
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('-----------encryption--------------')
        print('plane text is :        ',self.planeText)
        print('intermediate text is:  ',self.intermediateText1)
        print('cipher text is:        ',self.cipherText)
        print('key1 is        :       ',self.key1)
        print('key2 is        :       ',self.key2)
        print('--------------------------------------------------------------------------------------------------------------------------------------------')

    def display2(self):
        print('--------------------------------------------------------------------------------------------------------------------------------------------')
        print('-----------decryption--------------')
        print('cipher text is:        ',self.cipherText)
        print('intermediate text is:  ',self.intermediateText2)
        print('plane text is :        ',self.planeText)
        print('key1 is        :       ',self.key1)
        print('key2 is        :       ',self.key2)
        print('--------------------------------------------------------------------------------------------------------------------------------------------')

		
oa1=Affine_cipher()
oa1.input_pt()
oa1.input_key1()
oa1.input_key2()
oa1.encryption()
oa1.display1()
oa1.muliplicative_inverse()
oa1.decryption()
oa1.display2()
