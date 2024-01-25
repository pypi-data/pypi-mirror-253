import hashlib

import base58
import ecdsa
from Crypto.Hash import keccak


# pycryptodome = "^3.17"
# base58 = "^2.1.1"
# ecdsa = "^0.18.0"

class ADDR(bytes):
    """TRON Address."""

    def __new__(cls, value):
        if isinstance(value, bytes) and len(value) == 21:
            return bytes.__new__(cls, value)
        elif isinstance(value, str):
            if value.startswith('T') and len(value) == 34:
                return bytes.__new__(cls, base58.b58decode_check(value))
            elif value.startswith('41') and len(value) == 21 * 2:
                return bytes.__new__(cls, bytes.fromhex(value))
            elif value.startswith('0x') and len(value) == 21 * 2:
                return bytes.__new__(cls, b'\x41' + bytes.fromhex(value[2:]))

        raise ValueError("invalid address")

    def __str__(self):
        return base58.b58encode_check(self).decode('ascii')


class HEX(bytes):
    """HEX string."""

    def __new__(cls, value):
        if isinstance(value, bytes):
            return bytes.__new__(cls, value)
        elif isinstance(value, str):
            if value.startswith('0x'):
                return bytes.__new__(cls, bytes.fromhex(value[2:]))
            else:
                return bytes.__new__(cls, bytes.fromhex(value))

        raise ValueError("invalid hex")

    def __str__(self):
        return self.hex()


def sign_message(private_key: bytes, message: bytes) -> HEX:
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1, hashfunc=hashlib.sha256)
    public_key = sk.get_verifying_key().to_string()

    signature = sk.sign_deterministic(message)
    # recover address to get rec_id
    vks = ecdsa.VerifyingKey.from_public_key_recovery(
        signature, message, curve=ecdsa.SECP256k1, hashfunc=hashlib.sha256
    )
    v = None
    for v, pk in enumerate(vks):
        if pk.to_string() == public_key:
            break

    signature += bytes([v])
    return HEX(signature)


def sign_message_hash(private_key: bytes, message_hash: bytes) -> HEX:
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1, hashfunc=hashlib.sha256)
    public_key = sk.get_verifying_key().to_string()

    signature = sk.sign_digest_deterministic(message_hash)
    # recover address to get rec_id
    vks = ecdsa.VerifyingKey.from_public_key_recovery_with_digest(
        signature, message_hash, curve=ecdsa.SECP256k1, hashfunc=hashlib.sha256
    )
    v = None
    for v, pk in enumerate(vks):
        if pk.to_string() == public_key:
            break

    signature += bytes([v])
    return HEX(signature)


def keccak256(data: bytes) -> bytes:
    hasher = keccak.new(digest_bits=256)
    hasher.update(data)
    return hasher.digest()


def private_key_to_address(private_key: bytes) -> ADDR:
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1, hashfunc=hashlib.sha256)
    public_key = sk.get_verifying_key().to_string()

    addr = b"\x41" + keccak256(public_key)[-20:]
    return ADDR(addr)


def recover_address_from_message(signature: bytes, message: bytes) -> ADDR:
    vks = ecdsa.VerifyingKey.from_public_key_recovery(
        signature[:64], message, curve=ecdsa.SECP256k1, hashfunc=hashlib.sha256
    )
    pub_key = vks[signature[-1]].to_string()
    addr = b"\x41" + keccak256(pub_key)[-20:]
    return ADDR(addr)


def recover_address_from_message_hash(signature: bytes, message_hash: bytes) -> ADDR:
    vks = ecdsa.VerifyingKey.from_public_key_recovery_with_digest(
        signature[:64], message_hash, curve=ecdsa.SECP256k1, hashfunc=hashlib.sha256
    )
    pub_key = vks[signature[-1]].to_string()
    addr = b"\x41" + keccak256(pub_key)[-20:]
    return ADDR(addr)
