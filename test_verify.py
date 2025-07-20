from unittest import TestCase
from verify_signature import load_inputs, verify_signature

class TestSignatureVerify(TestCase):
    def test_valid_signature(self):
        payload, signature, pubkey = load_inputs()
        result = verify_signature(payload, signature, pubkey)
        self.assertTrue(result)

    def test_invalid_signature(self):
        with open("payload.json", "r", encoding="utf-8") as f:
            original = f.read()
        with open("payload.json", "w", encoding="utf-8") as f:
            f.write(original + "random_text") #  modify the payload to make the signature invalid 
        try:
            payload, signature, pubkey = load_inputs()
            with self.assertRaises(Exception):
                verify_signature(payload, signature, pubkey)
        finally: 
            with open("payload.json", "w", encoding="utf-8") as f:
                f.write(original) # restore the original payload otherwise the next test will fail because of the modified payload


