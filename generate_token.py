import jwt
import datetime
from datetime import UTC

secret = "supersecretkey"

# Create JWT
payload = {
    "username": "fake_user",
    "password": "fake_pass",
    "exp": datetime.datetime.now(UTC) + datetime.timedelta(minutes=30)
}

token = jwt.encode(payload, secret, algorithm="HS256")
print("JWT:", token)

# Decode JWT
decoded = jwt.decode(token, secret, algorithms=["HS256"])
print("Decoded:", decoded)