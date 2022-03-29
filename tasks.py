from django.db import models

from workflow_objects.models.workflow import Workflows
from workflow_objects.models.task_type_master import Task_type_master

class Tasks:
    id = models.IntegerField(primary_key=True, default=0)
    task_id = models.CharField(max_length=250)
    airflow_dag_id = models.ForeignKey(Workflows, db_column="dag_id", related_name="airflow_dag_id", on_delete=models.CASCADE)
    task_type_id = models.ForeignKey(Task_type_master, db_column="id", related_name="task_type_id", on_delete=models.CASCADE)
    auth_info = models.TextField()
    endpoint = models.TextField()
    method = models.CharField(max_length=250)
    header = models.TextField()
    request_body = models.TextField()
    response_check = models.CharField(max_length=250)
