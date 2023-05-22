class AES():
    def __init__(self):
        self.Matrix_Mult = [
                ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'],
                ['2', '4', '6', '8', 'A', 'C', 'E', '3', '1', '7', '5', 'B', '9', 'F', 'D'],
                ['3', '6', '5', 'C', 'F', 'A', '9', 'B', '8', 'D', 'E', '7', '4', '1', '2'],
                ['4', '8', 'C', '3', '7', 'B', 'F', '6', '2', 'E', 'A', '5', '1', 'D', '9'],
                ['5', 'A', 'F', '7', '2', 'D', '8', 'E', 'B', '4', '1', '9', 'C', '3', '6'],
                ['6', 'C', 'A', 'B', 'D', '7', '1', '5', '3', '9', 'F', 'E', '8', '2', '4'],
                ['7', 'E', '9', 'F', '8', '1', '6', 'D', 'A', '3', '4', '2', '5', 'C', 'B'],
                ['8', '3', 'B', '6', 'E', '5', 'D', 'C', '4', 'F', '7', 'A', '2', '9', '1'],
                ['9', '1', '8', '2', 'B', '3', 'A', '4', 'D', '5', 'C', '6', 'F', '7', 'E'],
                ['A', '7', 'D', 'E', '4', '9', '3', 'F', '5', '8', '2', '1', 'B', '6', 'C'],
                ['B', '5', 'E', 'A', '1', 'F', '4', '7', 'C', '2', '9', 'D', '6', '8', '3'],
                ['C', 'B', '7', '5', '9', 'E', '2', 'A', '6', '1', 'D', 'F', '3', '4', '8'],
                ['D', '9', '4', '1', 'C', '8', '5', '2', 'F', 'B', '6', '3', 'E', 'A', '7'],
                ['E', 'F', '1', 'D', '3', '2', 'C', '9', '7', '6', '8', '4', 'A', 'B', '5'],
                ['F', 'D', '2', '9', '6', '4', 'B', '1', 'E', 'C', '3', '8', '7', '5', 'A']
            ]
        self.Matrix_Add = [
                ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'],
                ['1', '0', '3', '2', '5', '4', '7', '6', '9', '8', 'B', 'A', 'D', 'C', 'F', 'E'],
                ['2', '3', '0', '1', '6', '7', '4', '5', 'A', 'B', '8', '9', 'E', 'F', 'C', 'D'],
                ['3', '2', '1', '0', '7', '6', '5', '4', 'B', 'A', '9', '8', 'F', 'E', 'D', 'C'],
                ['4', '5', '6', '7', '0', '1', '2', '3', 'C', 'D', 'E', 'F', '8', '9', 'A', 'B'],
                ['5', '4', '7', '6', '1', '0', '3', '2', 'D', 'C', 'F', 'E', '9', '8', 'B', 'A'],
                ['6', '7', '4', '5', '2', '3', '0', '1', 'E', 'F', 'C', 'D', 'A', 'B', '8', '9'],
                ['7', '6', '5', '4', '3', '2', '1', '0', 'F', 'E', 'D', 'C', 'B', 'A', '9', '8'],
                ['8', '9', 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7'],
                ['9', '8', 'B', 'A', 'D', 'C', 'F', 'E', '1', '0', '3', '2', '5', '4', '7', '6'],
                ['A', 'B', '8', '9', 'E', 'F', 'C', 'D', '2', '3', '0', '1', '6', '7', '4', '5'],
                ['B', 'A', '9', '8', 'F', 'E', 'D', 'C', '3', '2', '1', '0', '7', '6', '5', '4'],
                ['C', 'D', 'E', 'F', '8', '9', 'A', 'B', '4', '5', '6', '7', '0', '1', '2', '3'],
                ['D', 'C', 'F', 'E', '9', '8', 'B', 'A', '5', '4', '7', '6', '1', '0', '3', '2'],
                ['E', 'F', 'C', 'D', 'A', 'B', '8', '9', '6', '7', '4', '5', '2', '3', '0','1'],
                ['F', 'E', 'D', 'C', 'B', 'A', '9', '8', '7', '6', '5', '4', '3', '2', '1','0']
            ]
        
    def xor(self, str1, str2):
        result = ''
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                result += '0'
            else:
                result += '1'
        return result
    
    def RotNib(self, binary_string):
        first_half = binary_string[:4]
        second_half = binary_string[4:]
        swapped = second_half + first_half
        return swapped
    
    def swap_nibbles(self, binary_string):
        first_nibble = binary_string[:4]
        second_nibble = binary_string[4:8]
        third_nibble = binary_string[8:12]
        fourth_nibble = binary_string[12:]
        swapped = first_nibble + fourth_nibble + third_nibble + second_nibble
        return swapped
    
    def SubNib(self, binary_string):
        if len(binary_string) not in [8, 16]:
            raise ValueError("The input string must be 8 or 16 bits long.")
        sbox = {
            '0000': '1001', '0001': '0100', '0010': '1010', '0011': '1011',
            '0100': '1101', '0101': '0001', '0110': '1000', '0111': '0101',
            '1000': '0110', '1001': '0010', '1010': '0000', '1011': '0011',
            '1100': '1100', '1101': '1110', '1110': '1111', '1111': '0111'
        }
        if len(binary_string) == 8:
            first_nibble = binary_string[:4]
            second_nibble = binary_string[4:]
            new_first_nibble = sbox[first_nibble]
            new_second_nibble = sbox[second_nibble]
            result = new_first_nibble + new_second_nibble
        else: # 16-bit input
            first_nibble = binary_string[:4]
            second_nibble = binary_string[4:8]
            third_nibble = binary_string[8:12]
            fourth_nibble = binary_string[12:]
            new_first_nibble = sbox[first_nibble]
            new_second_nibble = sbox[second_nibble]
            new_third_nibble = sbox[third_nibble]
            new_fourth_nibble = sbox[fourth_nibble]
            result = new_first_nibble + new_second_nibble + new_third_nibble + new_fourth_nibble
        return result

    def hex_to_binary(self, hex_str):
        binary_map = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111",
        }
        return binary_map[hex_str]
    def InvSubNib(self, binary_string):
        if len(binary_string) not in [8, 16]:
            raise ValueError("The input string must be 8 or 16 bits long.")
        sbox ={
            '1001': '0000', '0100': '0001', '1010': '0010', '1011': '0011',
            '1101':'0100','0001': '0101', '1000': '0110', '0101': '0111', 
            '0110': '1000','0010': '1001', '0000': '1010', '0011': '1011',
            '1100': '1100', '1110': '1101', '1111': '1110','0111': '1111'
            }
        if len(binary_string) == 8:
            first_nibble = binary_string[:4]
            second_nibble = binary_string[4:]
            new_first_nibble = sbox[first_nibble]
            new_second_nibble = sbox[second_nibble]
            result = new_first_nibble + new_second_nibble
        else: # 16-bit input
            first_nibble = binary_string[:4]
            second_nibble = binary_string[4:8]
            third_nibble = binary_string[8:12]
            fourth_nibble = binary_string[12:]
            new_first_nibble = sbox[first_nibble]
            new_second_nibble = sbox[second_nibble]
            new_third_nibble = sbox[third_nibble]
            new_fourth_nibble = sbox[fourth_nibble]
            result = new_first_nibble + new_second_nibble + new_third_nibble + new_fourth_nibble
        return result
    def hex_to_dec(self, hex_char):
        if hex_char.isdigit():
            return int(hex_char)
        else:
            return ord(hex_char.lower()) - 87
    def Add(self, hex1,hex2):
        row_index = self.hex_to_dec(hex1[0])
        col_index = self.hex_to_dec(hex2[0])
        intersection_value = self.Matrix_Add[row_index][col_index]
        return intersection_value
            
    def Multi(self, hex1, hex2):
         #if hex1 == 0:
          #  return(hex1)
         if hex2 == '0000':
            return(hex2)
         else:
            sec_tot1 = ''
            sec_tot2 = 0
            if hex2[0] != '0':
                sec_tot2 += 8
            if hex2[1] != '0':
                sec_tot2 += 4
            if hex2[2] != '0':
                sec_tot2 += 2
            if hex2[3] != '0':
                sec_tot2 += 1
            row_index = hex1 - 1
            col_index = sec_tot2 - 1
            intersection_value = self.Matrix_Mult[row_index][col_index]
            return intersection_value
    def encrypt(self, text,key):   
        binary_list = []
        for char in text:
            # Convert character to binary and remove the '0b' prefix
            binary = bin(ord(char))[2:]
            # Pad binary with leading zeros if it's less than 8 digits
            binary = binary.zfill(8)
            binary_list.append(binary)
        # Join all the binary strings together into one long string
        binary_string = ''.join(binary_list)
        # Divide the binary string into groups of 16 digits
        binary_groups = [binary_string[i:i+16] for i in range(0, len(binary_string), 16)]
        # Pad the last group with zeros if it's less than 16 digits
        last_group_length = len(binary_groups[-1])
        if last_group_length < 16:
            padding_length = 16 - last_group_length
            binary_groups[-1] += '0' * padding_length           
        Results= '' 
        for i in range(len(binary_groups)):
            plaintext = binary_groups[i]
            
            W0 = key[:len(key)//2]
            W1 = key[len(key)//2:]
            
            yolo = self.xor(W0,'10000000')
            yolo2 = self.SubNib(self.RotNib(W1))
            W2 = self.xor(yolo,yolo2)
            
            W3=self.xor(W1,W2)
            
            yolo = self.xor(W2,'00110000')
            yolo2 = self.SubNib(self.RotNib(W3))
            W4 = self.xor(yolo,yolo2)
            
            W5 = self.xor(W3,W4)
            k0 = W0+W1
            k1 = W2+W3
            k2 = W4+W5
            
            #Encryption
            Ro1=self.xor(plaintext,k0)
            sub1=self.SubNib(Ro1)
            sub2= self.swap_nibbles(sub1)
            
            S00 = sub2[:4]
            S10 = sub2[4:8]
            S01 = sub2[8:12]
            S11 = sub2[12:]
            
            left = self.Multi(1,S00)
            right = self.Multi(4,S10)
            S00D= self.Add(left,right)
            S00D= self.hex_to_binary(S00D)
            
            left = self.Multi(4,S00)
            right = self.Multi(1,S10)
            S10D= self.Add(left,right)
            S10D= self.hex_to_binary(S10D)
            
            left = self.Multi(1,S01)
            right = self.Multi(4,S11)
            S01D= self.Add(left,right)
            S01D= self.hex_to_binary(S01D)
            
            left = self.Multi(4,S01)
            right = self.Multi(1,S11)
            S11D= self.Add(left,right)
            S11D= self.hex_to_binary(S11D)
            #
            Mix_Col=S00D+S10D+S01D+S11D
            #
            Ro2=self.xor(Mix_Col,k1)
            sub1=self.SubNib(Ro2)
            sub2 = self.swap_nibbles(sub1)
            Result = self.xor(sub2,k2)
            Results += Result
        return Results


    def decrypt(self, Ciphertext,key):   
        Results = ''
        binary_groups = []
        for i in range(0, len(Ciphertext), 16):
            binary_group = Ciphertext[i:i+16]
            binary_groups.append(binary_group)
        for i in range(len(binary_groups)):
            Encryption = binary_groups[i]
            W0 = key[:len(key)//2]
            W1 = key[len(key)//2:]
            
            yolo = self.xor(W0,'10000000')
            yolo2 = self.SubNib(self.RotNib(W1))
            W2 = self.xor(yolo,yolo2)
            
            W3=self.xor(W1,W2)
            
            yolo = self.xor(W2,'00110000')
            yolo2 = self.SubNib(self.RotNib(W3))
            W4 = self.xor(yolo,yolo2)
            
            W5 = self.xor(W3,W4)
            k0 = W0+W1
            k1 = W2+W3
            k2 = W4+W5
            
            peps = self.xor(Encryption,k2)
            peps = self.swap_nibbles(peps)
            
            pops = self.InvSubNib(peps)
            
            inv = self.xor(pops,k1)
            
            S00 = inv[:4]
            S10 = inv[4:8]
            S01 = inv[8:12]
            S11 = inv[12:]
            
            left = self.Multi(9,S00)
            right = self.Multi(2,S10)
            S00D= self.Add(left,right)
            S00D= self.hex_to_binary(S00D)
            
            left = self.Multi(2,S00)
            right = self.Multi(9,S10)
            S10D= self.Add(left,right)
            S10D= self.hex_to_binary(S10D)
            
            left = self.Multi(9,S01)
            right = self.Multi(2,S11)
            S01D= self.Add(left,right)
            S01D= self.hex_to_binary(S01D)
            
            left = self.Multi(2,S01)
            right = self.Multi(9,S11)
            S11D= self.Add(left,right)
            S11D= self.hex_to_binary(S11D)
            #
            Mix_Col=S00D+S10D+S01D+S11D
            #
            cont = self.swap_nibbles(Mix_Col)
            #
            pops = self.InvSubNib(cont)
            #
            result = self.xor(pops,k0)
            Results += result
            text = ''
        for i in range(0, len(Results), 8):
            byte = Results[i:i+8]
            text += chr(int(byte, 2))
        return text
    

# def main():
#     aess = AES()
#     txt = "hello there my friend I have come from a far way"
#     key = "1010011100111011"
#     cipher = aess.encrypt(txt, key)
#     print(cipher)
#     plain = aess.decrypt(cipher, key)
#     print(plain)
#     return 1


# if __name__ =="__main__":
#     main()