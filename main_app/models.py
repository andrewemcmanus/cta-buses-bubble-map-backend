from django.db import models, migrations

class Bubble(models.Model):
    longitude = models.FloatField
    latitude = models.FloatField
    boardings = models.FloatField
    alightings = models.FloatField
    stop_id = models.IntegerField

    def __str__(self):
        return self.stop_id
