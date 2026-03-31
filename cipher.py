import string
def caesar_cipher(text, action):
    shift = 3
    if action == "decrypt":
        shift = 26 - shift
    text = text.upper()
    print("CAESAR CIPHER\n\n")
    result = ""
    for ch in text:
        if ch.isalpha():
            original = ord(ch) - 65
            shifted = (original + shift) % 26
            new_char = chr(shifted + 65)

            print(f"{ch} -> {original} -> {shifted} -> {new_char}\n")
            result += new_char
        else:
            print(f"{ch} -> ignored\n")
            result += ch
    return result
def generate_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    used = set()
    letters = []
    for c in key + alphabet:
        if c not in used and c.isalpha():
            used.add(c)
            letters.append(c)
    matrix = [letters[i*5:(i+1)*5] for i in range(5)]
    return matrix
def find_position(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c
def create_pairs(text):
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs
def playfair_cipher(text, key, action):
    text = text.upper().replace("J", "I")
    text = "".join(filter(str.isalpha, text))
    matrix = generate_matrix(key)
    print("Key Matrix:\n")
    for row in matrix:
        print(" ".join(row)+ "\n")
    pairs = create_pairs(text)
    print("\nPairs:\n" + " ".join(pairs) + "\n\n")
    result = ""
    for pair in pairs:
        a, b = pair
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            shift = 1 if action == "encrypt" else -1
            newA = matrix[r1][(c1 + shift) % 5]
            newB = matrix[r2][(c2 + shift) % 5]
            print(f"{pair} -> Same Row -> {newA}{newB}\n")
        elif c1 == c2:
            shift = 1 if action == "encrypt" else -1
            newA = matrix[(r1 + shift) % 5][c1]
            newB = matrix[(r2 + shift) % 5][c2]
            print(f"{pair} -> Same Column -> {newA}{newB}\n")
        else:
            newA = matrix[r1][c2]
            newB = matrix[r2][c1]
            print(f"{pair} -> Rectangle -> {newA}{newB}\n")
        result += newA + newB
    return result
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None
def hill_cipher(text, key, action):
    text = "".join([c for c in text.upper() if c.isalpha()])
    a,b,c,d = key
    print("HILL CIPHER\n\n")
    matrix = [[a,b],[c,d]]
    if action == "decrypt":
        det = (a*d - b*c) % 26
        print(f"Determinant = ({a}×{d} - {b}×{c}) mod 26 = {det}\n")
        det_inv = mod_inverse(det,26)
        if det_inv is None:
            return "Matrix not invertible mod 26", ""
        print(f"Determinant Inverse = {det_inv}\n\n")
        adj = [[d,-b],[-c,a]]
        print("Adjoint Matrix:\n")
        print(f"[{d} {-b}]\n")
        print(f"[{-c} {a}]\n\n")
        matrix = [
            [(adj[0][0]*det_inv)%26,(adj[0][1]*det_inv)%26],
            [(adj[1][0]*det_inv)%26,(adj[1][1]*det_inv)%26]
        ]
        print("Inverse Key Matrix:\n")
        print(f"{matrix[0]}\n{matrix[1]}\n\n")
    print("Working Matrix:\n")
    print(f"{matrix[0]}\n{matrix[1]}\n\n")
    if len(text)%2!=0:
        text += "X"
        print("Text padded with X\n\n")
    result=""
    for i in range(0,len(text),2):
        p1 = ord(text[i]) - 65
        p2 = ord(text[i+1]) - 65
        print(f"Pair: {text[i]}{text[i+1]} -> [{p1},{p2}]\n")
        r1 = matrix[0][0]*p1 + matrix[0][1]*p2
        r2 = matrix[1][0]*p1 + matrix[1][1]*p2
        print(f"Row1: ({matrix[0][0]}×{p1}) + ({matrix[0][1]}×{p2}) = {r1}\n")
        print(f"Row2: ({matrix[1][0]}×{p1}) + ({matrix[1][1]}×{p2}) = {r2}\n")
        c1 = r1 % 26
        c2 = r2 % 26
        out1 = chr(c1 + 65)
        out2 = chr(c2 + 65)
        print(f"mod26: {r1}%26={c1}, {r2}%26={c2}\n")
        print(f"Output: {out1}{out2}\n\n")
        result += out1 + out2
    return result
print("\n==== Substitution Cipher ====\n")
print("1 Caesar Cipher")
print("2 Playfair Cipher")
print("3 Hill Cipher")
print("4 Exit")
while True:
    choice=input("Enter choice: ")
    if choice=="4":
        break
    action=input("Encrypt / Decrypt: ").lower()
    text=input("Enter message: ")
    if choice=="1":
        res=caesar_cipher(text,action)
    elif choice=="2":
        key=input("Enter Playfair key: ")
        res=playfair_cipher(text,key,action)
    elif choice=="3":
        key=list(map(int,input("Enter 4 numbers for 2x2 key matrix: ").split()))
        res=hill_cipher(text,key,action)
    else:
        print("Invalid choice")
        continue
    print("\nFinal Output:",res)