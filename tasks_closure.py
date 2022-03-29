from django.db import models

from workflow_objects.models.tasks import Tasks

class Tasks_closure:
    parent_id = models.ForeignKey(Tasks, db_column="id", related_name="parent_id", on_delete=models.CASCADE, primary_key=True)
    children_id = models.ForeignKey(Tasks, db_column="id", related_name="children_id", on_delete=models.CASCADE, primary_key=True)