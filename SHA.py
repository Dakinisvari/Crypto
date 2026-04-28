 
import math 
 
def rotr(x, n): 
    return ((x >> n) | (x << (64 - n))) & 0xffffffffffffffff 
 
def shr(x, n): 
    return x >> n 
 
def Ch(x, y, z): 
    return (x & y) ^ (~x & z) 
 
def Maj(x, y, z): 
    return (x & y) ^ (x & z) ^ (y & z) 
 
def Sigma0(x): 
    return rotr(x,28) ^ rotr(x,34) ^ rotr(x,39) 
 
def Sigma1(x): 
    return rotr(x,14) ^ rotr(x,18) ^ rotr(x,41) 
 
def sigma0(x): 
    return rotr(x,1) ^ rotr(x,8) ^ shr(x,7) 
 
def sigma1(x): 
    return rotr(x,19) ^ rotr(x,61) ^ shr(x,6) 
 
def to_hex(x): 
    return f"{x:016x}" 
 
K = [ 
0x428a2f98d728ae22,0x7137449123ef65cd,0xb5c0fbcfec4d3b2f,0xe9b5dba58189dbbc, 
0x3956c25bf348b538,0x59f111f1b605d019,0x923f82a4af194f9b,0xab1c5ed5da6d8118, 
0xd807aa98a3030242,0x12835b0145706fbe,0x243185be4ee4b28c,0x550c7dc3d5ffb4e2, 
0x72be5d74f27b896f,0x80deb1fe3b1696b1,0x9bdc06a725c71235,0xc19bf174cf692694, 
0xe49b69c19ef14ad2,0xefbe4786384f25e3,0x0fc19dc68b8cd5b5,0x240ca1cc77ac9c65, 
0x2de92c6f592b0275,0x4a7484aa6ea6e483,0x5cb0a9dcbd41fbd4,0x76f988da831153b5, 
0x983e5152ee66dfab,0xa831c66d2db43210,0xb00327c898fb213f,0xbf597fc7beef0ee4, 
0xc6e00bf33da88fc2,0xd5a79147930aa725,0x06ca6351e003826f,0x142929670a0e6e70, 
0x27b70a8546d22ffc,0x2e1b21385c26c926,0x4d2c6dfc5ac42aed,0x53380d139d95b3df, 
0x650a73548baf63de,0x766a0abb3c77b2a8,0x81c2c92e47edaee6,0x92722c851482353b, 
0xa2bfe8a14cf10364,0xa81a664bbc423001,0xc24b8b70d0f89791,0xc76c51a30654be30, 
0xd192e819d6ef5218,0xd69906245565a910,0xf40e35855771202a,0x106aa07032bbd1b8, 
0x19a4c116b8d2d0c8,0x1e376c085141ab53,0x2748774cdf8eeb99,0x34b0bcb5e19b48a8, 
0x391c0cb3c5c95a63,0x4ed8aa4ae3418acb,0x5b9cca4f7763e373,0x682e6ff3d6b2b8a3, 
0x748f82ee5defb2fc,0x78a5636f43172f60,0x84c87814a1f0ab72,0x8cc702081a6439ec, 
0x90befffa23631e28,0xa4506cebde82bde9,0xbef9a3f7b2c67915,0xc67178f2e372532b, 
0xca273eceea26619c,0xd186b8c721c0c207,0xeada7dd6cde0eb1e,0xf57d4f7fee6ed178, 
0x06f067aa72176fba,0x0a637dc5a2c898a6,0x113f9804bef90dae,0x1b710b35131c471b, 
0x28db77f523047d84,0x32caab7b40c72493,0x3c9ebe0a15c9bebc,0x431d67c49c100d4c, 
0x4cc5d4becb3e42b6,0x597f299cfc657e2a,0x5fcb6fab3ad6faec,0x6c44198c4a475817 
] 
 
INITIAL_H = [ 
0x6a09e667f3bcc908,0xbb67ae8584caa73b, 
0x3c6ef372fe94f82b,0xa54ff53a5f1d36f1, 
0x510e527fade682d1,0x9b05688c2b3e6c1f, 
0x1f83d9abfb41bd6b,0x5be0cd19137e2179 
] 
 
def sha512(message): 
    log = "=========== SHA-512 PROCESS START ===========\n\n" 
 
    H = INITIAL_H.copy() 
    msg = message.encode() 
 
    log += "STEP 1: INPUT\n" 
    log += f"Message = {message}\n" 
    log += "Hex = " + ' '.join(f"{b:02x}" for b in msg) + "\n\n" 
 
    # STEP 2: PADDING (DETAILED) 
    log += "STEP 2: PADDING (DETAILED)\n" 
    bit_len = len(msg) * 8 
    log += f"Original Length = {bit_len} bits\n\n" 
 
    padded = list(msg) 
    padded.append(0x80) 
 
    log += "After appending 0x80:\n" 
    log += ' '.join(f"{x:02x}" for x in padded) + "\n\n" 
 
    zero_count = 0 
    while (len(padded) % 128) != 112: 
        padded.append(0) 
        zero_count += 1 
 
    log += f"Zero bytes added = {zero_count}\n\n" 
 
    length_bytes = bit_len.to_bytes(16, 'big') 
    log += "Length (128-bit big endian):\n" 
    log += ' '.join(f"{x:02x}" for x in length_bytes) + "\n\n" 
 
    padded += list(length_bytes) 
 
    log += "Final Block (first 128 bytes):\n" 
    log += ' '.join(f"{x:02x}" for x in padded[:128]) + "\n\n" 
 
    # PROCESS BLOCKS 
    for i in range(0, len(padded), 128): 
        block = padded[i:i+128] 
 
        log += "STEP 3: MESSAGE SCHEDULE\n" 
 
        W = [] 
        for t in range(16): 
            val = int.from_bytes(bytes(block[t*8:(t+1)*8]), 'big') 
            W.append(val) 
            log += f"W[{t}] = {to_hex(val)}\n" 
 
        for t in range(16, 80): 
            val = (sigma1(W[t-2]) + W[t-7] + sigma0(W[t-15]) + W[t-16]) & 0xffffffffffffffff 
            W.append(val) 
 
        log += "\nSTEP 4: ROUND PROCESS (first 10 rounds)\n" 
 
        a,b,c,d,e,f,g,h = H 
 
        for t in range(80): 
            T1 = (h + Sigma1(e) + Ch(e,f,g) + K[t] + W[t]) & 0xffffffffffffffff 
            T2 = (Sigma0(a) + Maj(a,b,c)) & 0xffffffffffffffff 
 
            h,g,f,e,d,c,b,a = g,f,e,(d+T1)&0xffffffffffffffff,c,b,a,(T1+T2)&0xffffffffffffffff 
 
            if t < 4: 
                log += f"Round {t}:\n" 
                log += f"  T1 = {to_hex(T1)}\n" 
                log += f"  T2 = {to_hex(T2)}\n" 
                log += f"  a={to_hex(a)} b={to_hex(b)} e={to_hex(e)}\n\n" 
 
        # Update hash 
        H = [(H[j] + val) & 0xffffffffffffffff for j, val in enumerate([a,b,c,d,e,f,g,h])] 
 
    log += "STEP 5: FINAL HASH\n" 
    digest = ''.join(to_hex(x) for x in H) 
    log += "SHA-512 = " + digest + "\n" 
 
    log += "\n=========== END ===========" 
    return log 
 
if __name__ == "__main__": 
    msg = input("Enter message: ") 
    print(sha512(msg))
