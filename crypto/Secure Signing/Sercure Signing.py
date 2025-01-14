from pwn import *
from hashlib import sha256

SERVER_IP = "94.237.57.222"
SERVER_PORT = 55943

def xor(a, b):
    return bytes([i ^ j for i, j in zip(a, b)])

def find_flag():
    p = remote(SERVER_IP, SERVER_PORT)

    message = b"Hello"
    p.sendline(message)  

    response = p.recvuntil(b"Hash: ").decode()
    print("Received:", response)

    hsh = p.recvline().strip().split(b"Hash: ")[1].strip()
    print("Hash Received:", hsh.decode())

    FLAG_guess = xor(message, bytes.fromhex(hsh.decode()))
    print("Guessed FLAG:", FLAG_guess.decode())

    p.close()

if __name__ == "__main__":
    find_flag()
