import json
from base64 import b64encode
from hashlib import sha1
from datetime import datetime
from .pastry_rsa import sign


CANONICAL = '''Method:%(method)s
Hashed Path:%(hashed_path)s
X-Ops-Content-Hash:%(hashed_body)s
X-Ops-Timestamp:%(timestamp)s
X-Ops-UserId:%(client)s'''


def hashencode(content):
    hashed = sha1(content.encode()).digest()
    return encode(hashed)


def encode(hashed):
    based = b64encode(hashed)
    return [based[i:i + 60].decode() for i in range(0, len(based), 60)]


def authorization_headers(keypath, canonical_source):
    with open(keypath, 'rb') as keyfile:
        signature = sign(canonical_source.encode(), keyfile.read())
    parts = encode(signature)
    return {
        'X-ops-authorization-%s' % (i + 1): val for i, val in enumerate(parts)
    }


def signed_headers(client, keypath, path, method='GET', data=None):
    hashed_path = ''.join(hashencode(path))
    body = ''
    if data:
        body = json.dumps(data)
    hashed_body = '\n'.join(hashencode(body))
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    canonical_source = CANONICAL % locals()

    headers = {
        'Accept': 'application/json',
        'X-ops-sign': 'version=1.0',
        'X-ops-userid': client,
        'X-ops-timestamp': timestamp,
        'X-ops-content-hash': hashed_body,
        'X-chef-version': '12.8.0'
    }
    headers.update(authorization_headers(keypath, canonical_source))
    return headers
