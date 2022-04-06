from drf_spectacular.utils import OpenApiParameter, OpenApiExample, OpenApiResponse
from drf_spectacular.types import OpenApiTypes


download_url_api_doc = {
    'description':'ダウンロード用URL発行',
    'responses': {
        200: OpenApiResponse(
            response='array', 
            description='messageのkeyにcurlでの使用方、file_urlsのkeyにfile名をkeyにしてvalにdownload urlが入ったdictが入ったdictをreturn',
        ),
        422: OpenApiResponse(
            response='array', 
            description='エラーレスポンス時の定型をreturn',
        )
    },
    'examples': [
        OpenApiExample(
            'request',
            value={
                "bucket_name": "some_bucket",
                "bucket_folder_path": "some/awsome/folder/",
                "file_names": [
                    "file_1.csv",
                    "file_2.csv",
                    "file_3.csv"
                ]
            },
            request_only=True
        ),
        OpenApiExample(
            '200',
            status_codes=['200'],
            value={
                "message": "use download_url like 'curl 'リクエストするurl' ",
                "upload_urls": {
                    "file1.csv": "https://storage.googleapis.com/some_bucket/some_awsome_url",
                    "file2.csv": "https://storage.googleapis.com/some_bucket/some_awsome_url",
                    "file3.csv": "https://storage.googleapis.com/some_bucket/some_awsome_url",
                },
            },
            response_only=True
        ),
        OpenApiExample(
            '422',
            status_codes=['422'],
            value={
                "detail": [
                    {
                        "loc": "request body",
                        "msg": "invalid request body.",
                        "type": "invalid schema."
                    }
                ]
            },
            response_only=True
        ),
    ]
}