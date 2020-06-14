from Crypto import Random
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

key = get_random_bytes(16)  # generating a random key of 16 byte
iv = Random.new().read(AES.block_size)  # the Initialization Vector


def encrypt_msg(file_name):
    aes = AES.new(key, AES.MODE_CBC, iv)  # creating AES object
    with open(file_name, 'rb') as f:  # opening the file and reading
        file = f.read()
    pad_data = pad(file, AES.block_size)  # padding the file to have 16 bytes block size
    enc_data = aes.encrypt(pad_data)  # encrypting the padding data
    enc_file = file_name + '.enc'
    with open(enc_file, 'wb') as f:
        f.write(enc_data)  # encrypting all the content inside the file
    os.remove(file_name)  # removing the original file
    return enc_file


def decrypt_msg(file_name):
    aes = AES.new(key, AES.MODE_CBC, iv)
    with open(file_name, 'rb') as f:
        file = f.read()
    dec_data = aes.decrypt(file)
    unpad_data = unpad(dec_data, AES.block_size)
    with open(file_name[:-4], 'wb') as f:
        f.write(unpad_data)
    os.remove(file_name)
    return file_name


file = encrypt_msg('myfile.txt')
decrypt_msg(file)
