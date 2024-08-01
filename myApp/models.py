from django.db import models


class sabad(models.Model):
    name=models.CharField(max_length=100)
    count=models.IntegerField()
    class Meta:
        db_table='sabad'