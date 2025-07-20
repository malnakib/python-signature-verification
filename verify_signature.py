import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
    
    # function loads the payload, signature, and public key from files
    
def load_inputs():
    # The payload is a JSON file which contains the data that was signed by the private key.
    with open("payload.json", "r", encoding="utf-8") as f:
        payload = f.read()
        print(payload)
        # signature is a base64 encoded string in a text file
    with open("signature.txt", "r", encoding="utf-8") as f:
        signature = base64.b64decode(f.read().strip())   # strip white spaces and newline characters
    # public key is a PEM encoded file
    with open("public.pem", "rb") as f:
        pubkey = serialization.load_pem_public_key(f.read())
    return payload, signature, pubkey



def verify_signature(payload, signature, pubkey):
    # This function verifies the signature of the payload by using of the public key.
    pubkey.verify(
        signature,                  # the signature to verify, decoded from base64
        payload.encode("utf-8"),    # the payload to verify
        padding.PKCS1v15(),         # padding scheme used for signing, PKCS1 v1.5 is adding extra bytes to the data before signing.
        hashes.SHA256()             # the hashing algorithm which used for signing
    )
    print("The signature is valid")
    return True

if __name__ == "__main__":
    payload, signature, pubkey = load_inputs()
    try:
        verify_signature(payload, signature, pubkey)
    except Exception as e:
        print("The signature verification failed")
