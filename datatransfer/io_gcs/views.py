import sys
import traceback
import requests

from django.conf import settings
from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import structure_check
from .utils import err_responses
from .utils import constants
from .utils import gen_logger
from .api_docs import apidoc_upload_url
from .api_docs import apidoc_download_url
from .services import generate_presigned_url
from .serializers.get_presigned_urls_serializer import PreSignedUrlsSerializer

from opencensus.ext.azure.common import utils
from opencensus.trace import config_integration

config_integration.trace_integrations(['requests'])  # <-- this line enables the requests integration
# app insightsのrequestsでcloud role name とinstanceを設定
utils.azure_monitor_context['ai.cloud.role'] = 'datatransfer app'
utils.azure_monitor_context['ai.cloud.roleInstance'] = 'datatransfer server'

logger, tracer = gen_logger.get_logger(settings.APPNAME_IO_CGS)


def test_view(request):

    try:
        addr = request.META.get('REMOTE_ADDR')
        logger.warning("local:datatransfer:test logging")
        with tracer.span(name='test_view'):
            response = requests.get(url='https://www.wikipedia.org/wiki/Rabbit')
            print(response.status_code)
            return HttpResponse("<body>{}{}</body>".format(addr, response.text))
    except Exception as e:
        t, v, tb = sys.exc_info()
        logger.exception(traceback.format_tb(tb)[-1].replace('\n',''))

# Create your views here.
class GetUploadURL(APIView):
    ''' アップロード用URL問い合わせ '''
    serializer_class = PreSignedUrlsSerializer

    # 設定値
    expiration_min = constants.EXPIRATION_MIN  ## url有効期限
    tmp_bucket = constants.TEST_BUCKET ## 暫定bucket指定
    # request bodyのkeys
    bucket_key = 'bucket_name'
    pathes_key = 'bucket_folder_path'
    files_key = 'file_names'

    @extend_schema(request=PreSignedUrlsSerializer, **apidoc_upload_url.upload_url_api_doc)
    def post(self, request, **kwargs):
        try:
            serializer = PreSignedUrlsSerializer(data=request.data)
            if not serializer.is_valid():
                loc_list = ['request body']
                msg = serializer.errors
                err_type = 'invalid schema.'
                return Response(err_responses.response_with_err(loc_list, msg, err_type), status=422)

            # gcs url生成のためのargs調整
            bucket_data = serializer.validated_data.get(self.bucket_key, '')
            path_data = serializer.validated_data.get(self.pathes_key, '')
            files_data = serializer.validated_data.get(self.files_key, [])
            urls = generate_presigned_url.get_upload_urls(
                                            self.expiration_min,
                                            bucket_data,
                                            path_data,
                                            files_data,
                                            self.tmp_bucket)
            # response_data取得
            response_data = {
                    'message': "use upload_url like 'curl -X メソッド名 -H /'追加ヘッダ/' --upload-file 'アップロードするファイルのパス' 'リクエストするurl' ",
                    'urls': urls
            }
            return Response(response_data, status=200)
        except Exception as e:
            t, v, tb = sys.exc_info()
            logger.error(traceback.format_tb(tb)[-1].replace('\n',''))
            err_msg = err_responses.err_500_response(__name__, e)
            return Response(err_msg, status=500)


class GetDownloadURL(APIView):
    ''' ダウンロード用URL問い合わせ '''
    serializer_class = PreSignedUrlsSerializer

    # 設定値
    expiration_min = constants.EXPIRATION_MIN  ## url有効期限
    tmp_bucket = constants.TEST_BUCKET ## 暫定bucket指定
    # request bodyのkeys
    bucket_key = 'bucket_name'
    pathes_key = 'bucket_folder_path'
    files_key = 'file_names'

    @extend_schema(request=PreSignedUrlsSerializer, **apidoc_download_url.download_url_api_doc)
    def post(self, request, **kwargs):
        try:
            serializer = PreSignedUrlsSerializer(data=request.data)
            if not serializer.is_valid():
                loc_list = ['request body']
                msg = serializer.errors
                err_type = 'invalid schema.'
                return Response(err_responses.response_with_err(loc_list, msg, err_type), status=422)

            # gcs url生成のためのargs調整
            bucket_data = serializer.validated_data.get(self.bucket_key, '')
            path_data = serializer.validated_data.get(self.pathes_key, '')
            files_data = serializer.validated_data.get(self.files_key, [])
            urls = generate_presigned_url.get_download_urls(
                                            self.expiration_min,
                                            bucket_data,
                                            path_data,
                                            files_data,
                                            self.tmp_bucket)
            # response_data取得
            response_data = {
                    'message': "use download_url like 'curl 'リクエストするurl' ",
                    'urls': urls
            }
            return Response(response_data, status=200)
        except Exception as e:
            t, v, tb = sys.exc_info()
            logger.error(traceback.format_tb(tb)[-1].replace('\n',''))
            err_msg = err_responses.err_500_response(__name__, e)
            return Response(err_msg, status=500)


class HealthcheckView(APIView):
    def get(self, request):
        res = {"message": "datatransfer health check succeed."}
        return Response(res)
