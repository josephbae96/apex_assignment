import json
import hashlib
import base64

def generate_form_hash(json_form):
    
    sha256_digest = hashlib.sha256(json_form.encode("utf-8")).digest()

    base64_hash = base64.b64encode(sha256_digest).decode("utf-8")

    return base64_hash

