class Multiplicative_cipher:
    'Multiplicative cipher is one type moloalphabatic cipher'
	
    list1=[]
    list2=[]
    pt=[]
    ct=[]
	
    planeText=""
    cipherText=""
    key=""

        
    def input_pt(self):
        self.planeText=input('enter the plane text:')

    def input_key(self):
        print("key of muliplicative cipher is only prime number between 0 to 26 which muliplicative inverse availabel")
        print("muliplicative inverse of x availabel only if gcd(x,inverser of x)=1")
        print("same condition for prime number also so")
        print("key domain : 1,3,5,7,9,11,15,17,19,21,23,25")
        self.key=input('enter the key(numeric):')
		
    def encryption(self):
        self.pt=list(self.planeText)              #plane text list so we can use separate char 

        for i in self.pt:
            a=ord(i)-97                 # minus 97 so a=00, b=01, so on z=25 and ord-->ascii to integer converter
            b=a*int(self.key)
            n=b%26
            n=n+97                      #for give ascii value to interger so using chr fun we covert interger to ascii
            self.list1.append(chr(n))
		
        self.cipherText = ''.join(str(e) for e in self.list1)

    def muliplicative_inverse(self):
        a=int(self.key)
        for i in list(range(26)):
            if(((i*a)% 26)==1):
                self.key=i
                print(self.key)

    def decryption(self):
        self.ct=list(self.cipherText)

        for i in self.ct:
            a=ord(i)-97
            b=a*int(self.key)
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

		
oa1=Multiplicative_cipher()
oa1.input_pt()
oa1.input_key()
oa1.encryption()
oa1.display1()
oa1.muliplicative_inverse()
oa1.decryption()
oa1.display2()
