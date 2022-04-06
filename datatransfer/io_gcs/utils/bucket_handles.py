import base64
import os
import json

from google.cloud import storage
from google.oauth2 import service_account


def get_gcs_client(b64_key):
    decoded_str = base64.b64decode(b64_key).decode()
    json_acct_info = json.loads(decoded_str)
    credentials = service_account.Credentials.from_service_account_info(
        json_acct_info)
    return storage.Client(credentials=credentials)

def get_gcs_bucket(b64_key, bucket_nm):
    ''' return an access to gcs bucket. '''
    gcs_client = get_gcs_client(b64_key)
    return gcs_client.bucket(bucket_nm)
