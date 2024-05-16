import jwt
import datetime

# Payload defined by document
payload = {
    "username": "jws-test",
    "entity": "apex",
    "datetime": datetime.datetime.now()
}

# Shared secret given by document
shared_secret: "1234567890"

# Encode token
token = jwt.encode(
    payload,
    shared_secret,
    algorithm="HS512"
)

# Decode
decoded = jwt.decode(
    token, 
    shared_secret, 
    algorithms="HS512"
)

