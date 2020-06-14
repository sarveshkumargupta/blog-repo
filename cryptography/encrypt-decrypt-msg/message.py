from Crypto import Random
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # generating a random key of 16 byte
iv = Random.new().read(AES.block_size)  # the Initialization Vector


def encrypt_msg(data):
    aes = AES.new(key, AES.MODE_CBC, iv)  # creating AES object
    pad_data = pad(data.encode('utf-8'), AES.block_size)  # padding a message to have 16 bytes block size
    enc_data = aes.encrypt(pad_data)  # encrypting the padding data
    return enc_data


def decrypt_msg(data):
    aes = AES.new(key, AES.MODE_CBC, iv)
    dec_data = aes.decrypt(data)
    unpad_data = unpad(dec_data, AES.block_size)
    out = unpad_data.decode('utf-8')
    return out


message = "I Love Making Blog"
enc = encrypt_msg(message)
print(enc)
dec = decrypt_msg(enc)
print(dec)
