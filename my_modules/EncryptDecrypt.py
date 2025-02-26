from cryptography.fernet import Fernet

# Function to generate a key and print it
def generate_key():
    key = Fernet.generate_key()
    print(f"🔑 Encryption Key (SAVE THIS!): {key.decode()}")
    return key

# Function to encrypt a file (Overwrites the original file)
def encrypt_file(filename):
    key = generate_key()  # Generate a key
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()  # Read original file content

    encrypted_data = cipher.encrypt(file_data)  # Encrypt the file content

    with open(filename, "wb") as file:
        file.write(encrypted_data)  # Overwrite the file with encrypted content

    print(f"File '{filename}' has been encrypted (original file is overwritten).")

# Function to decrypt a file (Overwrites the original file)
def decrypt_file(filename, key):
    try:
        cipher = Fernet(key.encode())  # Convert key to bytes

        with open(filename, "rb") as file:
            encrypted_data = file.read()  # Read encrypted file

        decrypted_data = cipher.decrypt(encrypted_data)  # Decrypt content

        with open(filename, "wb") as file:
            file.write(decrypted_data)  # Overwrite with decrypted content

        print(f"File '{filename}' has been decrypted and restored.")
    except Exception as e:
        print("❌ Error: Invalid key or corrupted file!")

