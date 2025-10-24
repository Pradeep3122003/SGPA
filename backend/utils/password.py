import bcrypt
import os
from dotenv import load_dotenv
load_dotenv()
PEPPER = os.getenv("PEPPER", "a_strong_fallback_pepper_for_development_only")

def hash_password(password):
    peppered_password = password + PEPPER
    password_bytes = peppered_password.encode('utf-8')
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed

def verify_password(provided_password, stored_hash):
    peppered_password = provided_password + PEPPER
    password_bytes = peppered_password.encode('utf-8')

    try:
        stored_hash_bytes = stored_hash
        return bcrypt.checkpw(password_bytes, stored_hash_bytes)
    except Exception as e:
        print (e)
        return False


