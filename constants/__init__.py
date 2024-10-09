import os

VERSION = "0.1.0"

VOLARA_TMP_DIR = os.path.expanduser("~/.volara")

TMP_MINER_LOG = f"{VOLARA_TMP_DIR}/miner.log"
TMP_PID_FILE = f"{VOLARA_TMP_DIR}/miner.pid"
TMP_TWITTER_AUTH = f"{VOLARA_TMP_DIR}/twitter.cookies"
TMP_DRIVE_AUTH = f"{VOLARA_TMP_DIR}/drive.token"
TMP_VOLARA_TOKEN = f"{VOLARA_TMP_DIR}/volara.jwt"

TIMELINE_SLEEP_INTERVAL = 120
ERROR_SLEEP_INTERVAL = 15
TARGET_TWEET_COUNT = 1000

VOLARA_API = "https://api.volara.xyz"

DLP_ADDRESS = "0x3f0c5b6E3525b302F5FDa5d93b47085999D472f8"
DATA_REGISTRATION_ADDRESS = "0xEA882bb75C54DE9A08bC46b46c396727B4BFe9a5"
TEE_POOL_ADDRESS = "0xF084Ca24B4E29Aa843898e0B12c465fAFD089965"

ENCRYPTION_SEED = "VOLARA_ENCRYPTION_SEED"

VALIDATOR_IMAGE = "https://github.com/volaradlp/validator/releases/download/v15/gsc-volara-proof-15.tar.gz"
VOLARA_API_KEY = "010063b9d4e17ccfbc119aaf68d2071a65613fd423f4181c72ed6a66b061eef03b6e0a1b21dda3fd9c56d474f9e3353df64582820648185ad562171e98fa5ac29ca9ccbe53a9896a13964acd85273bbb3bda7ce8aeb0b87d15da288747aef11c98e264a6fb88198960bfe82cc43d9bd7dbb744fdfa0d64aede62c1b4b82ec289cdf42f1416c497f921bd76c65adfe40d5cf3be3b4e9ddc361dfa906708598367958307803890bd2d731292a01b6c5676a2c8f2068ffea2d89db862e24d42fbecc2f2aee0a787810c3b47c0a1c121d3ba6aa2c3199ad2fe55ed6ae38e8b65081d9dec7ba952bb821ca2019493a5bd3cd55f55a3acb5159a496499bfea486350438e18a8f0433a46193ca904a7383636ce0848a3567a1ff79e6b1d5a8e68865479230ee35fd4a194caf9811c9f1362e7993bfb56a39ed90cde1bf37f8c3c0482fc7e46251549ee68d619565711b858b96c5b936751f226225cb5470e2f832ff8efca745ee6009ba7fd8e3fc355aa9f8a979d247f2ad05fca19ca4cac84121b86c4"

VOLARA_DLP_OWNER_PUBLIC_KEY_HEX = "0xebd0b3dbe1ba0b298bc05c5f22e9b9c0816ac4d5bbfe00d8da2ec11a2be5aa9f3532e107b2bfa9b2b3e521c570392f1868f05ae8e697a499a9d1883777102252"
VOLARA_DLP_OWNER_ADDRESS = "0x07cdb997c45a008B803FCC6904a0f7E4383a63b6"

BALANCE_ERROR_STRING = "Insufficient balance to submit to Vana Network: Claim Vana from the faucet: https://faucet.vana.org/moksha"
