n, eValue, d = None, None, None
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
def mod_inverse(e, phi):
    t = 0
    new_t = 1
    r = phi
    new_r = e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None
    if t < 0:
        t += phi
    return t
def find_e(phi):
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            return e
    return None
def generate_keys():
    global n, eValue, d
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    print("\n===== KEY GENERATION =====")
    n = p * q
    phi = (p - 1) * (q - 1)
    print("Step 1: p =", p, "q =", q)
    print("Step 2: n = p × q =", n)
    print("Step 3: φ(n) = (p-1)(q-1) =", phi)
    eValue = find_e(phi)
    if eValue is None:
        print("Failed to find valid e")
        return
    print("Step 4: Choosing e such that gcd(e, φ(n)) = 1")
    print("e =", eValue)
    d = mod_inverse(eValue, phi)
    print("Step 5: d ≡ e⁻¹ mod φ(n)")
    print("d =", d)
    print("Verification: (e × d) mod φ(n) =", (eValue * d) % phi)
    print("\nPublic Key (n, e) =", (n, eValue))
    print("Private Key (d) =", d)
def encrypt():
    global n, eValue
    if n is None or eValue is None:
        print("Generate keys first!")
        return
    msg = input("\nEnter message: ")
    cipher = []
    print("\n===== ENCRYPTION =====")
    for ch in msg:
        m = ord(ch)
        C = pow(m, eValue, n)
        print(f"{ch} -> {m}^{eValue} mod {n} = {C}")
        cipher.append(C)
    print("\nEncrypted msg:", cipher)
    return cipher
def decrypt():
    global n, d
    if n is None or d is None:
        print("Generate keys first!")
        return
    cipher_text = input("\nEnter cipher numbers (space separated): ").split()
    message = ""
    print("\n===== DECRYPTION =====")
    for c in cipher_text:
        C = int(c)
        m = pow(C, d, n)
        ch = chr(m)
        print(f"{C}^{d} mod {n} = {m} -> {ch}")
        message += ch
    print("\nDecrypted message:", message)
generate_keys()
encrypt()
decrypt()