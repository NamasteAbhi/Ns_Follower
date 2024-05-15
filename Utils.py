from Crypto.Util.Padding import pad
from Crypto.Cipher import AES


class AES_CBC_NoPadding:
    def __init__(self):
        self.key = bytes.fromhex('71544467386b37424772353163676a70')
        self.iv = bytes.fromhex('665232347a6d7549527163304430576a')

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        ciphertext = cipher.encrypt(pad(plaintext,AES.block_size))
        return ciphertext

    def decrypt(self, ciphertext):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted_text = cipher.decrypt(ciphertext)
        return decrypted_text.rstrip(b'\x00')


if __name__ == '__main__':
    aes_cbc = AES_CBC_NoPadding()
    # plaintext =b'bc274838417192661d2db96e16520daaaNw90zallcQ3BSf9866xaNw90zallcadd8253fdb1ce2779205a4f8c94c7e6a*920'
    #
    # encrypted = aes_cbc.encrypt(plaintext)
    # print("Encrypted:", encrypted)
    # print(encrypted.hex())

    #"req_user_pk":"fd8f6cacce0e830442e4a91529510a3c","req_user_name":"bd89854f79634f7c130a8b218dd9ab6f"
    #"16f7fd21f346d4d60feaaf309df3d930","req_user_name":"006d8e2dac403bbf54839c8413ba42084904134f6cad74bd445bee5162c9ecf9"

    # encrypted=bytes.fromhex(encrypted.hex())
    #Decrypted: b'21085116*274\x00\x00\x00\x00'

    #Decrypted: b'66598345089*663\x00'
    #Decrypted: b'4909842508221085099*713\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    #Decrypted: b'4909842508221085099*335\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    #5d95dc403e5777d9fb41d52fcb672d3ff6135574540fa6a6070c0e8f5b67b40db9ba9fbd8a81e19c2c2fd3f9242313c0e6a0f6c63c006153312d684cb5b76e3577986ad4b2f88ec1eb9554c04af9d9ee6a33e856601fc2d78d26601024e41c139063ca14e4fc8eb90c70102e9cfbcd13*519\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00

    decrypted = aes_cbc.decrypt(bytes.fromhex('3326228154fa8b955157adcec898c04d1d747c740fb7d719a70ac76bc0536369b1f1c051a6f4b536929804c362e8b347'))
    print("Decrypted:", decrypted)
    #
