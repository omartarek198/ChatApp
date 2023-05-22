import random
from math import pow, sqrt

class elgammal():
    def __init__(self, q, a):
        self.q = q
        self.a = a
        if self.a != 0:
            self.privateKey = self.privateKeyGeneration(self.q)
            self.publicKey = self.publicKeyGeneration(self.a, self.q)



    def q_a_Generation(self):
        self.q = self.generateLargePrime(16)
        self.privateKey = self.privateKeyGeneration(self.q)
        self.a = self.findPrimitive(self.q)
        self.publicKey = self.publicKeyGeneration(self.a, self.q)

    def set_kSmall(self, kS):
        self.kS = kS
    
    def kSmallGeneration(self, max):
        self.kS = random.randint(1, max)
        
    def privateKeyGeneration(self, q):
        privateK = random.randint(1, q)
        return privateK
    
    def publicKeyGeneration(self, a, q):
        publicK = self.Square_Multiply(a, self.privateKey, q)    
        return publicK

    def KInverse(self, KC, q):
        KC = KC % q
        for i in range(1, q):
            if (KC * i) % q == 1:
                return i
        return 1
    
    def isPrime(self,n):
        """
            return True if n prime
            fall back to rabinMiller if uncertain
        """

        # 0, 1, -ve numbers not prime
        if n < 2:
            return False

        # low prime numbers to save time
        lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
                     47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                     101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
                     151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 
                     199, 211, 223, 227, 229, 233, 239, 241, 251, 257
                     , 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317
                     , 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 
                     401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 
                     487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 
                     593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 
                     683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                     809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
                     919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

        # if in lowPrimes
        if n in lowPrimes:
            return True

        # if low primes divide into n
        for prime in lowPrimes:
            if n % prime == 0:
                return False
        
     

        return True
    
    def generateLargePrime(self,keysize):
        """
            return random large prime number of keysize bits in size
        """

        while True:
            num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
            if (self.isPrime(num)):
                return num
    
    # Utility function to store prime
    # factors of a number
    def findPrimefactors(self,s, n) :
    
        # Print the number of 2s that divide n
        while (n % 2 == 0) :
            s.add(2)
            n = n // 2
    
        # n must be odd at this point. So we can 
        # skip one element (Note i = i +2)
        for i in range(3, int(sqrt(n)), 2):

            # While i divides n, print i and divide n
            while (n % i == 0) :
            
                s.add(i)
                n = n // i

        # This condition is to handle the case
        # when n is a prime number greater than 2
        if (n > 2) :
            s.add(n)
    
    # Function to find smallest primitive
    # root of n
    def findPrimitive(self, n) :
        s = set()
    
        # Check if n is prime or not
        if (self.isPrime(n) == False):
            return -1
    
        # Find value of Euler Totient function
        # of n. Since n is a prime number, the
        # value of Euler Totient function is n-1
        # as there are n-1 relatively prime numbers.
        phi = n - 1
    
        # Find prime factors of phi and store in a set
        self.findPrimefactors(s, phi)
    
        # Check for every number from 2 to phi
        for r in range(2, phi + 1):
        
            # Iterate through all prime factors of phi.
            # and check if we found a power with value 1
            flag = False
            for it in s:
            
                # Check if r^((phi)/primefactors)
                # mod n is 1 or not
                if (self.Square_Multiply(r, phi // it, n) == 1):
                
                    flag = True
                    break
                
            # If there was no power with value 1.
            if (flag == False):
                return r
    
        # If no primitive root found
        return -1

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
    
    def append_message(self, message):
        self.message = message
        return 1
    
    def Decrypt(self, C1, C2):
        KC = self.Square_Multiply(C1, self.privateKey, self.q)
        print(KC)
        Kin = self.KInverse(KC, self.q)
        
        decryptedM = []
        
        for i in range(0, len(C2)):
            decryptedM.append(int(C2[i] / KC))
            
        return decryptedM
    
    def Encrypt(self, recPublicKey, M):
        
       
        KC = self.Square_Multiply(recPublicKey, self.kS, self.q)
        C1 = self.Square_Multiply(self.a, self.kS, self.q)

        C2 = []

        for i in range(0, len(M)):
            #ord function returns an intger representing the unicode char
            C2.append((KC * ord(M[i])))

        return C1, C2
    

# def main(): 
#     # a = 10
#     # q = 19
#     k=10
#     M = 'Hello there! my friend I ahve missed you '

#     firstGammal = elgammal(0,0)
#     firstGammal.q_a_Generation()
#     secondGammal = elgammal(firstGammal.q, firstGammal.a)
#     secondGammal.kSmallGeneration(k)
#     firstGammal.set_kSmall(secondGammal.kS)
#     # SenderP = elgammal(a, k,q)
#     # SenderP.set_key(RecieverP.publicK)
#     C1, C2 = secondGammal.Encrypt(firstGammal.publicKey,M)
    
#     print('c1: ', C1)
#     print('c2: ',C2)
   

#     DM = firstGammal.Decrypt(C1, C2)
#     for i in range(0, len(DM)):
#         DM[i] = chr(DM[i])
#     print('Decrypted Message:', DM)

# if __name__ == "__main__":
#     main()
