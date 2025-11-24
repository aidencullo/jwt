import jwt
import datetime
from datetime import UTC

secret = "supersecretkey"
payload = {
    "username": "fake_user",
    "password": "fake_pass",
    "exp": datetime.datetime.now(UTC) + datetime.timedelta(minutes=30)
}

token = jwt.encode(payload, secret, algorithm="HS256")
print(token)
