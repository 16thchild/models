from django.db import models

from workflow_objects.models.workflow import Workflows
from workflow_objects.models.alert_settings import Alert_settings


class Alert_mapping:
    dag_id = models.ForeignKey(Workflows, db_column="dag_id", related_name="airflow_dag_id", on_delete=models.CASCADE, primary_key=True)
    alert_id = models.ForeignKey(Alert_settings, db_column="id", related_name="alert_id", on_delete=models.CASCADE, primary_key=True)