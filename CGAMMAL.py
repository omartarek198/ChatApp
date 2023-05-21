import random
from math import pow

class elgammal():
    def __init__(self):
        self.privateK = 5

    def set_key(self, key):
        self.EncryptionKey = key
    
    def PrivateKeyGeneration(q):
        privateK = random.randint(1, q)
        return privateK
    
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
    
    def publicKeyGeneration(self, a, q):
        publicK = self.Square_Multiply(a, self.privateK, q)    
        return publicK
    
    def KInverse(self, KC, q):
        KC = KC % q
        for i in range(1, q):
            if (KC * i) % q == 1:
                return i
        return 1
    
    def Decrypt(self, C1, C2, q):
        KC = self.Square_Multiply(C1, self.privateK, q)
        print(KC)
        Kin = self.KInverse(KC, q)
        
        decryptedM = []
        
        for i in range(0, len(C2)):
            decryptedM.append(int(C2[i] / KC))
            
        return decryptedM
    
    def Encrypt(self, q, a, publicK, M):
        
        kS = 6
        KC = self.Square_Multiply(self.EncryptionKey, kS, q)
        print(KC)
        C1 = self.Square_Multiply(a, kS, q)
        print(C1)

        C2 = []

        for i in range(0, len(M)):
            C2.append((KC * ord(M[i])))

        return C1, C2
    

def main(): 
    a = 10
    q = 19
    M = 'alaa'
    #MESSAGE ENCRYPTION AND DECRYPTION
    MT = []
    for i in range(0, len(M)):
        MT.append(ord(M[i]))

    print(MT)

    RecieverP = elgammal()
    RPublicKey = RecieverP.publicKeyGeneration(a,q)
    print(RPublicKey)
    SenderP = elgammal()
    SenderP.set_key(RPublicKey)
    C1, C2 = SenderP.Encrypt(q, a, RPublicKey, M)
    print(C2)
    #C1, C2, q
    C2T = []
    for i in range(0, len(C2)):
        C2T.append(chr(C2[i]))

    print(C2T)

    DM = RecieverP.Decrypt(C1, C2, q)
    print(DM)
    for i in range(0, len(DM)):
        DM[i] = chr(DM[i])
    print('Decrypted Message:', DM)

if __name__ == "__main__":
    main()