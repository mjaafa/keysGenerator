from Crypto.PublicKey import RSA  # provided by pycryptodome



class SSLGenerator:
    def __init__(self):
        pass

    def generate(self, bits):
        key = RSA.generate(bits)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        return private_key, public_key
