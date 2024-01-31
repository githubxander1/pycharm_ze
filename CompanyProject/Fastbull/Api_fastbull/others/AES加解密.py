# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


# 创建AES对象，使用CBC模式，使用一个16字节的随机IV
def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC, get_random_bytes(16))
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv
    return iv, ct_bytes


# 创建新的AES对象，用于解密
def aes_decrypt(iv, ct_bytes, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)
    return pt


# 生成一个随机密钥
key = get_random_bytes(16)

# 加密数据
data = b"Hello@2023"
iv, ct = aes_encrypt(data, key)
print("Ciphertext:", ct)

# 解密数据
decrypted = aes_decrypt(iv, ct, key)
print("Decrypted text:", decrypted)
