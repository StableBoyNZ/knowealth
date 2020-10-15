decrypt = input("Enter either 'd' to decrypt, or hit Enter to encrypt\n").lower()
output = []
decrypted = ""
key = 0
if decrypt == "d":
    key = int(input("Enter decryption key...\n"))
    stringInput = input("Enter coded message for decryption...\n")
    for i in range(len(stringInput)):
        output.append(ord(stringInput[i]) - key)
    print("ASCII: ", output)
    for i in range(len(output)):
        decrypted += chr(int(output[i]))
    print("\nDecrypted :", decrypted)
else:
    key = int(input("Enter encryption key...\n"))
    stringInput = input("Enter a phrase or word for encryption...\n")
    for i in range(len(stringInput)):
        output.append(ord(stringInput[i]) + key)
    print("ASCII: ", output)
    for i in range(len(output)):
        decrypted += chr(int(output[i]))
    print("\nEncrypted :", decrypted)
