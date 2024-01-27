import rsa


class PubkeyInfo:
    def __init__(self, n, e):
        self.modulus = n
        self.exponent = e

    def __repr__(self):
        return f'{{"modulus": {self.modulus}, "exponent": {self.exponent}}}'

def from_private(bs: bytes):
    private_key = rsa.PrivateKey.load_pkcs1(bs)
    tmp = rsa.PublicKey(private_key.n, private_key.e)
    return PubkeyInfo(tmp.n, tmp.e)
