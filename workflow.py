from django.db import models

class Workflows(models.Model):
    dag_id = models.CharField(primary_key=True, max_length=250)
    organization_id = models.IntegerField(default=0)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    execution_time = models.IntegerField(default=0)
    shedule_interval = models.CharField(250)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)