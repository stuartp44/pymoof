import base64
import getpass

import requests

from pymoof.tools import retrieve_bikes

def query(username, password):
    result = retrieve_bikes.query(username, password)
    print("Got bikes:", result)
    # Only get the first bike's encryption key
    encryption_key = result[0]["key"]["encryptionKey"]
    user_key_id = result[0]["key"]["userKeyId"]
    return encryption_key, user_key_id

if __name__ == "__main__":
    print(query())
