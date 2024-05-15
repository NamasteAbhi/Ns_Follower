from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class AES_CBC_NoPadding:
    def __init__(self):
        self.key = bytes.fromhex('71544467386b37424772353163676a70')
        self.iv = bytes.fromhex('665232347a6d7549527163304430576a')

    def encrypt(self, plaintext):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return ciphertext

    def decrypt(self, ciphertext):
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()
        return decrypted_text

if __name__ == '__main__':
    aes_cbc = AES_CBC_NoPadding()
    plaintext = b'489784xdfbdfbxfgbxfbxfgbfg25082*235'
    encrypted = aes_cbc.encrypt(plaintext)
    print("Encrypted:", encrypted)
    print(encrypted.hex())

    #"req_user_pk":"fd8f6cacce0e830442e4a91529510a3c","req_user_name":"bd89854f79634f7c130a8b218dd9ab6f"
    #"16f7fd21f346d4d60feaaf309df3d930","req_user_name":"006d8e2dac403bbf54839c8413ba42084904134f6cad74bd445bee5162c9ecf9"

    # encrypted=bytes.fromhex(encrypted.hex())
    #Decrypted: b'21085116*274\x00\x00\x00\x00'

    #Decrypted: b'66598345089*663\x00'
    #Decrypted: b'4909842508221085099*713\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    #Decrypted: b'4909842508221085099*335\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    #5d95dc403e5777d9fb41d52fcb672d3ff6135574540fa6a6070c0e8f5b67b40db9ba9fbd8a81e19c2c2fd3f9242313c0e6a0f6c63c006153312d684cb5b76e3577986ad4b2f88ec1eb9554c04af9d9ee6a33e856601fc2d78d26601024e41c139063ca14e4fc8eb90c70102e9cfbcd13*519\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00

    decrypted = aes_cbc.decrypt(bytes.fromhex('006d8e2dac403bbf54839c8413ba42084904134f6cad74bd445bee5162c9ecf9'))
    print("Decrypted:", len(decrypted))
    #
