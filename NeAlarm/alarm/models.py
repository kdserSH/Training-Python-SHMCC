from django.db import models

# Create your models here.
class alarmdb(models.Model):
    Ne40 = models.CharField(max_length=100)
    # Index = models.IntegerField(primary_key=True)
    Time = models.DateTimeField()
    Level = models.CharField(max_length=30)
    Info = models.CharField(max_length=300)
    Id = models.IntegerField()


    class Meta:
        db_table = u'NE40-Alarm'
