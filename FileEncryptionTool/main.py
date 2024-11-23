import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
import secrets

# Helper functions for secure key generation and password derivation
def generate_key(password: str, salt: bytes) -> bytes:
    """Derive a secure encryption key from a password."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Encryption function
def encrypt_file(input_file: str, password: str, output_file: str) -> None:
    """Encrypt a file securely using AES-GCM."""
    salt = secrets.token_bytes(16)
    key = generate_key(password, salt)
    
    with open(input_file, "rb") as f:
        data = f.read()
    
    # Padding the data for AES block size compatibility
    padder = PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    # Generate nonce for AES-GCM
    nonce = secrets.token_bytes(12)
    
    # Encrypting the data
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    tag = encryptor.tag
    
    # Save salt, nonce, tag, and ciphertext to the output file
    with open(output_file, "wb") as f:
        f.write(salt + nonce + tag + ciphertext)
    
    print(f"File '{input_file}' encrypted and saved to '{output_file}'.")

# Decryption function
def decrypt_file(input_file: str, password: str, output_file: str) -> None:
    """Decrypt a file encrypted with AES-GCM."""
    with open(input_file, "rb") as f:
        file_data = f.read()
    
    # Extract salt, nonce, tag, and ciphertext
    salt = file_data[:16]
    nonce = file_data[16:28]
    tag = file_data[28:44]
    ciphertext = file_data[44:]
    
    key = generate_key(password, salt)
    
    # Decrypting the data
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Remove padding
    unpadder = PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    
    with open(output_file, "wb") as f:
        f.write(data)
    
    print(f"File '{input_file}' decrypted and saved to '{output_file}'.")


def main():
    print("Secure File Encryption Tool")
    mode = input("Choose mode:\n(1) Encrypt \n(2) Decrypt: \n(0) Exit: \n").strip()
    if mode == "1":
        input_path = input("Enter path to file to encrypt: ").strip()
        password = input("Enter password for encryption: ").strip()
        output_path = input("Enter path to save encrypted file: ").strip()
        encrypt_file(input_path, password, output_path)
    elif mode == "2":
        input_path = input("Enter path to encrypted file: ").strip()
        password = input("Enter password for decryption: ").strip()
        output_path = input("Enter path to save decrypted file: ").strip()
        decrypt_file(input_path, password, output_path)
    elif mode == "0":
        print("Exiting...")
        exit(0)
    else:
        print("Invalid option!")
        main()

# Usage example
if __name__ == "__main__":
    main()

