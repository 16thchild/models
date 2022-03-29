from django.db import models

class Tags(models.Models):
    tag_id = models.CharField(primary_key=True, max_length=250)
    tag_name = models.CharField(max_length=250)
    organization_id = models.IntegerField(default=0)