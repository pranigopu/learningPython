# Main functions...
def nextSpecialChar(c, n):
    j = 1
    if n < 0: j, n = -1, -n
    i, count = ord(c) + j, 0
    while count < n - 1:
        if not chr(i).isalnum(): count, i = count + 1, i + j
        while chr(i).isalnum(): i = i + j
    print()
    return chr(i)
def offsetChar(c, key):
    if c.isspace(): return c
    x, min, max = ord(c) + key, 0, 0
    if c >= "0" and c <= "9": min, max = ord("0"), ord("9")
    elif c >= "A" and c <= "Z": min, max = ord("A"), ord("Z")
    elif c >= "a" and c <= "z": min, max = ord("a"), ord("z")
    else: return nextSpecialChar(c, key)
    # If alphanumeric...
    if x > max: return chr(min + (x - max) - 1)
    elif x < min: return chr(max - (min - x) + 1)
    return chr(x)
def encrypt(original, key):
    try: key = int(key)
    except: return "Invalid key!"
    encrypted = ""
    for c in original: encrypted = encrypted + offsetChar(c, key)
    return "Encrypted message:\n" + encrypted
def decrypt(encrypted, key):
    try: key = int(key)
    except: return "Invalid key!"
    original = ""
    for c in encrypted: original = original + offsetChar(c, -key)
    return "Original message:\n" + original
#------------------------
# Other functions...
def sectionTitle(title): print("------------\n" + title.upper() + "\n______")
def e():
    sectionTitle("encrypter")
    x, key = input("Input string to enrypt: "), input("Input key: ")
    print(encrypt(x, key))
def d():
    sectionTitle("decrypter")
    x, key = input("Input string to decrypt: "), input("Input key: ")
    print(decrypt(x, key))
def q():
    print("Goodbye!\n")
    exit()
def error(): print("Invalid key!")
def h():
    print("Enter e for encryption.")
    print("Enter d for decryption.")
    print("Enter x for exit.")
def switch(option):
    try: return {"e":e, "d":d, "x":q, "?":h}[option]
    except: return error
#------------------------
# Main program
print("\nCAESAR ENCRYPTION AND DECRYPTION")
print("(Enter ? for help)")
while True: switch(input(">> "))()