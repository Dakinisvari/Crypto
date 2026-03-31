
def euler_totient(n):
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result
def mod_power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result
def check_primitive_root():
    n = int(input("Enter n: "))
    a = int(input("Enter a: "))
    if n <= 1 or a <= 0:
        print("Enter valid values for n and a.")
        return
    phi = euler_totient(n)
    residues = set()
    print(f"\nChecking if {a} is a primitive root of {n}\n")
    for i in range(1, phi + 1):
        val = mod_power(a, i, n)
        residues.add(val)
        print(f"{a}^{i} mod {n} = {val}")

    if len(residues) == phi and 1 in residues:
        print("\nAll remainders are distinct")
        print(f"{a} is a primitive root of {n}")
    else:
        print("\nRemainders repeat")
        print(f"{a} is NOT a primitive root of {n}")
def find_gcd():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num1 <= 0 or num2 <= 0:
        print("Please enter two positive integers.")
        return
    print("\nUsing Formula:")
    print("gcd(a, b) = gcd(b, a mod b)\n")
    while num2 != 0:
        r = num1 % num2
        print(f"gcd({num1}, {num2}) = gcd({num2}, {r})\n")
        num1 = num2
        num2 = r
    print(f"GCD = {num1}")
print("1. Primitive Root Checker")
print("2. Euclidean Algorithm (GCD)")
print("3. Exit")
while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        check_primitive_root()
    elif choice == "2":
        find_gcd()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")