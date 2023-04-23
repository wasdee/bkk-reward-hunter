import os
from cryptography.fernet import Fernet
from datetime import datetime
from pathlib import Path

# Read encrypted data from the file
output_dir = Path(__file__).parent.absolute() / "data" / "track_status"


def decrypt_all():
    for filename in output_dir.rglob("**/*.json.encrypted"):
        decrypt(filename)


def decrypt(filepath):
    with filepath.open("rb") as f:
        encrypted_data = f.read()

    # Get the encryption key from the environment variable
    key = os.getenv("REWARD_ENCRYPT_KEY")
    if key is None:
        raise Exception("REWARD_ENCRYPT_KEY not found")

    # Decrypt the data using the Fernet class
    fernety = Fernet(key)
    decrypted_data = fernety.decrypt(encrypted_data)

    # Print the decrypted data
    # print(decrypted_data)

    # apply json
    import json

    json_data = json.loads(decrypted_data)

    # to file
    output_dir = Path(__file__).parent.absolute() / "data" / "track_status"
    fp = output_dir / f"{filepath.stem}"
    with fp.open("w", encoding="utf-8") as f:
        f.write(json.dumps(json_data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    decrypt_all()
