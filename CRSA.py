import random

class RSA:
    def __init__(self) -> None:
            self.d = 0
            self.e = 0
            self.N =0
            
            print("Hello, RSA!")

            keysize = 16
            
            self.generateKeys(keysize)

       

          
    def generateKeys(self,keysize=8 ):
        e = d = N = 0

        # get prime nums, p & q
        p = self.generateLargePrime(keysize)
        q = self.generateLargePrime(keysize)

        print(f"p: {p}")
        print(f"q: {q}")

        N = p * q # RSA Modulus
        phiN = (p - 1) * (q - 1) # totient

        # choose e
        # e is coprime with phiN & 1 < e <= phiN
        print(phiN)
        dp = {}
        # self.gcd(e, phiN) != 1
        while True :
            e = random.randint(2, phiN)  # Generate a random value between 2 and phiN
            if e in dp:
                continue
            if self.gcd(e, phiN) == 1:
                break
            dp[e] = -1
                
        print (e)
                        
                        
                

        # e * d (mod phiN) = 1
        d = self.modularInv(e, phiN)
        print (e)
        self.e = e
        self.d = d
        self.N = N
        
        print(f"e: {e}")
        print(f"d: {d}")
        print(f"N: {N}")
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
    def gcd(self,p, q):
        """
            euclidean algorithm to find gcd of p and q
        """

        while q:
            p, q = q, p % q
        return p


    def egcd(self,a, b):
        s = 0; old_s = 1
        t = 1; old_t = 0
        r = b; old_r = a

        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t

        # return gcd, x, y
        return old_r, old_s, old_t
    def modularInv(self,a, b):
        gcd, x, y = self.egcd(a, b)

        if x < 0:
            x += b

        return x
    def encrypt(self,e, N, msg):
        cipher = ""

        for c in msg:
            m = ord(c)
            cipher += str(pow(m, e, N)) + " "

        return cipher
    def decrypt(self,d, N, cipher):
        msg = ""

        parts = cipher.split()
        for part in parts:
            if part:
                c = int(part)
                msg += chr(pow(c, d, N))

        return msg
    
    
def main():
    msg = "123omar456"
    test = RSA()
    enc = test.encrypt(test.e, test.N, msg)
    dec = test.decrypt(test.d, test.N, enc)
    print(f"Message: {msg}")
    print(f"e: {test.e}")
    print(f"d: {test.d}")
    print(f"N: {test.N}")
    print(f"enc: {enc}")
    print(f"dec: {dec}")
    
if __name__ == "__main__":
    main()


