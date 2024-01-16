import base64
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad

# 密文（base64编码）
from cryptography.hazmat.primitives.ciphers.algorithms import AES

ciphertext = "OqRZEG9mm9B/y92h7+muvxXlcCtDYYxNO4XDimqoHjRZu9oTSsrcAnDKV5zUQbaT6H1NWjmyUGiNwlIBt5EwNTUZjN9GOPLSl/0TX27d3E0="
# 偏移量（16位）
iv = "Bai1unC1ub1sBest"
# 密钥（16位）
key = "c0iOcX2p1v782YUY"

# 将密文从base64格式解码为字节数组
ciphertext_bytes = base64.b64decode(ciphertext)

# 创建AES解密器
cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())

# 使用密钥和偏移量进行解密
plaintext_bytes = unpad(cipher.decrypt(ciphertext_bytes), AES.block_size)

# 将解密后的字节数组转换为字符串
plaintext = plaintext_bytes.decode()

print("明文：", plaintext)
