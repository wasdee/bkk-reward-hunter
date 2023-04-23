import os
from pathlib import Path
import httpx

client = httpx.Client()

reqUrl = "https://reward.bangkok.go.th/reward2/track.php"

from scripts.header2text import text2header


header_raw = os.getenv("REWARD_HEADER")
if header_raw is None:
    raise Exception("REWARD_HEADER not found")

headersList: dict[str, str] = text2header(header_raw)
# print(headersList)

payload = ""

data = client.post(reqUrl, headers=headersList)

# print(data.json())

# encrypt data

key = os.getenv("REWARD_ENCRYPT_KEY")
if key is None:
    raise Exception("REWARD_ENCRYPT_KEY not found")

from cryptography.fernet import Fernet

fernety = Fernet(key)
encrypted = fernety.encrypt(data.content)

# save to file with date
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")
output_dir = Path(__file__).parent.absolute() / "data" / "track_status"
fp = output_dir / f"reward_{date}.json.encrypted"
with fp.open("wb") as f:
    f.write(encrypted)

if __name__ == "__main__":
    pass
