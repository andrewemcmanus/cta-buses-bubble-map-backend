from django.db import models, migrations
import jsonfield

class Bubble(models.Model):
    stop_id = models.IntegerField()
    boardings = models.FloatField()
    alightings = models.FloatField()
    location = jsonfield.JSONField()

    def __str__(self):
        return self.stop_id
