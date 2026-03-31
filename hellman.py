p,g,a,b,A,B,K = None, None, None, None, None, None, None
def setup():
    global p, g, a, b
    p = int(input("Enter prime number p: "))
    g = int(input("Enter primitive root g: "))
    a = int(input("Enter Alice private key (a): "))
    b = int(input("Enter Bob private key (b): "))
    print("Parameters set.\n")
def generate_public_keys():
    global A, B
    A = pow(g, a, p)
    B = pow(g, b, p)
    print(f"Alice Public Key (A = g^a mod p) = {A}")
    print(f"Bob Public Key (B = g^b mod p) = {B}\n")
def generate_shared_secret():
    global K
    K_alice = pow(B, a, p)
    K_bob = pow(A, b, p)
    K = K_alice
    print(f"Alice computes (K = B^a mod p) = {K_alice}")
    print(f"Bob computes (K = A^b mod p) = {K_bob}")
    print(f"Shared Secret Key (K) = {K}\n")
def mod_inverse(k, p):
    for i in range(1, p):
        if (k * i) % p == 1:
            return i
    return None
setup()
generate_public_keys()
print("Exchanging public keys...\n")
print("Alice sends A to Bob.")
print("Bob sends B to Alice.\n")
generate_shared_secret()