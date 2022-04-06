import re

from rest_framework import serializers


class PreSignedUrlsSerializer(serializers.Serializer):
    bucket_name = serializers.CharField(max_length=255, allow_blank=True)
    bucket_folder_path = serializers.CharField(max_length=255, allow_blank=True)
    file_names = serializers.ListField(
        min_length=1,
        max_length=100,
        child=serializers.CharField(max_length=255)
    )
