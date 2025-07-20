import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def load_inputs():
    with open("payload.json", "r", encoding="utf-8") as f:
        payload = f.read()
        print(payload)
    with open("signature.txt", "r", encoding="utf-8") as f:
        signature = base64.b64decode(f.read().strip())
    with open("public.pem", "rb") as f:
        pubkey = serialization.load_pem_public_key(f.read())
    return payload, signature, pubkey



def verify_signature(payload, signature, pubkey):
    pubkey.verify(
        signature,
        payload.encode("utf-8"),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("The signature is valid")
    return True


