import random

from main import generate_keys, encrypt, decrypt, PublicKey, PrivateKey


def run_message(message: int, pub_key: PublicKey, private_key: PrivateKey) -> bool:
    encrypted_message = encrypt(message, pub_key)
    assert encrypted_message != message
    assert pub_key.e != private_key.d
    decrypted_message = decrypt(encrypted_message, private_key)
    return decrypted_message == message


TEST_KEYS_NUMBER = 100
TEST_NUMBER = 1000

def test_messages():
    for _ in range(TEST_KEYS_NUMBER):
        pub_key, private_key = generate_keys()
        for _ in range(TEST_NUMBER):
            message = random.randint(1, 10000000)
            assert run_message(message, pub_key, private_key)
