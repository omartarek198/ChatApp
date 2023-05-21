import random
from math import pow

class elgammal():
    def __init__(self, q, a, k):
        self.kS = k
        self.privateK = self.privateKeyGeneration(q)
        self.publicK = self.publicKeyGeneration(a, q)

    def set_key(self, key):
        self.EncryptionKey = key
    
    def privateKeyGeneration(q):
        privateK = random.randint(1, q)
        return privateK
    
    def publicKeyGeneration(self, a, q):
        publicK = self.Square_Multiply(a, self.privateK, q)    
        return publicK
    
    def KInverse(self, KC, q):
        KC = KC % q
        for i in range(1, q):
            if (KC * i) % q == 1:
                return i
        return 1
    
    def Square_Multiply(self,First, power, q):
        results = []
        n = 1
        pn = 0

        while n < power:
            if n == 1:
                calc = First % q
            else:
                calc = First * First
                calc = calc % q

            First = calc
            results.append(calc)

            pn = n
            n = n + n


        power = format(power, "0b")
        MultArray = []
        counter = len(results) - 1

        for i in range(0, len(power)):
            if power[i] == '1':
                MultArray.append(results[counter - i])

        for i in range (0, len(MultArray)):
            if i == 0:
                calc = MultArray[i]
            else:
                calc = calc * MultArray[i]


        publicK = calc % q

        return publicK
    
    
    
    
    def Decrypt(self, C1, C2, q):
        KC = self.Square_Multiply(C1, self.privateK, q)
        print(KC)
        Kin = self.KInverse(KC, q)
        
        decryptedM = []
        
        for i in range(0, len(C2)):
            decryptedM.append(int(C2[i] / KC))
            
        return decryptedM
    
     def Encrypt(self, q, a, publicK, M):
        
       
        KC = self.Square_Multiply(self.EncryptionKey, self.kS, q)
        C1 = self.Square_Multiply(a, self.kS, q)

        C2 = []

        for i in range(0, len(M)):
            C2.append((KC * ord(M[i])))

        return C1, C2
    

def main(): 
    a = 10
    q = 19
    k=6
    M = 'alaa'

    RecieverP = elgammal(a,k, q)
    SenderP = elgammal(a, k,q)
    SenderP.set_key(RecieverP.publicK)
    C1, C2 = SenderP.Encrypt(q, a, SenderP.EncryptionKey, M)
    #C1, C2, q
   

    DM = RecieverP.Decrypt(C1, C2, q)
    for i in range(0, len(DM)):
        DM[i] = chr(DM[i])
    print('Decrypted Message:', DM)


if __name__ == "__main__":
    main()
