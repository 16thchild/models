import os
from pydantic import BaseSettings
from typing import List
from pydantic.class_validators import validator

import logging

logger = logging.getLogger('root')


class EnvVars(BaseSettings):

    # Django settings
    django_secret_key: str ='1pj50e!^(id6-zr8k83(#^ub4@46p7yr4n-wai8=gg0ea!2@cw'
    django_arrowed_hosts: List[str] = ["*"]
    django_internal_ips: List[str] = ["*"]
    django_debug: bool = False

    # MySQL
    mysql_host: str ='127.0.0.1'
    mysql_port: int = 3306
    mysql_db_name: str = 'datalinkage'
    mysql_user_name: str = 'pleidak'
    mysql_user_password: str = 'abc123'

    # GCP
    gcp_b64_credentials: str = ''

    gcp_project_no: str = '364744031319'

    internal_api_domain_host_datatransfer: str = ''

    bucket_cors_origin: List[str] = ''

    @validator("bucket_cors_origin", pre=True, check_fields=False)
    def _assemble_cors_origins(cls, bucket_cors_origin):
        if isinstance(bucket_cors_origin, str):
            return [item.strip() for item in bucket_cors_origin.split(",")]
        return bucket_cors_origin

    # APP INSIGHT
    instrumentationkey: str = ''

if os.path.exists(".env"):
    env_vars = EnvVars(_env_file='.env', _env_file_encoding='utf-8')
else:
    try:
        env_vars = EnvVars()
    except Exception as e:
        logger.error('Env vars load error.')
        print(e)
        