import base64

ciphertext = "OqRZEG9mm9B/y92h7+muv9Wo/hqLayfEHblOiW/1ePColbT1ffuMo1ApsQPHr4G02+zbOMm2tnftFXUAhKjlxV6rosUNFayqQABV7DhESBjMTNzgCI3tF5P5afpnQFK0Ux09uC6F4gHEE+MN4Ydt32pu25IbXW0GVRzoSjAaDxB+cQVsBQ2JKGlXPVEI+FfU"
decoded_ciphertext = base64.b64decode(ciphertext)

from Crypto.Cipher import AES
import binascii

key = "c0iOcX2p1v782YUY".encode('utf-8')  # 密钥长度必须是16、24或32字节（AES-128、AES-192或AES-256）
iv = "Bai1unC1ub1sBest".encode('utf-8')  # 偏移量（IV）必须是16字节
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(decoded_ciphertext)

# 去除填充字节
padding_byte = plaintext[-1]
if padding_byte == 0x00:
    plaintext = plaintext[:-1]

plaintext_str = plaintext.decode('utf-8')
print(plaintext_str)  # 输出解密的明文内容