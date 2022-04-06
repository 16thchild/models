import os
from google.cloud import storage
from opencensus.trace import config_integration

from django.conf import settings

from env_vars import env_vars
from io_gcs.utils import structure_check
from io_gcs.utils import bucket_handles
from io_gcs.utils import constants
from io_gcs.utils import gen_logger


logger, tracer = gen_logger.get_logger(settings.APPNAME_IO_CGS)


def __get_bucket_name(tmp_bucket, bucket_data):
    # gcs url問い合わせ用変数まとめ
    return tmp_bucket if not bucket_data else bucket_data  ## TODO: bucketの有無確認

def __get_file_pathes(pathes_data, files_data):
    path = pathes_data
    files = files_data
    return [path + f for f in files]

def get_upload_urls(
    url_expiration, bucket_data,
    pathes_data, files_data, tmp_bucket):
    ''' return upload urls '''
    config_integration.trace_integrations(['google_cloud_clientlibs'])

    bucket_nm = __get_bucket_name(tmp_bucket, bucket_data)
    pathes = __get_file_pathes(pathes_data, files_data)

    import datetime

    bucket = bucket_handles.get_gcs_bucket(env_vars.gcp_b64_credentials, bucket_nm)
    urls = {}
    for path in pathes:
        file_nm, ext = os.path.splitext(path)
        content_type = constants.CONTENT_TYPE_DIC[ext] if ext in constants.CONTENT_TYPE_DIC else 'application/octet-stream'
        blob = bucket.blob(path)
        url = blob.generate_signed_url(
            version="v4",
            expiration=datetime.timedelta(minutes=url_expiration), 
            method="PUT",
            content_type=content_type,
        )
        urls[path] = {
            'url': url,
            'content-type': content_type
        }
    return urls


def get_download_urls(
    url_expiration, bucket_data,
    pathes_data, files_data, tmp_bucket):
    ''' return download urls '''
    config_integration.trace_integrations(['google_cloud_clientlibs'])

    bucket_nm = __get_bucket_name(tmp_bucket, bucket_data)
    pathes = __get_file_pathes(pathes_data, files_data)

    import datetime

    bucket = bucket_handles.get_gcs_bucket(env_vars.gcp_b64_credentials, bucket_nm)
    urls = {}
    for path in pathes:
        blob = bucket.blob(path)
        url = blob.generate_signed_url(
            version="v4",
            expiration=datetime.timedelta(minutes=url_expiration), 
            method="GET"
        )
        urls[path] = url
    return urls

