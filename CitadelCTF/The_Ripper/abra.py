import bcrypt

def crack_bcrypt_hash(hash_file='hash.txt', wordlist_file='wordlist.txt'):
    # Read bcrypt hash from file
    with open(hash_file, 'r') as f:
        hashed = f.read().strip().encode()

    # Open wordlist and try each password
    with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            password = line.strip().encode()
            if bcrypt.checkpw(password, hashed):
                print(f"Passcode found: {password.decode()}")
                print(f"Flag: citadel{{{password.decode()}}}")
                return

    print("Passcode not found in wordlist.")

if __name__ == '__main__':
    crack_bcrypt_hash()
