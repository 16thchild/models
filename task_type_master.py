from django.db import models


class Public_connection:
    pass


class Task_type_master:
    id = models.IntegerField(default=0)
    conn_id = models.ForeignKey(Public_connection, db_column="id", related_name="conn_id", on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()