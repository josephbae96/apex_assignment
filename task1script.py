import jwt
import datetime

# Payload defined by document
payload = {
    "username": "jws-test",
    "entity": "apex",
    "datetime": datetime.datetime.now()
}

# Secret given by document
shared_secret: "1234567890"

