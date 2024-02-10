import hmac
import hashlib

# Secret key for authentication
secret_key = b'my_secret_key'


# Function to generate an HMAC for a given message
def generate_hmac(message):
    return hmac.new(secret_key, message.encode('utf-8'), hashlib.sha256).hexdigest()


