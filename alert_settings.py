from django.db import models

class Alert_settings:
    id = models.IntegerField(primary_key=True, default=0)
    alert_method = models.CharField(max_length=250)
    key = models.CharField(max_length=250)
    val = models.TextField()
    is_verified = models.BooleanField(default=False)
    organization_id = models.IntegerField(default=0)