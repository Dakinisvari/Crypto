import math 
def left_rotate(x, c): 
    return ((x << c) | (x >> (32 - c))) & 0xffffffff 
 
def F(x,y,z): return (x & y) | (~x & z) 
def G(x,y,z): return (x & z) | (y & ~z) 
def H(x,y,z): return x ^ y ^ z 
def I(x,y,z): return y ^ (x | ~z) 
 
T = [int(abs(math.sin(i+1)) * (2**32)) & 0xffffffff for i in range(64)] 
 
S = [ 
7,12,17,22, 7,12,17,22, 7,12,17,22, 7,12,17,22, 
5,9,14,20, 5,9,14,20, 5,9,14,20, 5,9,14,20, 
4,11,16,23, 4,11,16,23, 4,11,16,23, 4,11,16,23, 
6,10,15,21, 6,10,15,21, 6,10,15,21, 6,10,15,21 
] 
 
def real_md5(message): 
    log = "=========== MD5 PROCESS START ===========\n\n" 
 
    msg_bytes = message.encode() 
 
    log += "STEP 1: INPUT\n" 
    log += "Message = " + message + "\n" 
    log += "Hex = " + ' '.join(f"{x:02x}" for x in msg_bytes) + "\n\n" 
 
    # STEP 2: PADDING 
    log += "STEP 2: PADDING (DETAILED)\n" 
 
    original_bit_length = len(msg_bytes) * 8 
    log += f"Original Length: {original_bit_length} bits\n\n" 
 
    padded = list(msg_bytes) 
 
    # Append 0x80 
    padded.append(0x80) 
    log += "After appending 0x80:\n" 
    log += ' '.join(f"{x:02x}" for x in padded) + "\n\n" 
 
    # Zero padding 
    zero_count = 0 
    while (len(padded) % 64) != 56: 
        padded.append(0x00) 
        zero_count += 1 
 
    log += f"Zero bytes added = {zero_count}\n" 
    log += "After zero padding:\n" 
    log += ' '.join(f"{x:02x}" for x in padded) + "\n\n" 
 
    # STEP 3: APPEND LENGTH 
    log += "STEP 3: APPEND LENGTH (DETAILED)\n" 
 
    low = original_bit_length & 0xffffffff 
    high = (original_bit_length >> 32) & 0xffffffff 
 
    length_bytes = [] 
 
    for i in range(4): 
        length_bytes.append((low >> (8*i)) & 0xff) 
    for i in range(4): 
        length_bytes.append((high >> (8*i)) & 0xff) 
 
    log += "64-bit Length (Little Endian):\n" 
    log += ' '.join(f"{x:02x}" for x in length_bytes) + "\n\n" 
 
    padded += length_bytes 
 
    log += "Final 512-bit Block:\n" 
    log += ' '.join(f"{x:02x}" for x in padded) + "\n\n" 
 
    # STEP 4: INIT 
    A = 0x67452301 
    B = 0xefcdab89 
    C = 0x98badcfe 
    D = 0x10325476 
 
    for i in range(0, len(padded), 64): 
 
        M = [] 
 
        for j in range(0, 64, 4): 
            M.append( 
                padded[i+j] | 
                (padded[i+j+1] << 8) | 
                (padded[i+j+2] << 16) | 
                (padded[i+j+3] << 24) 
            ) 
 
        a, b, c, d = A, B, C, D 
 
        for k in range(64): 
 
            if k < 16: 
                f = F(b,c,d) 
                g = k 
            elif k < 32: 
                f = G(b,c,d) 
                g = (5*k+1) % 16 
            elif k < 48: 
                f = H(b,c,d) 
                g = (3*k+5) % 16 
            else: 
                f = I(b,c,d) 
                g = (7*k) % 16 
 
            temp = d 
            d = c 
            c = b 
 
            s = (a + f) & 0xffffffff 
            s = (s + T[k]) & 0xffffffff 
            s = (s + M[g]) & 0xffffffff 
 
            s = left_rotate(s, S[k]) 
            b = (b + s) & 0xffffffff 
 
            a = temp 
 
        A = (A + a) & 0xffffffff 
        B = (B + b) & 0xffffffff 
        C = (C + c) & 0xffffffff 
        D = (D + d) & 0xffffffff 
 
    def to_hex_le(x): 
        return ''.join(f"{(x >> (8*i)) & 0xff:02x}" for i in range(4)) 
 
    hash_val = to_hex_le(A) + to_hex_le(B) + to_hex_le(C) + to_hex_le(D) 
 
    log += "STEP 6: FINAL HASH\n" 
    log += "MD5 = " + hash_val + "\n" 
 
    log += "\n=========== END ==========="  
 
    return log 
 
if __name__ == "__main__": 
    msg = input("Enter message: ") 
    print(real_md5(msg)) 
