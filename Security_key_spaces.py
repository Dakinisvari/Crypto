def cipher(message, k):
    result = []    
    for ch in message:
        digit = int(ch)
        new_digit = (digit + k) % 10
        result.append(str(new_digit))
    return "".join(result)
message = input().strip()
k = int(input().strip())
print(cipher(message, k))
