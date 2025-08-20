import os

def get_key(key_name):
    key_value = os.getenv(key_name)
    if key_value is None:
        print("No such key present!")
    return key_value