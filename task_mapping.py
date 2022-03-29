from django.db import models

from workflow_objects.models.workflow import Workflows
from workflow_objects.models.tags import Tags

class Tag_mapping:
    dag_id = models.ForeignKey(Workflows, db_column="dag_id", related_name="dag_id", on_delete=models.CASCADE, primary_key=True)
    tag_id = models.ForeignKey(Tags, db_column="tag_id", related_name="airflow_tag_id", on_delete=models.CASCADE, primary_key=True)