import os

class AES:
    def __init__(self):
        self.sub_Box = [
            # OriginalNib
            [0b0000, 0b0001, 0b0010, 0b0011, 0b0100, 0b0101, 0b0110, 0b0111], 
            # Substitution
            [0b1001, 0b0100, 0b1010, 0b1011, 0b1101, 0b0001, 0b1000, 0b0101],
            # OriginalNib
            [0b1000, 0b1001, 0b1010, 0b1011, 0b1100, 0b1101, 0b1110, 0b1111], 
            # Substitution
            [0b0110, 0b0010, 0b0000, 0b0011, 0b1100, 0b1110, 0b1111, 0b0111]
        ]
        
    def generate_key(self):
        key = os.urandom(16)
        return key
    
    def print_key(self, key):
        for byte in key:
            print(byte)
    
    def format_sub_box(self):
        for i in range(len(self.sub_Box)):
            for j in range(len(self.sub_Box[i])):
                self.sub_Box[i][j] = format(self.sub_Box[i][j], "04b")
    
    def rot_nib(self, key):
        temp1 = key[0]
        temp2 = key[1]
        
        key[0] = key[2]
        key[1] = key[3]
        
        key[2] = temp1
        key[3] = temp2
        
        return key
    
    def sub_nib(self, key):
        for i in range(len(key)):
            Div1 = key[i][:4]
            Div2 = key[i][4:]
            
            flagDiv1 = 0
            flagDiv2 = 0
            
            y = 0
            while y < len(self.sub_Box):
                for z in range(len(self.sub_Box[y])):
                    if flagDiv1 == 0:
                        if key[i][:4] == self.sub_Box[y][z]:
                            Div1 = self.sub_Box[y + 1][z]
                            flagDiv1 = 1
                    if flagDiv2 == 0:
                        if key[i][4:] == self.sub_Box[y][z]:
                            Div2 = self.sub_Box[y + 1][z]
                            flagDiv2 = 1
                        
                    if flagDiv1 == 1 and flagDiv2 == 1:
                        key[i] = Div1 + Div2
                        break
                y = y + 2
        return key
    
    def decimal_to_binary(self, n):
        return '{:032b}'.format(n)
    
    def expand_key(self, key):
        key_array = []
        for i in range(len(key)):
            key_array.append(format(key[i], "08b"))
        
        multi_array_key = []
        rows, cols = (4, 4)
        i = 0
        for r in range(rows):
            col = []
            for c in range(cols):
                col.append(key_array[i])
                i += 1
            multi_array_key.append(col)
        
        fw = 0
        for i in range(9):
            print('last word:', multi_array_key[3])
            multi_array_key.append([0] * 4)
            
            if i == 0:
                temp = multi_array_key[fw + 3][0]
                multi_array_key[fw + 3][0] = multi_array_key[fw + 3][1]
                multi_array_key[fw + 3][1] = multi_array_key[fw + 3][2]
                multi_array_key[fw + 3][2] = multi_array_key[fw + 3][3]
                multi_array_key[fw + 3][3] = temp
                
                for i in range(len(multi_array_key[fw + 3])):
                    multi_array_key[fw + 3][i] = format(multi_array_key[fw + 3][i], "08b")
                    
                for i in range(len(multi_array_key[fw])):
                    multi_array_key[fw + 4][i] = format(int(multi_array_key[fw][i], 2) ^ int(multi_array_key[fw + 3][i], 2), "08b")
                    
                for i in range(len(multi_array_key[fw + 4])):
                    multi_array_key[fw + 4][i] = format(multi_array_key[fw + 4][i], "08b")
                    
                temp = multi_array_key[fw + 4][0]
                multi_array_key[fw + 4][0] = multi_array_key[fw + 4][1]
                multi_array_key[fw + 4][1] = multi_array_key[fw + 4][2]
                multi_array_key[fw + 4][2] = multi_array_key[fw + 4][3]
                multi_array_key[fw + 4][3] = temp
                
                for i in range(len(multi_array_key[fw + 4])):
                    multi_array_key[fw + 4][i] = format(multi_array_key[fw + 4][i], "08b")
                    
                for i in range(len(multi_array_key[fw])):
                    multi_array_key[fw + 5][i] = format(int(multi_array_key[fw + 4][i], 2) ^ int(multi_array_key[fw][i], 2), "08b")
                    
                for i in range(len(multi_array_key[fw + 5])):
                    multi_array_key[fw + 5][i] = format(multi_array_key[fw + 5][i], "08b")
                    
                for i in range(len(multi_array_key[fw + 3])):
                    multi_array_key[fw + 6][i] = multi_array_key[fw + 3][i]
                    
                for i in range(len(multi_array_key[fw + 6])):
                    multi_array_key[fw + 6][i] = format(multi_array_key[fw + 6][i], "08b")
                    
                for i in range(len(multi_array_key[fw + 4])):
                    multi_array_key[fw + 6][i] = format(int(multi_array_key[fw + 4][i], 2) ^ int(multi_array_key[fw + 3][i], 2), "08b")
                    
                for i in range(len(multi_array_key[fw + 6])):
                    multi_array_key[fw + 6][i] = format(multi_array_key[fw + 6][i], "08b")
                    
                for i in range(len(multi_array_key[fw + 5])):
                    multi_array_key[fw + 7][i] = multi_array_key[fw + 5][i]
                    
                for i in range(len(multi_array_key[fw + 7])):
                    multi_array_key[fw + 7][i] = format(multi_array_key[fw + 7][i], "08b")
                    
                for i in range(len(multi_array_key[fw + 6])):
                    multi_array_key[fw + 7][i] = format(int(multi_array_key[fw + 6][i], 2) ^ int(multi_array_key[fw + 5][i], 2), "08b")
                    
                for i in range(len(multi_array_key[fw + 7])):
                    multi_array_key[fw + 7][i] = format(multi_array_key[fw + 7][i], "08b")
                    
                fw = fw + 4
                
            if i == 1 or i == 2 or i == 3:
                for j in range(len(multi_array_key[fw])):
                    multi_array_key[fw + 4][j] = format(int(multi_array_key[fw][j], 2) ^ int(multi_array_key[fw + 3][j], 2), "08b")
                    
                for j in range(len(multi_array_key[fw + 4])):
                    multi_array_key[fw + 4][j] = format(multi_array_key[fw + 4][j], "08b")
                    
                temp = multi_array_key[fw + 4][0]
                multi_array_key[fw + 4][0] = multi_array_key[fw + 4][1]
                multi_array_key[fw + 4][1] = multi_array_key[fw + 4][2]
                multi_array_key[fw + 4][2] = multi_array_key[fw + 4][3]
                multi_array_key[fw + 4][3] = temp
                
                for j in range(len(multi_array_key[fw + 4])):
                    multi_array_key[fw + 4][j] = format(multi_array_key[fw + 4][j], "08b")
                    
                for j in range(len(multi_array_key[fw])):
                    multi_array_key[fw + 5][j] = format(int(multi_array_key[fw + 4][j], 2) ^ int(multi_array_key[fw][j], 2), "08b")
                    
                for j in range(len(multi_array_key[fw + 5])):
                    multi_array_key[fw + 5][j] = format(multi_array_key[fw + 5][j], "08b")
                    
                for j in range(len(multi_array_key[fw + 3])):
                    multi_array_key[fw + 6][j] = multi_array_key[fw + 3][j]
                    
                for j in range(len(multi_array_key[fw + 6])):
                    multi_array_key[fw + 6][j] = format(multi_array_key[fw + 6][j], "08b")
                    
                for j in range(len(multi_array_key[fw + 4])):
                    multi_array_key[fw + 6][j] = format(int(multi_array_key[fw + 4][j], 2) ^ int(multi_array_key[fw + 3][j], 2), "08b")
                    
                for j in range(len(multi_array_key[fw + 6])):
                    multi_array_key[fw + 6][j] = format(multi_array_key[fw + 6][j], "08b")
                    
                for j in range(len(multi_array_key[fw + 5])):
                    multi_array_key[fw + 7][j] = multi_array_key[fw + 5][j]
                    
                for j in range(len(multi_array_key[fw + 7])):
                    multi_array_key[fw + 7][j] = format(multi_array_key[fw + 7][j], "08b")
                    
                for j in range(len(multi_array_key[fw + 6])):
                    multi_array_key[fw + 7][j] = format(int(multi_array_key[fw + 6][j], 2) ^ int(multi_array_key[fw + 5][j], 2), "08b")
                    
                for j in range(len(multi_array_key[fw + 7])):
                    multi_array_key[fw + 7][j] = format(multi_array_key[fw + 7][j], "08b")
                    
                fw = fw + 4
                
            if i == 4 or i == 5 or i == 6:
                for j in range(len(multi_array_key[fw])):
                    multi_array_key[fw + 4][j] = format(int(multi_array_key[fw][j], 2) ^ int(multi_array_key[fw + 3][j], 2), "08b")
                    
                for j in range(len(multi_array_key[fw + 4])):
                    multi_array_key[fw + 4][j] = format(multi_array_key[fw + 4][j], "08b")
                    
                temp = multi_array_key[fw + 4][0]
                multi_array_key[fw + 4][0] = multi_array_key[fw + 4][1]
                multi_array_key[fw + 4][1] = multi_array_key[fw + 4][2]
                multi_array_key[fw + 4][2] = multi_array_key[fw + 4][3]
                multi_array_key[fw + 4][3] = temp
                
                for j in range(len(multi_array_key[fw + 4])):
                    multi_array_key[fw + 4][j] = format(multi_array_key[fw + 4][j], "08b")
                    
                for j in range(len(multi_array_key[fw])):
                    multi_array_key[fw + 5][j] = format(int(multi_array_key[fw + 4][j], 2) ^ int(multi_array_key[fw][j], 2), "08b")
                    
                for j in range(len(multi_array_key[fw + 5])):
                    multi_array_key[fw + 5][j] = format(multi_array_key[fw + 5][j], "08b")
                    
                for j in range(len(multi_array_key[fw + 3])):
                    multi_array_key[fw + 6][j] = multi_array_key[fw + 3][j]
                    
                for j in range(len(multi_array_key[fw + 6])):
                    multi_array_key[fw + 6][j] = format(multi_array_key[fw + 6][j], "08b")
                    
                for j in range(len(multi_array_key[fw + 4])):
                    multi_array_key[fw + 6][j] = format(int(multi_array_key[fw + 4][j], 2) ^ int(multi_array_key[fw + 3][j], 2), "08b")
                    
                for j in range(len(multi_array_key[fw + 6])):
                    multi_array_key[fw + 6][j] = format(multi_array_key[fw + 6][j], "08b")
                    
                for j in range(len(multi_array_key[fw + 5])):
                    multi_array_key[fw + 7][j] = multi_array_key[fw + 5][j]
                    
                for j in range(len(multi_array_key[fw + 7])):
                    multi_array_key[fw + 7][j] = format(multi_array_key[fw + 7][j], "08b")
                    
                for j in range(len(multi_array_key[fw + 6])):
                    multi_array_key[fw + 7][j] = format(int(multi_array_key[fw + 6][j], 2) ^ int(multi_array_key[fw + 5][j], 2), "08b")
                    
                for j in range(len(multi_array_key[fw + 7])):
                    multi_array_key[fw + 7][j] = format(multi_array_key[fw + 7][j], "08b")
                    
                fw = fw + 4
                
        for i in range(len(multi_array_key)):
            for j in range(len(multi_array_key[i])):
                multi_array_key[i][j] = int(multi_array_key[i][j], 2)
        
        expanded_key = []
        for i in range(len(multi_array_key)):
            for j in range(len(multi_array_key[i])):
                expanded_key.append(multi_array_key[i][j])
                
        return expanded_key
